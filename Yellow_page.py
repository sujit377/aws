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
    t2 = time.time()
    try:
        time.sleep(3600-int(t2-t1))
    except:
        pass
    print(time.asctime(time.localtime(time.time())))
    t1 = time.time()
    
    t = mc.connect(host = "localhost",
              user="root",
              password= "jaf123",#jaf123
              database="scraped_data")#scraped_data
    cursor = t.cursor()
    cursor.execute("truncate table vendor_data") #vendor_data
    for i in emp:
        sql = "INSERT INTO vendor_data (name,NUMBER,ADDRESS) VALUES (%s,%s,%s)" #vendor_data
        val = [i[0],i[1],i[2]]
        cursor.execute(sql,val)
    t.commit()
    t.close()
    
