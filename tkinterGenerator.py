def log(text):
    print(text)
log("created log function")

import tkinter as tk
log("imported tkinter as tk")

# region Initialize Window
mainWin: tk.Tk = tk.Tk()
mainWin.title("TkinterGenerator")
mainWin.minsize(600, 500)
mainWin.resizable(True, True)
log("Initialized The window")
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
        log("Toggled the CheckBoxGenerator on")
    elif showCheck == 1 and (state == 0 or state == 2):
        showCheck = 0
        checkButtonGen.pack_forget()
        log("Toggled the CheckBoxGenerator off")
def toggleRadio(state):
    global showRadio
    if showRadio == 0 and (state == 1 or state == 2):
        showRadio = 1
        radioButtonGen.pack()
        log("Toggled the RadioBoxGenerator on")
    elif showRadio == 1 and (state == 0 or state == 2):
        showRadio = 0
        radioButtonGen.pack_forget()
        log("Toggled the RadioBoxGenerator off")
# endregion


previewCheck = tk.Frame(checkButtonGen)
log("created the previewCheck Frame")


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
        log("removed the previous preview")
        checkPreviewSuccess = 0
        temp_0 = 0
        temp_1 = 0
        buttonPreviewCheck = tk.Checkbutton(previewCheck,
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
        try:
            buttonPreviewCheck.config(background = self.allCheckVars["background"][:-1])
        except tk.TclError:
            log("!!!   Couldn't find background color. Used default (White) instead")
            buttonPreviewCheck.config(background="white")
        try:
            buttonPreviewCheck.config(activebackground=self.allCheckVars["activebackground"][:-1])
        except tk.TclError:
            log("!!!   Couldn't find activebackground color. Used default (White) instead")
            buttonPreviewCheck.config(activebackground="white")
        try:
            buttonPreviewCheck.config(foreground= self.allCheckVars["foreground"][:-1])
        except tk.TclError:
            log("!!!   Couldn't find foreground color. Used default (Black) instead")
            buttonPreviewCheck.config(foreground="black")
        try:
            buttonPreviewCheck.config(activeforeground= self.allCheckVars["activeforeground"][:-1])
        except tk.TclError:
            log("!!!   Couldn't find activeforeground color. Used default (Black) instead")
            buttonPreviewCheck.config(activeforeground="black")
        try:
            buttonPreviewCheck.config(disabledforeground= self.allCheckVars["disabledforeground"][:-1])
        except tk.TclError:
            log("!!!   Couldn't find disabled foreground color. Used default (gray40) instead")
            buttonPreviewCheck.config(disabledforeground="gray40")

        buttonPreviewCheck.pack()
        log("Succesfully made a preview")
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
log("Created the CheckBox object")

def previewCheckFunc(object):
    object.allCheckVars["text"] = checkButtonGenText.get("1.0", "end")
    object.allCheckVars["windowname"] = checkButtonGenWindow.get("1.0","end")
    object.allCheckVars["background"] = checkButtonGenBackground.get("1.0", "end")
    object.allCheckVars["activebackground"] = checkButtonGenActiveBackground.get("1.0", "end")
    object.allCheckVars["foreground"] = checkButtonGenForeground.get("1.0", "end")
    object.allCheckVars["activeforeground"] = checkButtonGenActiveForeground.get("1.0", "end")
    object.allCheckVars["disabledforeground"] = checkButtonGenDisabledForeground.get("1.0", "end")
    object.previewCheckButton()
    object.resetCheckVars()

def disableCheck(object):
    global buttonPreviewCheck
    if buttonPreviewCheck["state"] == "normal":
        buttonPreviewCheck.config(state="disabled")
    else:
        buttonPreviewCheck.config(state="normal")


# region Creates the Widgets
theTitle = tk.Label(mainWin, text="TkinterGenerator", font=("Courier", 44))
theSubTitle = tk.Label(mainWin, text="By Djaro Donk", font=("Courier", 20))
goToCheckButton = tk.Button(mainWin, text="Create CheckButton", font=("Verdana", 20), command=lambda: toggleCheck(2))
goToRadioButton = tk.Button(mainWin, text="Create RadioButton", font=("Verdana", 20), command=lambda: toggleRadio(2))
checkButtonGenText= tk.Text(checkButtonGen,font=("Arial",11),width=40,height=1)
checkButtonGenText.insert("insert","Your Text Here")
checkButtonGenWindow = tk.Text(checkButtonGen,font=("Arial",11),width=40,height=1)
checkButtonGenWindow.insert("insert","The name of the frame/window here")
checkButtonGenBackground = tk.Text(checkButtonGen,font=("Arial",11),width=40,height=1)
checkButtonGenBackground.insert("insert","The name of the background colour here")
checkButtonGenActiveBackground = tk.Text(checkButtonGen,font=("Arial",11),width=40,height=1)
checkButtonGenActiveBackground.insert("insert","The name of the active background colour here")
checkButtonGenForeground = tk.Text(checkButtonGen,font=("Arial",11),width=40,height=1)
checkButtonGenForeground.insert("insert","The name of the foreground colour here")
checkButtonGenActiveForeground = tk.Text(checkButtonGen,font=("Arial",11),width=40,height=1)
checkButtonGenActiveForeground.insert("insert","The name of the active foreground colour here")
checkButtonGenDisabledForeground = tk.Text(checkButtonGen,font=("Arial",11),width=40,height=1)
checkButtonGenDisabledForeground.insert("insert","The name of the disabled foreground colour here")


checkButtonpreviewCheck = tk.Button(checkButtonGen,text="Create previewCheck",
                                    command=lambda: previewCheckFunc(allTheChecks))

#endregion

# region Packs the Widgets
theTitle.pack()
theSubTitle.pack()
tk.Label(mainWin, text="use all_colors.py to see all available colours").pack()
goToCheckButton.pack()
goToRadioButton.pack()
checkButtonpreviewCheck.pack()
tk.Button(checkButtonGen, text="Disable/enable preview button", command=lambda:disableCheck(allTheChecks)).pack()
tk.Label(radioButtonGen, text="My radio text").pack()
checkButtonGenText.pack()
checkButtonGenWindow.pack()
checkButtonGenBackground.pack()
checkButtonGenActiveBackground.pack()
checkButtonGenForeground.pack()
checkButtonGenActiveForeground.pack()
checkButtonGenDisabledForeground.pack()
previewCheck.pack_forget()
previewCheck.pack()
mainWin.mainloop()
# endregion.
