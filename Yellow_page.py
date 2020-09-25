from urllib.request import urlopen
from bs4 import BeautifulSoup as bf
import requests
import mysql.connector as mc
import time
import json

while(True):
    
    emp=[]
    for i in range(1,28):
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
            e1.append(url)
            e1.append("www.yellowpages.com")
            emp.append(e1)
    for i in range(1,15):
        url = "https://www.bbb.org/search?find_country=USA&find_entity=10113-000&find_id=2990_8000-1900&find_latlng=40.727204%2C-74.058756&find_loc=Jersey%20City%2C%20NJ&find_text=Plumber&find_type=Category&page="+str(i)+"&sort=Relevance&touched=7"
        try:
            r = urlopen(url)
            soup = bf(r,'lxml')
        except:
            print("Error in page"+i)
            continue;
        e =soup.findAll(class_ = "MuiPaper-root MuiCard-root styles__ResultItem-sc-7wrkzl-0 yheMW result-item MuiPaper-elevation1 MuiPaper-rounded")
        for j in range(len(e)):
            e1 = []
            try:
                e1.append(e[j].find(class_="MuiTypography-root Name-sc-1srnbh5-0 lfDNIb result-item__name MuiTypography-h4").find('a').get_text())
            except:
                e1.append("NA")
            try:
                e1.append(e[j].find(class_ = "MuiTypography-root Phone-sc-418jiw-0 blBqyQ result-item__phone MuiTypography-body1").get_text())
            except:
                e1.append("NA")
            try:
                e1.append(e[j].find(class_ = "MuiTypography-root Address-ee3ajc-0 fpMHTB result-item__address MuiTypography-body1").get_text())
            except:
                e1.append("NA")
            e1.append(url)
            e1.append("www.bbb.org")
            emp.append(e1)


    for i in range(1,15):
        url = "https://www.bbb.org/search?find_country=USA&find_entity=10113-000&find_id=2990_8000-1900&find_latlng=40.762801%2C-73.977818&find_loc=New%20York%2C%20NY&find_text=Plumber&find_type=Category&page="+str(i)
        try:
            r = urlopen(url)
            soup = bf(r,'lxml')
        except:
            print("Error in page"+i)
            continue;
        e =soup.findAll(class_ = "MuiPaper-root MuiCard-root styles__ResultItem-sc-7wrkzl-0 yheMW result-item MuiPaper-elevation1 MuiPaper-rounded")
        for j in range(len(e)):
            e1 = []
            try:
                e1.append(e[j].find(class_="MuiTypography-root Name-sc-1srnbh5-0 lfDNIb result-item__name MuiTypography-h4").find('a').get_text())
            except:
                e1.append("NA")
            try:
                e1.append(e[j].find(class_ = "MuiTypography-root Phone-sc-418jiw-0 blBqyQ result-item__phone MuiTypography-body1").get_text())
            except:
                e1.append("NA")
            try:
                e1.append(e[j].find(class_ = "MuiTypography-root Address-ee3ajc-0 fpMHTB result-item__address MuiTypography-body1").get_text())
            except:
                e1.append("NA")
            e1.append(url)
            e1.append("www.bbb.org")
            emp.append(e1)

 
    t2 = time.time()
    try:
        time.sleep(3600-int(t2-t1))
    except:
        pass
    print(time.asctime(time.localtime(time.time())))
    t1 = time.time()

    t = mc.connect(host = "localhost",
    cursor = t.cursor()
    cursor.execute("truncate table vendor_data") #vendor_data
    for i in emp:
        sql = "INSERT INTO vendor_data (name,NUMBER,ADDRESS,Data_Address,Data_Site) VALUES (%s,%s,%s,%s,%s)" #vendor_data
        val = [i[0],i[1],i[2],i[3],i[4]]
        cursor.execute(sql,val)
    t.commit()
    t.close()


    
