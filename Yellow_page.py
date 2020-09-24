from urllib.request import urlopen
from bs4 import BeautifulSoup as bf
import requests
import mysql.connector as mc
import time
import json

while(True):
    
    emp=[]
######

    for i in range(1,50):

        url = "https://www.justdial.com/us/data/result/getdata?uri=result&city=New-York&catid=ct-1000969324&search=Plumbers&sortBy=&state=NY&page=page-"+str(i)+"&v=9.20"
        try:
            req = requests.get(url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.3'})

        except:
            print("Error in page"+i)
            continue;
        print(req.text)
        data =req.json()

            continue;
        for j in range(len(data['result']['display']['results'])):
            e1 = []
            try:
                e1.append(data['result']['display']['results'][j]['CompanyName'])
            except:
                e1.append("NA")
            try:
                e1.append(data['result']['display']['results'][j]['phonelnk'])
            except:
                e1.append("NA")
            try:
                e1.append(data['result']['display']['results'][j]['address'])
            except:
                e1.append("NA")



            emp.append(e1)

    for i in range(1,42):
        url = "https://www.justdial.com/us/data/result/getdata?uri=result&city=Trenton&catid=ct-1000969324&search=Plumbers&sortBy=&state=NJ&page=page-"+str(i)+"&v=9.20"
        try:
            req = requests.get(url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.3'})

        except:
            print("Error in page"+i)
            continue;
        try:
            data =req.json()
        except:
            print(i)
            continue;
        for j in range(len(data['result']['display']['results'])):
            e1 = []
            try:
                e1.append(data['result']['display']['results'][j]['CompanyName'])
            except:
                e1.append("NA")
            try:
                e1.append((data['result']['display']['results'][j]['phonelnk']).split("|")[0])
            except:
                e1.append("NA")
            try:
                e1.append(data['result']['display']['results'][j]['address'])
            except:
                e1.append("NA")



            emp.append(e1)

 
    t2 = time.time()
    try:
        time.sleep(600-int(t2-t1))
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


    
