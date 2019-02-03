import tkinter as tk
from tkinter import Tk


mainWin: Tk = tk.Tk()
mainWin.title("TkinterGenerator")
mainWin.minsize(600, 500)
mainWin.resizable(True, True)


showCheck = 0
showRadio = 0
checkButtonGen = tk.Frame(mainWin)
radioButtonGen = tk.Frame(mainWin)


def toggleCheck(state):
    global showCheck
    if showCheck == 0 and (state == 1 or state == 2):
        showCheck = 1
        checkButtonGen.pack()
    elif showCheck == 1 and (state == 0 or state == 2):
        showCheck = 0
        checkButtonGen.pack_forget()
def toggleRadio(state):
    global showRadio
    if showRadio == 0 and (state == 1 or state == 2):
        showRadio = 1
        radioButtonGen.pack()
    elif showRadio == 1 and (state == 0 or state == 2):
        showRadio = 0
        radioButtonGen.pack_forget()


theTitle = tk.Label(mainWin, text="TkinterGenerator", font=("Courier", 44))
theSubTitle = tk.Label(mainWin, text="By Djaro Donk", font=("Courier", 20))
goToCheckButton = tk.Button(mainWin, text="Create CheckButton", font=("Verdana", 20), command=lambda: toggleCheck(2))
goToRadioButton = tk.Button(mainWin, text="Create RadioButton", font=("Verdana", 20), command=lambda: toggleRadio(2))
theTitle.pack()
theSubTitle.pack()
goToCheckButton.pack()
goToRadioButton.pack()
tk.Label(checkButtonGen, text="My check text").pack()
tk.Label(radioButtonGen, text="My radio text").pack()
mainWin.mainloop()