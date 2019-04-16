from urllib.request import urlopen
from bs4 import BeautifulSoup
# import pyexcel
from youtube_dl import YoutubeDL

#1: open connection
url = "https://www.apple.com/itunes/charts/songs/"
conn = urlopen(url)
raw_data = conn.read()
html_content = raw_data.decode("utf8")
# print(html_content)
# with open("itune.html", "wb") as f: 
soup = BeautifulSoup(html_content, "html.parser")
section = soup.find("section", "section chart-grid")
into_section = section.div.ul
li_list = into_section.find_all("li")
list_data = []
for li in li_list:
    a_h4 = li.h4.a
    a_h3 = li.h3.a
    artists = a_h4.string.strip()    
    song_name = a_h3.string.strip()
    info = {
        "Song name" : song_name,
        "Artists" : artists
    }
    list_data.append(info)
#part1: 
pyexcel.save_as(records=list_data, dest_file_name="itune44.xls")
#part2:
options = {
    'default_search': 'ytsearch',
    'max_downloads': 1
}
dl = YoutubeDL(options)
for i in list_data:
    songname = i["Song name"]
    singer = i["Artists"]
    down = songname + singer
    dl.download([down])

