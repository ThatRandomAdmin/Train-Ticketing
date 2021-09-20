#Package imports
import tkinter as tk
from tkinter import filedialog
from tkcalendar import DateEntry
import os

#File imports
from booking import enter
from ticketview import mainUI


#Tkinter code
def main():
    root = tk.Tk()
    root.title("Train Ticketing System")

    button_1 = tk.Button(master=root,
                         width=30,
                         height=7,
                         text="Book a Ticket",
                         command=book)
    button_1.grid(row=0, column=0, sticky="nsew")

    button_2 = tk.Button(master=root,
                         width=30,
                         height=7,
                         text="View tickets",
                         command=view)
    button_2.grid(row=0, column=1, sticky="nsew")

    root.mainloop()

def book():
    root1 = tk.Tk()
    root1.title("Book a ticket")

    #Heading
    label1 = tk.Label(master=root1, width=20, height=2, text="Book a ticket")
    label1.config(font=("", 20))
    label1.grid(row=0, column=0, sticky="nsew")

    #Name
    fn = tk.Entry(master=root1)
    fn.insert(0, "Enter your first name.")
    fn.grid(row=2, column=0)
    sn = tk.Entry(master=root1)
    sn.insert(0, "Enter your last name.")
    sn.grid(row=3, column=0)

    #Spacing
    Label = tk.Label(master=root1, width=13, height=1)
    Label.grid(row=4, column=0)

    #Leaving
    OptionList = ["Station 1", "Station 2", "Station 3", "Station 4", "Station 5"]
    variable1 = tk.StringVar(root1)
    variable1.set(OptionList[0])
    opt = tk.OptionMenu(root1, variable1, *OptionList)
    opt.grid(row=5, column=0)

    #Spacing
    Label = tk.Label(master=root1, width=13, height=1, text="to")
    Label.grid(row=6, column=0)

    #Destination
    OptionList = ["Station 1", "Station 2", "Station 3", "Station 4", "Station 5"]
    variable2 = tk.StringVar(root1)
    variable2.set(OptionList[0])
    opt = tk.OptionMenu(root1, variable2, *OptionList)
    opt.grid(row=7, column=0)

    #Spacing
    Label = tk.Label(master=root1, width=13, height=1)
    Label.grid(row=8, column=0)

    #Ticket type
    OptionList = ["Adult ticket", "Child ticket"]
    variable3 = tk.StringVar(root1)
    variable3.set(OptionList[0])
    opt = tk.OptionMenu(root1, variable3, *OptionList)
    opt.grid(row=9, column=0)

    #Spacing
    Label = tk.Label(master=root1, width=13, height=1)
    Label.grid(row=10, column=0)

    #Date entry
    cal = DateEntry(root1,
                    width=13,
                    background='darkblue',
                    foreground='white',
                    borderwidth=2)
    cal.insert(
        0,
        "                                         Enter the date                                                                                                                      "
    )
    cal.grid(row=11, column=0, sticky="nsew")

    #Spacing
    Label1 = tk.Label(master=root1, width=13, height=1)
    Label1.grid(row=12, column=0)

    #Refresh the error message
    def refresh():
        label1.configure(text="Book a ticket")

    #Destroy the Window
    def destroyit():
        root1.destroy()

    #Epic variables
    fname1 = fn.get()
    sname1 = sn.get()
    getdate1 = cal.get()

    #running booking
    def enters():
        #Gathering input data
        fname = fn.get()
        sname = sn.get()
        geton = variable1.get()
        leave = variable2.get()
        ticktype = variable3.get()
        getdate = cal.get()

        #Checks for valid data
        if fname == fname1:
            label1.configure(text="Please enter your forename.")
            label1.after(1200, refresh)
            
        elif sname == sname1:
            label1.configure(text="Please enter your surname.")
            label1.after(1200, refresh)

        elif geton == leave:
            label1.configure(text="Please enter valid stations.")
            label1.after(1200, refresh)

        elif getdate == getdate1:
            label1.configure(text="Please enter a date.")
            label1.after(1200, refresh)

        #Sending data
        else:
            enter(fname, sname, geton, leave, ticktype, getdate)
            label1.configure(text="Succsefully booked!")
            label1.after(1500, destroyit)

    #Button to enter the inputed data
    button = tk.Button(root1, text="Book now", command=enters)
    button.grid(row=13, column=0, sticky="nsew")

    root1.mainloop()


def view():
    root2 = tk.Tk()
    root2.title("View Tickets")

    #Heading
    label1 = tk.Label(master=root2,
                      width=20,
                      height=2,
                      text="View Tickets")
    label1.config(font=("", 20))
    label1.grid(row=0, column=0, sticky="nsew")

    #Name
    fn = tk.Entry(master=root2)
    fn.insert(0, "Enter your first name.")
    fn.grid(row=2, column=0)
    sn = tk.Entry(master=root2)
    sn.insert(0, "Enter your last name.")
    sn.grid(row=3, column=0)

    #Spacing
    Label = tk.Label(master=root2, width=13, height=1)
    Label.grid(row=4, column=0)

    #Date entry
    cal = DateEntry(root2,
                    width=13,
                    background='darkblue',
                    foreground='white',
                    borderwidth=2)
    cal.insert(
        0,
        "                                        Enter the date                                                                                                                      "
    )
    cal.grid(row=5, column=0, sticky="nsew")

    #Spacing
    Label = tk.Label(master=root2, width=13, height=1)
    Label.grid(row=6, column=0)

    #Refresh the error message
    def refresh():
        label1.configure(text="View Tickets")

    #Destroy the Window
    def destroyit():
        root2.destroy()

    #Epic variables
    fname1 = fn.get()
    sname1 = sn.get()
    getdate1 = cal.get()

    #running viewing
    def enters():
        #Gathering input data
        fname = fn.get()
        sname = sn.get()
        getdate = cal.get()

        #Checks for valid data
        if fname == fname1:
            label1.configure(text="Please enter your forename.")
            label1.after(1200, refresh)

        elif sname == sname1:
            label1.configure(text="Please enter your surname.")
            label1.after(1200, refresh)

        elif getdate == getdate1:
            label1.configure(text="Please enter a date.")
            label1.after(1200, refresh)

        #Sending data
        else:
            #Getting ticket savepath
            save_path = 'tickets/'
            file_name = (getdate.replace("/", "_") + (".txt"))
            fldr = fname[0] + sname
            fldr_path = save_path + fldr

            #Checking if ticket exists
            if os.path.exists(fldr_path):
                completeName = fldr_path + '/' + file_name
                if os.path.exists(completeName):
                    mainUI(completeName)
                    label1.configure(text="Succsefully found!")
                    label1.after(1500, destroyit)
                else:
                    label1.configure(text="No ticket found.")
                    label1.after(1200, refresh)
            else:
                label1.configure(text="No ticket found.")
                label1.after(1200, refresh)

    #Button to enter the inputed data
    button = tk.Button(root2, text="View now", command=enters)
    button.grid(row=7, column=0, sticky="nsew")
    button1 = tk.Button(root2, text="Close", command=destroyit)
    button1.grid(row=8, column=0, sticky="nsew")

    root2.mainloop()

main()
