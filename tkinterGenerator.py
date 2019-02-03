import tkinter as tk
from tkinter import Tk

mainWin: Tk = tk.Tk()
mainWin.title("TkinterGenerator")
mainWin.minsize(600, 500)
mainWin.resizable(True, True)

theTitle = tk.Label(mainWin, text="TkinterGenerator", font=("Courier", 44))
theSubTitle = tk.Label(mainWin, text="By Djaro Donk", font=("Courier", 20))
goToCheckButton = tk.Button(mainWin, text="Create CheckButton", font=("Verdana", 20))
goToRadioButton = tk.Button(mainWin, text="Create RadioButton", font=("Verdana", 20))

theTitle.pack()
theSubTitle.pack()
goToCheckButton.pack()
goToRadioButton.pack()
mainWin.mainloop()