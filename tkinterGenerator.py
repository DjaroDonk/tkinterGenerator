import tkinter as tk
from tkinter import Tk

# region Initialize Window
mainWin: Tk = tk.Tk()
mainWin.title("TkinterGenerator")
mainWin.minsize(600, 500)
mainWin.resizable(True, True)
#endregion

# region Toggle Check and Radio
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
# endregion


previewCheck = tk.Frame(checkButtonGen)

buttonPreviewCheck = tk.Checkbutton()
buttonPreviewCheck.pack_forget()
class theChecks():
    allCheckVars = {"windowname": "[Insert Window Here]",
                    "background": "white",
                    "activebackground": "white",
                    "foreground": "black",
                    "activeforeground": "black",
                    "disabledforeground": "black",
                    "selectcolor": "white",
                    "width": None,
                    "height": None,
                    "padx": 0,
                    "pady": 0,
                    "borderwidth": 0,
                    "cursor": "arrow",
                    "offvalue": 0,
                    "onvalue": 1,
                    "indicatoron": True,
                    "textortextvar": "text",
                    "text": "",
                    "textvar": None}
    tkinterName = "tkinter"
    def resetCheckVars(self):
        self.allCheckVars = {"windowname": "[Insert Window Here]",
                        "background": "white",
                        "activebackground": "white",
                        "foreground": "black",
                        "activeforeground": "black",
                        "disabledforeground": "black",
                        "selectcolor": "white",
                        "width": None,
                        "height": None,
                        "padx": 0,
                        "pady": 0,
                        "borderwidth": 0,
                        "cursor": "arrow",
                        "offvalue": 0,
                        "onvalue": 1,
                        "indicatoron": True,
                        "textortextvar": "text",
                        "text": "",
                        "textvar": None}
    checkButtonCode = ""
    allChecks = []
    def newCheck(self):
        global allCheckVars
        if self.allCheckVars["textortextvar"] == "text":
            self.allChecks.append(tk.Checkbutton(previewCheck,
                                                 background=self.allCheckVars["background"],
                                                 activebackground=self.allCheckVars["activebackground"],
                                                 foreground=self.allCheckVars["activeforeground"],
                                                 activeforeground=self.allCheckVars["activeforeground"],
                                                 disabledforeground=self.allCheckVars["disabledforeground"],
                                                 selectcolor=self.allCheckVars["selectcolor"],
                                                 width=self.allCheckVars["width"],
                                                 height=self.allCheckVars["height"],
                                                 padx=self.allCheckVars["padx"],
                                                 pady=self.allCheckVars["pady"],
                                                 borderwidth=self.allCheckVars["borderwidth"],
                                                 cursor=self.allCheckVars["cursor"],
                                                 offvalue=self.allCheckVars["offvalue"],
                                                 onvalue=self.allCheckVars["onvalue"],
                                                 indicatoron=self.allCheckVars["indicatoron"],
                                                 text=self.allCheckVars["text"]))
            self.checkButtonCode.append(
                f"{self.tkinterName}.Checkbutton({self.allCheckVars['windowname']}," +
                f"background={self.allCheckVars['background']}," +
                f"activebackground={self.allCheckVars['activebackground']}," +
                f"foreground={self.allCheckVars['foreground']}," +
                f"activeforeground={self.allCheckVars['activeforeground']}," +
                f"disabledforeground={self.allCheckVars['disabledforeground']}," +
                f"selectvolor={self.allCheckVars['selectcolor']}," +
                f"width={self.allCheckVars['width']},height={self.allCheckVars['height']}," +
                f"padx={self.allCheckVars['padx']},pady={self.allCheckVars['pady']}," +
                f"borderwidth={self.allCheckVars['borderwidth']}," +
                f"cursor={self.allCheckVars['cursor']},offvalue={self.allCheckVars['offvalue']}," +
                f"onvalue={self.allCheckVars['onvalue']}," +
                f"indicatoron={self.allCheckVars['indicatoron']},textvar={self.allCheckVars['textvar']})")
        elif self.allCheckVars["textortextvar"] == "textvar":
            self.allChecks.append(tk.Checkbutton(previewCheck,
                                                 background=self.allCheckVars["background"],
                                                 activebackground=self.allCheckVars["activebackground"],
                                                 foreground=self.allCheckVars["activeforeground"],
                                                 activeforeground=self.allCheckVars["activeforeground"],
                                                 disabledforeground=self.allCheckVars["disabledforeground"],
                                                 selectvolor=self.allCheckVars["selectcolor"],
                                                 width=self.allCheckVars["width"],
                                                 height=self.allCheckVars["height"],
                                                 padx=self.allCheckVars["padx"],
                                                 pady=self.allCheckVars["pady"],
                                                 borderwidth=self.allCheckVars["borderwidth"],
                                                 cursor=self.allCheckVars["cursor"],
                                                 offvalue=self.allCheckVars["offvalue"],
                                                 onvalue=self.allCheckVars["onvalue"],
                                                 indicatoron=self.allCheckVars["indicatoron"],
                                                 textvar=self.allCheckVars["textvar"]))
            self.checkButtonCode.append(
                f"{self.tkinterName}.Checkbutton({self.allCheckVars['windowname']},"+
                f"background={self.allCheckVars['background']}," +
                f"activebackground={self.allCheckVars['activebackground']},"+
                f"foreground={self.allCheckVars['foreground']}," +
                f"activeforeground={self.allCheckVars['activeforeground']},"+
                f"disabledforeground={self.allCheckVars['disabledforeground']}," +
                f"selectvolor={self.allCheckVars['selectcolor']},"+
                f"width={self.allCheckVars['width']},height={self.allCheckVars['height']}," +
                f"padx={self.allCheckVars['padx']},pady={self.allCheckVars['pady']},"+
                f"borderwidth={self.allCheckVars['borderwidth']}," +
                f"cursor={self.allCheckVars['cursor']},offvalue={self.allCheckVars['offvalue']},"+
                f"onvalue={self.allCheckVars['onvalue']}," +
                f"indicatoron={self.allCheckVars['indicatoron']},textvar={self.allCheckVars['textvar']})")
    def previewCheckButton(self):
        global buttonPreviewCheck
        buttonPreviewCheck.pack()
        buttonPreviewCheck.pack_forget()
        buttonPreviewCheck = tk.Checkbutton(previewCheck,
                           background=self.allCheckVars["background"],
                           activebackground=self.allCheckVars["activebackground"],
                           foreground=self.allCheckVars["activeforeground"],
                           activeforeground=self.allCheckVars["activeforeground"],
                           disabledforeground=self.allCheckVars["disabledforeground"],
                           selectcolor=self.allCheckVars["selectcolor"],
                           width=self.allCheckVars["width"],
                           height=self.allCheckVars["height"],
                           padx=self.allCheckVars["padx"],
                           pady=self.allCheckVars["pady"],
                           borderwidth=self.allCheckVars["borderwidth"],
                           cursor=self.allCheckVars["cursor"],
                           offvalue=self.allCheckVars["offvalue"],
                           onvalue=self.allCheckVars["onvalue"],
                           indicatoron=self.allCheckVars["indicatoron"])
        if self.allCheckVars["textortextvar"] == "text":
            buttonPreviewCheck["text"] = self.allCheckVars["text"][:-1]
        else:
            buttonPreviewCheck["textvar"] = self.allCheckVars["textvar"]
        buttonPreviewCheck.pack()
    # region Old script for a single preview, doesnt work. Don't know why not!!
    # def previewCheckButton(self):
    #     global buttonPreviewCheck
    #     buttonPreviewCheck.pack()
    #     buttonPreviewCheck.pack_forget()
    #     if self.allCheckVars["textortextvar"] == "text":
    #         buttonpreviewCheck = tk.Checkbutton(previewCheck,
    #                        background=self.allCheckVars["background"],
    #                        activebackground=self.allCheckVars["activebackground"],
    #                        foreground=self.allCheckVars["activeforeground"],
    #                        activeforeground=self.allCheckVars["activeforeground"],
    #                        disabledforeground=self.allCheckVars["disabledforeground"],
    #                        selectcolor=self.allCheckVars["selectcolor"],
    #                        width=self.allCheckVars["width"],
    #                        height=self.allCheckVars["height"],
    #                        padx=self.allCheckVars["padx"],
    #                        pady=self.allCheckVars["pady"],
    #                        borderwidth=self.allCheckVars["borderwidth"],
    #                        cursor=self.allCheckVars["cursor"],
    #                        offvalue=self.allCheckVars["offvalue"],
    #                        onvalue=self.allCheckVars["onvalue"],
    #                        indicatoron=self.allCheckVars["indicatoron"],
    #                        text=self.allCheckVars["text"][:-1])
    #         buttonpreviewCheck.pack(anchor="center")
    #     elif self.allCheckVars["textortextvar"] == "textvar":
    #         buttonpreviewCheck = tk.Checkbutton(previewCheck,
    #                        background=self.allCheckVars["background"],
    #                        activebackground=self.allCheckVars["activebackground"],
    #                        foreground=self.allCheckVars["activeforeground"],
    #                        activeforeground=self.allCheckVars["activeforeground"],
    #                        disabledforeground=self.allCheckVars["disabledforeground"],
    #                        selectvolor=self.allCheckVars["selectcolor"],
    #                        width=self.allCheckVars["width"],
    #                        height=self.allCheckVars["height"],
    #                        padx=self.allCheckVars["padx"],
    #                        pady=self.allCheckVars["pady"],
    #                        borderwidth=self.allCheckVars["borderwidth"],
    #                        cursor=self.allCheckVars["cursor"],
    #                        offvalue=self.allCheckVars["offvalue"],
    #                        onvalue=self.allCheckVars["onvalue"],
    #                        indicatoron=self.allCheckVars["indicatoron"],
    #                        textvar=self.allCheckVars["textvar"])
    #         buttonpreviewCheck.pack(anchor="center")
    # endregion
    def fullPreviewCheck(self):
        for i in self.allChecks:
            previewCheck.pack_forget()
            i.pack_forget()
            i.pack()
            previewCheck.pack()

