from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)
raw_data = conn.read()
html_content = raw_data.decode("utf8")

with open("scafef.html", "wb") as cf:
    cf.write(raw_data)

#find ROI
soup = BeautifulSoup(html_content, "html.parser")
roi = soup.find("div", style="overflow:hidden;width:100%;border-bottom:solid 1px #cecece;")
inside_div = roi.tr
tr_list = inside_div.find_all('tr')
list_data=[]

#**************************************************************************************************
#i don't have done yet