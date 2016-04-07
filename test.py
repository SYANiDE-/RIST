import mechanize
import urllib
from webbrowser import open as wopen


"""
this = {"sha256": "79e874a35dc04cacf3dad5fe573aac297f8ee1252d034edeea4ceeaf87a7915b"}
print this.values()[0]

"""
theSHA="http://builtwith.com/http://mxtoolbox.com/SuperTool.aspx?action=blacklist197.44.232.1&run=toolpage"
URL = 'http://urlquery.net/'
br = mechanize.Browser()
br.addheaders = [('User-agent', 'Mozilla/5.0')]
br.open(URL)
br.form = list(br.forms())[0]
print(br.form)



"""br['h'] = theSHA
response = br.submit()
this = response.read()
print(this)"""



"""br['query'] = theSHA
    response = br.submit()
    this = response.read()
    if this.find("/en/file/not/found/") != -1:
        print("https://virustotal.com/en/file/not/found/")
    else:
        print("https://virustotal.com/en/file/" + theSHA + "/analysis/")
    #    wopen("https://virustotal.com/en/file/79e874a35dc04cacf3dad5fe573aac297f8ee1252d034edeea4ceeaf87a7915b/analysis/)
"""



#wopen("https://virustotal.com/en/file/" + theSHA + "/analysis/")
"""
this all sort of worked...  the function def works just fine of course.
def shortenToFQDN(URL):
    temp = ""
    if URL.find('://') != -1:
        temp = (URL.split('://')[1:])[0]
        if temp.find('/') != -1:
            temp = (temp.split('/')[0:])[0]
    else:
        if URL.find('/') != -1:
            temp = (URL.split('/')[0:])[0]
    if temp == "":
        return(URL)
    else:
        return(temp)




URL = 'https://www.virustotal.com/'
aURL = 'https://wiki.archlinux.org/index.php/Systemd-networkd'
IP = '196.53.23.10'

br = mechanize.Browser()
br.addheaders = [('User-agent', 'Mozilla/5.0')]
br.open(URL + "en/#search")
br.form = list(br.forms())[2]
br['query'] = shortenToFQDN(aURL)
response = br.submit()
this = response.read()
this = this.split(' href="/en/domain')[1]
this = this.split('"')[0]
print URL + "en/domain" + this
print(this)
# br['url']=URL
# response = br.submit()
# this = response.read()
# this = (this.split('class="loader" id="')[1:])[0].split('">')[0]
# this = (this.split('? Check ')[1:])[0].split(' with multiple blacklists')[0]
# this = (this.split('/submission/show/')[1:])[0].split('" title="View')[0]

"""


"""
source = 'https://www.virustotal.com/'
URL = 'https://www.google.com/?gws_rd=ssl#q=tkinter+make+grab+handle+for+window+corners'
IP = '196.53.23.10'

br = mechanize.Browser()
br.addheaders = [('User-agent', 'Mozilla/5.0')]
br.open(source)
br.form= list(br.forms())[1]
br['url']=URL
response = br.submit()
this = response.read()
# this = (this.split('class="loader" id="')[1:])[0].split('">')[0]
# this = (this.split('? Check ')[1:])[0].split(' with multiple blacklists')[0]
# this = (this.split('/submission/show/')[1:])[0].split('" title="View')[0]
print(this)
"""










"""
br.form= list(br.forms())[0]
br['url'] = URL
response = br.submit()
this = response.read()
# this = (this.split('/public/url_feedbacks?ftype=2&amp;id=')[1:])[0].split('">')[0]
print this
"""






"""
THIS WORKED - TrendMicro
s = requests.Session()
r = s.get(source)
payload = {"url": URL}
r1 = s.post(source + "lib/idn.php", data=payload)
payload = {"urlname": URL, "getinfo": "Check Now"}
r2 = s.post(source + "result.php", data=payload)
this = r2.content
that = this.replace('labeltitleresult"', 'labeltitleresult" style="font-size:20px"')
print that
"""



"""
THIS WORKS
br = mechanize.Browser()
br.open(source)
br.form= list(br.forms())[1]
br['url'] = URL
response = br.submit()
this = response.read()
print (this.split('": "')[1:2])[0].split('", "')[0]
print this
"""







"""
br.form = list(br.forms())[0]
br['ip'] = IP
br.method="POST"
response = br.submit()
url = source + 'scan/' + IP + '/'
webbrowser.open(url)
"""

"""
br = mechanize.Browser(factory=mechanize.RobustFactory())
br.open(source)
br.select_form(nr=0)
print br.form
# options = br.form.possible_items()
"""



"""
br.set_all_readonly(False)
br.set_handle_robots(False)
br.set_handle_refresh(False)
br.addHeaders = [('User-agent', 'Firefox')]
response = br.open(source)
for form in response.forms():
    print form
"""

"""
URL = "https://www.google.com/?gws_rd=ssl#q=google+safe+browsing+url+check&start=10"
test = "https://sitereview.bluecoat.com/sitereview.jsp#/?search="
oURL=urllib.quote(URL)
final = str(test + oURL)
webbrowser.open(final)




form_data = {
    'url': URL,
    'action': '/public/tasks',
}
post_args=urllib.urlencode(form_data)
post = urllib.urlopen(test, post_args)
soup = BeautifulSoup(post, 'html5lib')
soup2 = BeautifulSoup(soup.encode('utf8'))
print str(soup2.encode('utf8'))
"""

"""
source = 'http://www.ipvoid.com/'
IP = '121.52.42.12'

payload = {
    'ip': IP,
    'action': source,
}

session = requests.Session()
t = session.get(source)
u = session.post(source, data=payload, headers=t.headers)
url = source + 'scan/' + IP + '/'
webbrowser.open(url)

"""