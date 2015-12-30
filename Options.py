import Tkinter as TK, sources
from webbrowser import open as wopen
from clipboard import paste as clippaste
from pickle import load as pload
from pickle import dump as pdump
from os import path
from re import match
import thread
import threading


class option(TK.Frame):
    def __init__(self, master=None, thetype="IPs"):
        TK.Frame.__init__(self, master, bd="1p", relief="groove", )
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
        self.app.grid(column=4, row=row, sticky="NW")
        self.thetype=thetype
        self.etext = TK.StringVar()
        self.label = TK.Label(self, text=thetype)
        self.label.grid(column=0, row=row, sticky='NW')
        self.tbox = TK.Entry(self, textvariable=self.etext, width=width)
        self.tbox.grid(column=1, row=row, sticky='NW')
        self.tbox.bind('<Button-3>', self.eText)
        self.tbox.bind('<Double-Button-1>', self.eTextclear)
        self.tbox["background"] = "White"
        self.tbox["foreground"] = "Black"
        self.button1=TK.Button(self, text="Spawn", command=lambda: self.fire(self.sources, self.values, self.trigger, self.etext))
        self.button1.grid(column=2, row=row, sticky = 'NW')
        self.button2=TK.Button(self, text="BL", command=lambda: self.processIP())
        self.button2.grid(column=3, row=row, sticky = 'NW')
        self.cb_settings=TK.Checkbutton(self, variable=self.showsettings, onvalue=1, offvalue=0, command=lambda: self.showSettings(row))
        self.cb_settings.grid(column=0, row=row2, pady=20, sticky = 'NW')
        self.showSettings(row)
        self.a = sources.sources()
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

    def showSettings(self, where):
        if self.showsettings.get() == 0:
            self.app.grid_forget()
        if self.showsettings.get() == 1:
            self.app.grid(column=4, row=where, sticky="NW")

    def eTextclear(self, event):
        self.etext.set("")
        self.tbox["background"] = "White"
        self.tbox["foreground"] = "Black"

    def eText(self, event):
        if self.thetype=="IPs":
            self.etext.set(clippaste())
        if self.thetype=="URLs":
            self.etext.set(self.etext.get() + clippaste())
        text = self.etext.get()
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
                    self.tbox["foreground"] = "White"
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
        if process >= 1:
            self.tbox["background"] = "White"
            self.tbox["foreground"] = "Black"
            counter = 0
            thread_list = []
            for x in xrange(len(sources[:])):
                if values[0][x].get():
                    openthis = trigger[x](str(etext.get()), sources, x)
                    if openthis != "":
                        # t = threading.Thread(target=wopen, args=(openthis, ))
                        # thread_list.append(t)
                        thread.start_new_thread(wopen, (openthis, ))
            #for thread in thread_list:
            #   thread.start()
            for line in open(self.read, 'r'):
                if text in line:
                    counter = counter +1
                for line2 in open(self.blread, 'r'):
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
        if self.thetype == "URLs":
            set_save = self.a.URLSettingsfile
            for x in xrange(len(self.a.url.values)):
                if self.values[0][x].get() == 0:
                    export.append(0)
                else:
                    export.append(1)
        pdump( export, open(set_save, 'wb'))


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
        col = 3 if counter <= 5-1 else 4 if counter > 5-1 else 5 if counter > 10-1 else 6 if counter > 15-1 else 7 \
            if counter > 20-1 else 8 if counter > 25-1 else 9
        row = counter%5
        c.grid(column=col, row=row, sticky="Nw")