from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
#1: open connection
url = "https://dantri.com.vn"
conn = urlopen(url)
raw_data = conn.read()
html_content = raw_data.decode("utf8")

with open("dantri.html", "wb") as f: 
    #wb: write binary
    f.write(raw_data)
#2: find ROI
# ROI: region of interest
soup = BeautifulSoup(html_content, "html.parser")
ul = soup.find("ul", "ul1 ulnew")

#3: extract ROI
li_list = ul.find_all("li")

list_data =[]

for li in li_list: 
    h4 = li.h4
    a = h4.a
    title = a.string.strip()
    link = url + a["href"]
    dic_data = OrderedDict({
        "Title": title,
        "Link": link
    })
    list_data.append(dic_data)
    


pyexcel.save_as(records=list_data, dest_file_name="intro6.xls")