import Tkinter as TK, sources
from webbrowser import open_new_tab as wopen, get as wget
from clipboard import paste as clippaste
from pickle import load as pload
from pickle import dump as pdump
from os import path
from re import match
import threading


class option(TK.Frame):
    def __init__(self, master=None, thetype="IPs"):
        TK.Frame.__init__( self, master, bd="1p", relief="groove", )
        self.top = self.winfo_toplevel()
        self.grid(pady=3, padx=0)
        self.app = TK.Frame(self)
        self.showsettings = TK.IntVar()
        row = 0
        width = 0
        row2 = 0
        if thetype == "IPs":
            row=0
            row2=0
            width=31
        if thetype == "URLs":
            row=6
            row2=6
            width=30
        if thetype == "SPECs":
            row=12
            row2=12
            width=34
        self.app.grid(column=4, row=row, sticky="NW")
        self.thetype=thetype
        self.etext = TK.StringVar()
        self.label = TK.Label(self, text=thetype)
        self.label.grid(column=0, row=row, sticky='NW')
        self.tbox = TK.Entry(self, textvariable=self.etext, width=width)
        self.tbox.grid(column=1, row=row, sticky='NW')
        self.tbox.bind('<Button-3>', self.eText)
        self.tbox.bind("<Return>", self.RetKey)
        self.tbox.bind('<Double-Button-1>', self.eTextclear)
        self.tbox["background"] = "White"
        self.tbox["foreground"] = "Black"
        self.button1=TK.Button(self, text="Spawn", command=lambda: self.fire(self.sources, self.values, self.trigger, self.etext))
        self.button1.grid(column=2, row=row, sticky = 'NW')
        if  (thetype != "SPECs"):
            self.button2=TK.Button(self, text="BL", command=lambda: self.processIP())
            self.button2.grid(column=3, row=row, sticky = 'NW')
        self.cb_settings=TK.Checkbutton(self, variable=self.showsettings, onvalue=1, offvalue=0, command=lambda: self.showSettings(row))
        self.cb_settings.grid(column=0, row=row2, pady=20, sticky = 'NW')
        self.a = sources.sources()
        self.IPdims = self.a.IPdimensions
        self.URLdims = self.a.URLdimensions
        self.SPECdims = self.a.SPECIALdimensions
        self.showSettings(row)
        if (thetype == "IPs"):
            self.sources = self.a.ip.sources
            self.trigger = self.a.ip.trigger
            self.links = self.a.IPLinks
            self.values = [[TK.IntVar() for x in xrange(len(self.sources[:]))]]
            if path.isfile(self.a.IPSettingsfile) and path.getsize(self.a.IPSettingsfile) > 0:
                persist = pload(open(self.a.IPSettingsfile, "rb"))
                for x in xrange(len(persist)):
                    self.values[0][x].set(persist[x])
            for x in xrange(0, len(self.sources[:])):
                self.addCheckBox(self.sources[x][0], x)
            self.ip_chb_define(self.sources, self.values, self.trigger, self.etext, self.links)
            self.read = self.a.IPpath
            self.blread = self.a.IPbl
        if (thetype == "URLs"):
            self.sources = self.a.url.sources
            self.trigger = self.a.url.trigger
            self.links = self.a.URLLinks
            self.values = [[TK.IntVar() for x in xrange(len(self.sources[:]))]]
            if path.isfile(self.a.URLSettingsfile) and path.getsize(self.a.URLSettingsfile) > 0:
                persist = pload(open(self.a.URLSettingsfile, "rb"))
                for x in xrange(len(persist)):
                    self.values[0][x].set(persist[x])
            for x in xrange(0, len(self.sources[:])):
                self.addCheckBox(self.sources[x][0], x)
            self.ip_chb_define(self.sources, self.values, self.trigger, self.etext, self.links)
            self.read = self.a.URLpath
            self.blread = self.a.URLbl
        if (thetype == "SPECs"):
            self.sources = self.a.special.sources
            self.trigger = self.a.special.trigger
            self.links = self.a.SPECIALLinks
            self.values = TK.IntVar()
            for x in xrange(0, len(self.sources[:])):
                self.addRadio(self.sources[x][0], x, x+1)
            self.ip_chb_define(self.sources, self.values, self.trigger, self.etext, self.links)
        self.update()



    def showSettings(self, where):
        if self.showsettings.get() == 0:
            self.app.grid_forget()
            self.update()
            self.top.update()
            set_save=""
            export = []
            if self.thetype == "IPs":
                set_save = self.a.IPdimensions
            if self.thetype == "URLs":
                set_save = self.a.URLdimensions
            if self.thetype == "SPECs":
                set_save = self.a.SPECIALdimensions
            export.append(int(self.winfo_width()))
            export.append(int(self.winfo_height()))
            pdump( export, open(set_save, 'wb'))
        if self.showsettings.get() == 1:
            self.app.grid(column=4, row=where, sticky="NW")
            self.app.update()
            self.update()
            self.top.update()
            set_save = ""
            export = []
            if self.thetype == "IPs":
                set_save = self.a.IPdimensions
            if self.thetype == "URLs":
                set_save = self.a.URLdimensions
            if self.thetype == "SPECs":
                set_save = self.a.SPECIALdimensions
            export.append(int(self.winfo_width()))
            export.append(int(self.winfo_height()))
            pdump(export, open(set_save, 'wb'))
        if (path.getsize(self.a.IPdimensions) > 0) and (path.getsize(self.a.URLdimensions) > 0) and (path.getsize(self.a.SPECIALdimensions) > 0):
            self.update()
            IPs_dim = pload(open(self.a.IPdimensions, "rb"))
            URLs_dim = pload(open(self.a.URLdimensions, "rb"))
            SPECs_dim = pload(open(self.a.SPECIALdimensions, "rb"))
            theIPx = int(IPs_dim[0])
            theIPy = int(IPs_dim[1])
            theURLx = int(URLs_dim[0])
            theURLy = int(URLs_dim[1])
            theSPECx = int(SPECs_dim[0])
            theSPECy = int(SPECs_dim[1])
            newx = 0
            newy = theIPy + theURLy + theSPECy + 15
            if (theIPx > newx):
                newx = theIPx
            if (theURLx > newx):
                newx = theURLx
            if (theSPECx > newx):
                newx = theSPECx
            self.top.geometry(str(newx) + "x" + str(newy))
            self.top.update()

    def RetKey(self, event):
        self.fire(self.sources, self.values, self.trigger, self.etext)



    def eTextclear(self, event):
        self.etext.set("")
        self.tbox["background"] = "White"
        self.tbox["foreground"] = "Black"

    def eText(self, event):
        if self.thetype=="IPs":
            self.etext.set(clippaste())
        if self.thetype=="URLs":
            self.etext.set(self.etext.get() + clippaste())
        if self.thetype=="SPECs":
            self.etext.set(self.etext.get() + clippaste())
            self.tbox["background"] = "White"
            self.tbox["foreground"] = "Black"
        text = self.etext.get()
        if not (self.thetype == "SPECs"):
            blisted = 0
            wlisted = 0
            with open(self.blread, 'r') as read:
                for line in read:
                    if text in line:
                        self.tbox["background"] = "Black"
                        self.tbox["foreground"] = "White"
                        blisted = blisted +1
            with open(self.read, 'r') as read:
                for line in read:
                    if blisted == 0 and text in line:
                        self.tbox["background"] = "Green"
                        self.tbox["foreground"] = "black"
                        wlisted = wlisted +1
            if blisted == 0 and wlisted == 0:
                self.tbox["background"] = "White"
                self.tbox["foreground"] = "Black"

    def processIP(self):
        text = self.etext.get()
        process = 0
        if self.thetype == "IPs":
            if match(r'^((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\.){3}(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])$', text):
                process = process + 1
            else:
                self.tbox["background"] = "Grey"
                self.tbox["foreground"] = "red"
        if self.thetype == "URLs":
            pass
        count = 0
        with open(self.blread, 'r') as read:
            for line in read:
                if text in line:
                    count = count + 1
        if count == 0 :
            with open(self.blread, 'a') as z:
                z.write(str(text+"\n"))
                self.tbox["background"] = "Red"
                self.tbox["foreground"] = "White"
        # else:
        #    self.tbox["background"] = "Grey"
        #    self.tbox["foreground"] = "red"


    def fire(self, sources, values, trigger, etext):
        text = self.etext.get()
        process = 0
        if self.thetype == "IPs":
            if match(r'^((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\.){3}(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])$', etext.get()):
                process += 1
        if self.thetype == "URLs":
            process += 1
        if self.thetype == "SPECs":
            process += 1
        if process >= 1:
            self.tbox["background"] = "White"
            self.tbox["foreground"] = "Black"
            counter = 0
            jobs_list = []
            if not (self.thetype == "SPECs"):
                for x in xrange(len(sources[:])):
                    if values[0][x].get():
                        thread = threading.Thread(target=self.TaskHandler, args=(x, ))
                        thread.setDaemon(True)
                        jobs_list.append(thread)
            else:
                thread = threading.Thread(target=self.TaskHandler, args=(values, ))
                thread.setDaemon(True)
                jobs_list.append(thread)
            for j in jobs_list:
                j.start()
            if not (self.thetype == "SPECs"):
                for line in open(self.read, 'r'):
                    if text in line:
                        counter = counter +1
                    for line in open(self.blread, 'r'):
                        if text in line:
                            counter = counter +1
                if counter == 0:
                    with open(self.read, 'a') as z:
                        z.write(str(etext.get())+"\n")
        else:
            self.tbox["background"] = "Red"
            self.tbox["foreground"] = "white"
        export = []
        set_save = ""
        if self.thetype == "IPs":
            set_save = self.a.IPSettingsfile
            for x in xrange(len(self.a.ip.values)):
                if self.values[0][x].get() == 0:
                    export.append(0)
                else:
                    export.append(1)
            pdump(export, open(set_save, 'wb'))
        if self.thetype == "URLs":
            set_save = self.a.URLSettingsfile
            for x in xrange(len(self.a.url.values)):
                if self.values[0][x].get() == 0:
                    export.append(0)
                else:
                    export.append(1)
            pdump(export, open(set_save, 'wb'))


    def ip_chb_define(self, sources, values, trigger, etext, links):
        for x in xrange(len(sources)):
            method_name = sources[x][0]
            possibles = globals().copy()
            possibles.update(locals())
            check= getattr(links, method_name)
            if not callable(check):
                raise Exception("Method %s not implemented" % method_name)
            self.trigger[x]=getattr(links, method_name)

    def addCheckBox(self, name, counter):
        checkBoxName = name
        c = TK.Checkbutton(self.app, text=checkBoxName, variable=self.values[0][counter], onvalue=1, offvalue=0)
        col = (counter/5)+3
        row = counter%5
        c.grid(column=col, row=row, sticky="Nw")

    def addRadio(self, name, counter, val):
        RadioName = name
        c = TK.Radiobutton(self.app, text=RadioName, variable=self.values, value=val)
        col = (counter/5)+3
        row = counter%5
        c.grid(column=col, row=row, sticky="Nw")

    def TaskHandler(self, index):
        openthis=""
        if not (self.thetype == "SPECs"):
            openthis = self.trigger[index](str(self.etext.get()), self.sources, index)
            if openthis != "":
                wopen(openthis)
        else:
            for x in xrange(0, len(self.sources[:])):
                if self.values.get() == x+1:
                    openthis = self.trigger[x](str(self.etext.get()), self.sources, x)
            if openthis != "":
                wopen(openthis)
