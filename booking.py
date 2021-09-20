#Package imports
import os

#Save data to a text file
def enter(fname, sname, geton, leave, ticktype, getdate):
    save_path = 'tickets/'
    file_name = (getdate.replace("/", "_") + (".txt"))
    fldr = (fname[0] + sname).lower()
    fldr_path = save_path + fldr

    #Working out distance travled
    if geton == ("Station 1"):
        board = 1
    elif geton == ("Station 2"):
        board = 10
    elif geton == ("Station 3"):
        board = 15
    elif geton == ("Station 4"):
        board = 25
    elif geton == ("Station 5"):
        board = 40

    if leave == ("Station 1"):
        depart = 1
    elif leave == ("Station 2"):
        depart = 10
    elif leave == ("Station 3"):
        depart = 15
    elif leave == ("Station 4"):
        depart = 25
    elif leave == ("Station 5"):
        depart = 40

    #Working out cost
    cost = abs((board - depart) / 2)
    if ticktype == ("Child ticket"):
        cost = cost * 0.7
    cost = ("%.2f" % round(cost, 2))
    cost = str(cost)
    cost = "£"+cost

    #Making sure file path exists
    if os.path.exists(fldr_path):
        #Adding data to the file
        completeName = fldr_path + '/' + file_name

        data1 = ("\n########################################\n Name: ", fname.title(), " ", sname.title(), "\n Date: ", getdate, "\n Joining: ", geton, "\n Departing: ", leave, "\n", "\n Ticket type: ", ticktype, "\n", "\n Cost: ", cost)
        data = ''.join(data1)

        if os.path.exists(completeName):
            f = open(completeName, 'a')
            f.write((data))
            f.close()
        else:
            f = open(completeName, 'x')
            f.write((data))
            f.close()

    else:
        #Checking if tickets folder exists
        if os.path.exists(save_path):
            #Adding data to the file and creating new folder
            os.mkdir(fldr_path)
            completeName = fldr_path + '/' + file_name

            data1 = ("\n########################################\n Name: ", fname, " ", sname, "\n Date: ", getdate, "\n Joining: ", geton, "\n Departing: ", leave, "\n", "\n Ticket type: ", ticktype, "\n", "\n Cost: ", cost)
            data = ''.join(data1)

            if os.path.exists(completeName):
                f = open(completeName, 'a')
                f.write((data))
                f.close()
            else:
                f = open(completeName, 'x')
                f.write((data))
                f.close()
        else:
            #Adding data to the file and creating new folder
            os.mkdir(save_path)
            os.mkdir(fldr_path)
            completeName = fldr_path + '/' + file_name

            data1 = ("\n########################################\n Name: ", fname, " ", sname, "\n Date: ", getdate, "\n Joining: ", geton, "\n Departing: ", leave, "\n", "\n Ticket type: ", ticktype, "\n", "\n Cost: ", cost)
            data = ''.join(data1)

            if os.path.exists(completeName):
                f = open(completeName, 'a')
                f.write((data))
                f.close()
            else:
                f = open(completeName, 'x')
                f.write((data))
                f.close()
