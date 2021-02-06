import tkinter as tk
from tkinter import simpledialog


def location_prompt():
    ROOT = tk.Tk()

    ROOT.withdraw()
    ROOT.geometry('800x500')
    # the input dialog
    USER_INP = simpledialog.askstring(title="Path location",
                                      prompt="Where is your \"messages\" directory?")
    if USER_INP == None:
        USER_INP = ''

    USER_INP = USER_INP.lower()

    return USER_INP


def override_prompt():
    ROOT = tk.Tk()

    ROOT.withdraw()
    ROOT.geometry('800x500')
    # the input dialog
    USER_INP = simpledialog.askstring(title="Files were found",
                                      prompt="Do you want to override files? Y/N?")

    ROOT.focus_force()

    if USER_INP == None or USER_INP == '':
        USER_INP = 'n'

    USER_INP = USER_INP.lower()

    return USER_INP
