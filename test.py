
import random
import urllib, urllib2
import requests
from os import path
import webbrowser
from bs4 import BeautifulSoup
import mechanize
import time

"""
this = {"sha256": "79e874a35dc04cacf3dad5fe573aac297f8ee1252d034edeea4ceeaf87a7915b"}
print this.values()[0]

"""
source = 'https://www.webhostinghero.com/blacklists/'
URL = 'http://stackoverflow.com/questions/9249996/mechanize-cannot-read-form-with-submitcontrol-that-is-disabled-and-has-no-value'
IP = '196.53.23.10'

br = mechanize.Browser()
br.addheaders = [('User-agent', 'Mozilla/5.0')]
br.open(source)
br.select_form(nr=0)
br['ip']=IP
response = br.submit()
this = response.read()
this = (this.split('class="loader" id="')[1:])[0].split('">')[0]
# this = (this.split('? Check ')[1:])[0].split(' with multiple blacklists')[0]
# this = (this.split('/submission/show/')[1:])[0].split('" title="View')[0]
print(this)
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