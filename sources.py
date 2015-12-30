from os import path, makedirs
import MakeSourceList
from source_methods import *

class sources():
    def __init__(self,
                IPsrc = "seenip.lst",
                URLsrc = "seenurl.lst",
                IPbl = "blacklist_ip.lst",
                URLbl = "blacklist_url.lst",
                SettingsIP = "IP.settings",
                SettingsURL = "URL.settings",
                dataDir = "RISTdat"):
        self.IPpath = str(dataDir + path.sep + IPsrc)
        self.URLpath = str(dataDir + path.sep + URLsrc)
        self.IPbl = str(dataDir + path.sep + IPbl)
        self.URLbl = str(dataDir + path.sep + URLbl)
        self.IPSettingsfile = str(dataDir + path.sep + SettingsIP)
        self.URLSettingsfile = str(dataDir + path.sep + SettingsURL)
        if not path.exists(dataDir):
            makedirs(dataDir)
        def checkpath(somepath):
            if not path.exists(somepath):
                z = open(somepath, 'w')
                z.close()
        checkpath(self.URLpath)
        checkpath(self.IPpath)
        checkpath(self.IPbl)
        checkpath(self.URLbl)
        checkpath(self.IPSettingsfile)
        checkpath(self.URLSettingsfile)

        self.ip = MakeSourceList.ipsource()
        self.IPLinks = IPLinks()
        self.url = MakeSourceList.urlsource()
        self.URLLinks = URLLinks()
        # TODO: self.url = MakeSourceList.urlsource()
