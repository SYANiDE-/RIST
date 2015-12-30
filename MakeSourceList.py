import pickle

ipsources = [
                ["Robtex",              "http://www.robtex.com/en/advisory/ip/"],
                ["TCPUtils",            "http://www.tcpiputils.com/browse/ip-address/"],
                ["Whois",               "http://www.whois.com/whois/"],
                ["RepAuthority",        "http://www.reputationauthority.org/lookup.php?ip="],
                ["DNSStuff",            "http://www.dnsstuff.com/tools#ipInformation|type=ipv4&&value="],
                ["MultiRBL",            "http://multirbl.valli.org/lookup/"],
                ["MXToolbox",           "http://mxtoolbox.com/SuperTool.aspx?action=blacklist%3"],
                ["IPVoid",              "http://www.ipvoid.com/"],
                ["WebHostingHero",      "https://www.webhostinghero.com/blacklists/"],
                ["Hetrix",              "https://hetrixtools.com/blacklist-check/"]
            ]

urlsources = [
                ["ScanURL",             "http://scanurl.net/?u="],
                ["GoogleSafeBrowsing",  "https://www.google.com/transparencyreport/safebrowsing/diagnostic/#url="],
                ["TrendMicro",          "http://global.sitesafety.trendmicro.com/"],
                ["VirusTotal",          "https://www.virustotal.com/"],
                ["URLVoid",             "http://www.urlvoid.com/"],
                ["BlueCoat",            "https://sitereview.bluecoat.com/sitereview.jsp#/?search="],
                ["IsItHacked",          "http://www.isithacked.com/check/"],
                ["NortonSafeWeb",       "https://safeweb.norton.com/report/show?url="],
                ["McAfeeSiteAdvisor",   "http://www.siteadvisor.com/sites/"],
                ["ZScalerZulu",         "http://zulu.zscaler.com/"]
             ]

class ipsource():
    def __init__(self, src=ipsources):

        self.sources = src
        self.trigger = [0 for x in xrange(len(self.sources))]
        self.values = [0 for x in xrange(len(self.sources))]


class urlsource():
    def __init__(self, src=urlsources):
        self.sources = src
        self.trigger = [0 for x in xrange(len(self.sources))]
        self.values = [0 for x in xrange(len(self.sources))]


# LB = [[0 for x in xrange(3)] for x in xrange(len(sources))]
# self.value = [TK.IntVar() for x in range(len(self.sources))]