allTheChecks = theChecks()

def previewCheckFunc(object):
    object.allCheckVars["text"] = checkButtonGenText.get("1.0", "end")
    object.previewCheckButton()


# region Creates the Widgets
# region The main screen
theTitle = tk.Label(mainWin, text="TkinterGenerator", font=("Courier", 44))
theSubTitle = tk.Label(mainWin, text="By Djaro Donk", font=("Courier", 20))
goToCheckButton = tk.Button(mainWin, text="Create CheckButton", font=("Verdana", 20), command=lambda: toggleCheck(2))
goToRadioButton = tk.Button(mainWin, text="Create RadioButton", font=("Verdana", 20), command=lambda: toggleRadio(2))
checkButtonGenText= tk.Text(checkButtonGen,font=("Arial",11),width=40,height=1)
checkButtonGenText.insert("insert","Your Text Here")
checkButtonpreviewCheck = tk.Button(checkButtonGen,text="Create previewCheck",
                                    command=lambda: previewCheckFunc(allTheChecks))

# endregion
# region The CheckBox Widgets

# endregion
#endregion

# region Packs the Widgets
theTitle.pack()
theSubTitle.pack()
goToCheckButton.pack()
goToRadioButton.pack()
checkButtonpreviewCheck.pack()
tk.Label(radioButtonGen, text="My radio text").pack()
checkButtonGenText.pack()
previewCheck.pack_forget()
previewCheck.pack()
mainWin.mainloop()
# endregion.
