from random import randint
import urllib, urllib2
from requests import Session, get, post
from os import path
import mechanize

class IPLinks():
    def Robtex(self, IP, sources, index):
        PATH=str(sources[index][1]+ IP.replace(".", "/", 3) + "/")
        return PATH

    def TCPUtils(self, IP, sources, index):
        PATH=str(sources[index][1]+ IP)
        return PATH

    def Whois(self, IP, sources, index):
        PATH=str(sources[index][1]+ IP)
        return PATH

    def RepAuthority(self, IP, sources, index):
        PATH=str(sources[index][1]+ IP + "&Submit.x="+str(randint(0,40)) +"&Submit.y="+ str(randint(0,40)))
        return PATH

    def DNSStuff(self, IP, sources, index):
        PATH=str(sources[index][1]+ IP)
        return PATH

    def MultiRBL(self, IP, sources, index):
        PATH=str(sources[index][1]+ IP +".html")
        return PATH

    def MXToolbox(self, IP, sources, index):
        PATH=str(sources[index][1]+ IP + "&run=toolpage")
        return PATH

    def IPVoid(self, IP, sources, index):
        br = mechanize.Browser()
        br.open(sources[index][1])
        br.form = list(br.forms())[0]
        br['ip'] = IP
        br.method="POST"
        br.submit()
        url = sources[index][1] + 'scan/' + IP + '/'
        return url

    def WebHostingHero(self, IP, sources, index):
        br = mechanize.Browser()
        br.addheaders = [('User-agent', 'Mozilla/5.0')]
        br.open(sources[index][1])
        br.select_form(nr=0)
        br['ip']=IP
        response = br.submit()
        this = response.read()
        return sources[index][1] + '?id=' + (this.split('class="loader" id="')[1:])[0].split('">')[0]

    def Hetrix(self, IP, sources, index):
        PATH = str(sources[index][1] + IP)
        return PATH


class URLLinks():
    def ScanURL(self, URL, sources, index):
        PATH=str(sources[index][1] + urllib.quote(URL) + "&uesb=Check+This+URL#results" )
        return PATH

    def TrendMicro(self, URL, sources, index):
        s = Session()
        r = s.get(sources[index][1])
        payload = {"url": URL}
        r1 = s.post(sources[index][1] + "lib/idn.php", data=payload)
        payload = {"urlname": URL, "getinfo": "Check Now"}
        r2 = s.post(sources[index][1] + "result.php", data=payload)
        outfile= "RISTdat"+path.sep+"transient.html"
        t = file(outfile, 'w')
        this = r2.content
        that = this.replace('labeltitleresult"', 'labeltitleresult" style="font-size:40px; margin:10px 0;"')
        that = that.replace('resulturlholder"', 'resulturlholder" style="font-size:20px; margin:40px 0 10px 0;"')
        t.write(that)
        pathtofile = "file:///"+path.realpath(outfile)
        t.close()
        return pathtofile

    def VirusTotal(self, URL, sources, index):
        br = mechanize.Browser()
        br.open(sources[index][1] + '?#url')
        br.form= list(br.forms())[1]
        br['url'] = URL
        response = br.submit()
        this = response.read()
        return sources[index][1] + 'en/url/' + (this.split('": "')[1:2])[0].split('", "')[0] + '/analysis/'

    def URLVoid(self, URL, sources, index):
        br = mechanize.Browser()
        br.addheaders = [('User-agent', 'Mozilla/5.0')]
        br.open(sources[index][1])
        br.select_form(nr=0)
        br['url']=URL
        response = br.submit()
        this = response.read()
        return sources[index][1] + 'scan/' + (this.split('? Check ')[1:])[0].split(' with multiple blacklists')[0]

    def GoogleSafeBrowsing(self, URL, sources, index):
        PATH=str(sources[index][1]+ URL)
        return PATH

    def BlueCoat(self, URL, sources, index):
        PATH=str(sources[index][1]+ urllib.quote(URL))
        return PATH

    def IsItHacked(self, URL, sources, index):
        PATH=str(sources[index][1] + urllib.quote_plus(URL))
        return PATH

    def NortonSafeWeb(self, URL, sources, index):
        PATH=str(sources[index][1] + urllib.quote(URL))
        return PATH

    def McAfeeSiteAdvisor(self, URL, sources, index):
        PATH=str(sources[index][1] + urllib.quote(URL))
        return PATH

    def ZScalerZulu(self, URL, sources, index):
        br = mechanize.Browser()
        br.set_handle_robots(False)
        br.set_handle_equiv(False)
        br.addheaders = [('User-agent', 'Mozilla/5.0')]
        br.open(sources[index][1])
        br.select_form(nr=0)
        br['submission[submission]']=URL
        response = br.submit()
        this = response.read()
        try:
            this = (this.split('/submission/show/')[1:])[0].split('" title="View')[0]
        except:
            pass
        try:
            this = (this.split('status/')[1:])[0].split("', function")[0]
        except:
            pass
        return sources[index][1] + 'submission/show/' + this