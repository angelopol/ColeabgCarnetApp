import socket
import tkinter as tk
from tkinter import *
from datetime import datetime
from datetime import timedelta
from tkcalendar import Calendar
from babel.dates import format_date, parse_date, get_day_names, get_month_names
from babel.numbers import *

def shortcut(presioned, LenShortcut, KeyOne, Function, KeyTwo = ""):

    if LenShortcut == 1:

        if len(presioned) == LenShortcut and (presioned[0] == KeyOne):

            Function()

    elif LenShortcut == 2:

        if len(presioned) == LenShortcut and (presioned[0] == KeyOne and presioned[1] == KeyTwo):

            Function()

def FileRead(rute):
    List = []
    with open(rute,"r") as file:
        for line in file:
            List.append(line.replace("\n", ""))
    return List

def IsConnected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

def CenterWindow(wventana, hventana, root):

    wtotal = root.winfo_screenwidth()
    htotal = root.winfo_screenheight()
    pwidth = round(wtotal/2-int(wventana)/2)
    pheight = round(htotal/2-int(hventana)/2)
    root.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

def SetDate(root, EmisionEntry, VencimientoEntry = False, YearMonthDay = False, fix = False):

    window = tk.Toplevel()
    window.iconbitmap("assets/logo.ico")
    window.geometry(("260x190"))
    window.resizable(False,False)
    window.title("Cierre el calendario para seleccionar la fecha")
    CenterWindow("260", "190", window)
    window.transient(root)
    window.focus()

    now = datetime.datetime.now()

    cal = Calendar(window, selectmode = 'day', year = now.year, month = now.month, day = now.day)
    cal.pack()

    def on_close():

        if YearMonthDay == False:
            try:
                date = datetime.datetime.strptime(((datetime.datetime.strptime((cal.get_date()).replace('/', '-'), '%d-%m-%y')).strftime('%d-%m-%Y')), '%d-%m-%Y')
            except:
                date = datetime.datetime.strptime(((datetime.datetime.strptime((cal.get_date()).replace('/', '-'), '%m-%d-%y')).strftime('%d-%m-%Y')), '%d-%m-%Y')
        else:
            try:
                date = datetime.datetime.strptime(((datetime.datetime.strptime((cal.get_date()).replace('/', '-'), '%d-%m-%y')).strftime('%Y-%m-%d')), '%Y-%m-%d')
            except:
                date = datetime.datetime.strptime(((datetime.datetime.strptime((cal.get_date()).replace('/', '-'), '%m-%d-%y')).strftime('%Y-%m-%d')), '%Y-%m-%d')

        EmisionEntry.config(state="normal")
        EmisionEntry.delete(0, END)
        if YearMonthDay == False:
            EmisionEntry.insert(0, (date).strftime('%d-%m-%Y'))
        else:
            EmisionEntry.insert(0, (date).strftime('%Y-%m-%d'))
        EmisionEntry.config(state="disabled")

        if VencimientoEntry != False:
            VencimientoEntry.config(state="normal")
            VencimientoEntry.delete(0, END)
            if fix:
                VencimientoEntry.insert(0, date.strftime('%d-%m-%Y'))
            else:
                VencimientoEntry.insert(0, (date + timedelta(days=730)).strftime('%d-%m-%Y'))
            VencimientoEntry.config(state="disabled")

        window.destroy()

    window.protocol("WM_DELETE_WINDOW", on_close)

    window.mainloop()