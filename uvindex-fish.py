# UV index
 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
 

url = 'https://tides4fishing.com/as/thailand/bangkok/forecast/uv-exposure-level'
webopen = urlopen(url)
pagehtml = webopen.read() 
webopen.close()


data = BeautifulSoup(pagehtml,'html.parser')
 
UV = data.find_all('div',{'class':'f_uv'})
Day = data.find_all('div',{'class':'f_info_dia'})

All = [(Day[0].text,UV[0].text),
		(Day[1].text,UV[1].text),
		(Day[2].text,UV[2].text),
		(Day[3].text,UV[3].text),
		(Day[4].text,UV[4].text),
		(Day[5].text,UV[5].text),
		(Day[6].text,UV[6].text)]



print(All)

 
with open('UVindexresult.txt','w',encoding='utf-8') as file:
    #file.write(All)
 	write = csv.writer(file)
 	write.writerow(All)

 