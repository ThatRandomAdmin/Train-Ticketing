#Package imports
import os
import tkinter as tk
from tkinter import filedialog
import shutil
import getpass

#View ticket
def viewtick(fname, sname, getdate):
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
        else:
            print("No ticket found")           
    else:
        print("No ticket found")

#UI for ticket viewing 
def mainUI(completeName):
    #Destroy the Window
    def destroyit():
        root.destroy()

    #Refresh the save button
    def refresh():
        button.configure(text="Save Ticket")

    #Save to downloads drive
    def save():
        usern = getpass.getuser()
        saveto = "C:/Users/" + usern + "/Downloads/"
        shutil.copy(completeName, str(saveto))
        button.configure(text="Succsefully downloaded!")
        button.after(1500, refresh)

    #Tkinter  code
    root = tk.Tk()
    root.title("Tickets")

    txtarea = tk.Text(root, width=40, height=10)
    txtarea.grid(row=0, column=0, pady=20)

    #inserting ticket data into the text box
    f = open(completeName, "r")
    data = f.read()
    txtarea.insert(tk.END, data)
    f.close()

    button = tk.Button(root, text="Save Ticket", command=save)
    button.grid(row=2, column=0, sticky="nsew")
    button1 = tk.Button(root, text="Close", command=destroyit)
    button1.grid(row=3, column=0, sticky="nsew")
    
    root.mainloop()
