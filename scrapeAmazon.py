import requests
from bs4 import BeautifulSoup as bs
import urllib
import time

url="https://www.amazon.in/s/ref=nb_sb_noss?url=node%3D1388921031&field-keywords=earphones"
page=requests.get(url)

soup=bs(page.text,"html.parser")

res=soup.findAll("a",{"class":"s-access-detail-page"})
print("List of all the earphones under the catagory of lightning deals:\n")
count=0
i=1

for each_tag in res:
	eachurl=(each_tag.prettify().__str__().split('\n')[0].split('"')[3])
	print str(i),'.',each_tag.text
	i+=1
	print(eachurl)
	eachpage=requests.get(eachurl)
	#print(eachpage)
	# print(eachpage.text[:10],eachpage)
	# print("abrakadabra")
	gg=eachpage.text.find("dealType")
	# print(gg)
	if(gg!=-1):
		eachsoup=bs(eachpage.text,"html.parser")
		eachres=eachsoup.findAll("span",{"id":"productTitle"}).__str__().split('\n')[9].strip(' ')
		# print(eachres)
		eachresprice=eachsoup.findAll("span",{"id":"priceblock_dealprice"}).__str__().split("</span>")[1].strip(' ')

		print(count+1,") ",eachres)
		print("\t=> ",eachresprice)
		count+=1
		# if(count==5):
		# 	break

# print(count)
