ipsources = [
                ["Robtex",              "http://www.robtex.com/en/advisory/ip/"],
                ["TCPUtils",            "http://www.tcpiputils.com/browse/ip-address/"],
                ["Whois",               "http://www.whois.com/whois/"],
                ["RepAuthority",        "http://www.reputationauthority.org/lookup.php?ip="],
                ["DNSStuff",            "http://www.dnsstuff.com/tools#ipInformation|type=ipv4&&value="],
                ["MultiRBL",            "http://multirbl.valli.org/lookup/"],
                ["MXToolbox",           "http://mxtoolbox.com/SuperTool.aspx?action=blacklist:"],
                ["IPVoid",              "http://www.ipvoid.com/"],
                ["WebHostingHero",      "https://www.webhostinghero.com/blacklists/"],
                ["Hetrix",              "https://hetrixtools.com/blacklist-check/"],
                ["VirusTotal",          "https://www.virustotal.com/en/ip-address/"],
                ["AntiAbuseProject",    "http://www.anti-abuse.org/multi-rbl-check-results/?host="],
                ["AbuseIPDB",           "https://www.abuseipdb.com/report-history/"],
                ["ProjectHoneypot",     "https://www.projecthoneypot.org/ip_"],
                ["Deepviz",             "https://search.deepviz.com/?s="],
                ["M_webroot_brightcloud", "http://www.brightcloud.com/tools/url-ip-lookup.php"],
                ["M_malwareURL_IP",        "http://malwareurl.com/listing-urls.php"],
                ["Alienvault_IP",   "https://otx.alienvault.com/browse/pulses/?q="],
                ["IBM_XForce_IP",   "https://exchange.xforce.ibmcloud.com/search/"],
                ["ThreatMiner_IP",  "https://www.threatminer.org/host.php?q="]

            ]

urlsources = [
                ["ScanURL",             "http://scanurl.net/?u="],
                ["GoogleSafeBrowsing",  "https://www.google.com/transparencyreport/safebrowsing/diagnostic/#url="],
                ["TrendMicro",          "http://global.sitesafety.trendmicro.com/"],
                ["VirusTotal_URL",      "https://www.virustotal.com/"],
                ["VirusTotal_DOMAIN",   "https://www.virustotal.com/en/domain/"],
                ["URLVoid",             "http://www.urlvoid.com/"],
                ["BlueCoat",            "https://sitereview.bluecoat.com/sitereview.jsp#/?search="],
                ["IsItHacked",          "http://www.isithacked.com/check/"],
                ["NortonSafeWeb",       "https://safeweb.norton.com/report/show?url="],
                ["McAfeeSiteAdvisor",   "http://www.siteadvisor.com/sites/"],
                ["ZScalerZulu",         "http://zulu.zscaler.com/"],
                ["MultiRBL",            "http://multirbl.valli.org/lookup/"],
                ["DomainCheckTool",     "http://www.domainchecktool.net/domain-"],
                ["DNSStuff_man",         "http://www.dnsstuff.com/tools"],
                ["Sucuri",              "https://sitecheck.sucuri.net/results/"],
                ["Deepviz_URL",         "https://search.deepviz.com/?s="],
                ["Deepviz_DOMAIN",      "https://search.deepviz.com/?s="],
                ["M_urlquery",          "http://urlquery.net/index.php"],
                ["M_onlinelinkscan",    "http://onlinelinkscan.com"],
                ["M_webroot_brightcloud",    "http://www.brightcloud.com/tools/url-ip-lookup.php"],
                ["M_malwareURL",        "http://malwareurl.com/listing-urls.php"],
                ["M_UnmaskParasites",   "http://www.unmaskparasites.com/security-report/"],
                ["M_BuiltWith",         "https://builtwith.com"],
                ["Alienvault_DOMAIN",   "https://otx.alienvault.com/browse/pulses/?q="],
                ["IBM_XForce_DOMAIN",   "https://exchange.xforce.ibmcloud.com/search/"],
                ["ThreatMiner_DOMAIN",  "https://www.threatminer.org/domain.php?q="]


]

specialsources = [
                ["WinEventID",          "https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventid="],
                ["VirusTotal_HASH",     "https://www.virustotal.com/"],
                ["CVE_mitre",           "http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-"],
                ["CVE_details",         "https://www.cvedetails.com/cve/CVE-"]

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


class specialsource():
    def __init__(self, src=specialsources):
        self.sources = src
        self.trigger = [0 for x in xrange(len(self.sources))]
        self.values = 0

# LB = [[0 for x in xrange(3)] for x in xrange(len(sources))]
# self.value = [TK.IntVar() for x in range(len(self.sources))]