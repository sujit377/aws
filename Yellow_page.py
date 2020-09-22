from urllib.request import urlopen
from bs4 import BeautifulSoup as bf
import requests
import mysql.connector as mc
import time

while(True):
    
    emp=[]
    for i in range(1,30):
        url = 'https://www.yellowpages.com/south-brunswick-nj/plumbers?page='+str(i)
        r = urlopen(url)
        soup = bf(r,'lxml')
        d = soup.find(class_ = "search-results organic")
        e =d.findAll(class_="result")
        for j in range(len(e)):
            e1 = []
            e1.append(e[j].find(class_ = "business-name").get_text())
            e1.append(e[j].find(class_ = "phones phone primary").get_text())
            address = ""

            try:
                address = address+str(e[j].find(class_ = "street-address").get_text()+" "+e[j].find(class_ = "locality").get_text())
            except:
                pass;
            try:
                address = address + str(e[j].find(class_ = "adr").get_text())
            except:
                address = "South Brunswick, NJ"
            if(address.strip()==""):
                address = "South Brunswick, NJ"
            e1.append(address)
            emp.append(e1)

    
