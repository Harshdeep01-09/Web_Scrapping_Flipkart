import pandas as pd
from bs4 import BeautifulSoup
import requests




Product_name = []
Prices = []
Description = []
Reviews = []
#for i in range(2,10):

#print(r)


    
for i in range(1,4):    
    url = "https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+ str(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"lxml")
    
    box = soup.find("div", class_ = "_1YokD2 _3Mn1Gg")

    names =  box.find_all("div",class_ ="_4rR01T")   
    for i in names :
        name = i.text 
        Product_name.append(name)
        
    prices = box.find_all("div", class_ = "_30jeq3 _1_WHN1")
    for i in prices :
        price = i.text 
        Prices.append(price)
        
    desc = box.find_all("div", class_ = "fMghEO")
    for i in desc: 
        des = i.text
        Description.append(des)

    rev = box.find_all("div", class_ = "_3LWZlK")
    for i in rev: 
        revs = i.text
        Reviews.append(revs)
    
    #print (soup)

    #while True:
    #np = soup.find("a", class_="_1LKTO3").get("href")
    #cnp = "https://flipkart.com" + np
    #print(cnp)

    #url = cnp
    #r=requests.get(url)
    #soup = BeautifulSoup(r.text,"lxml")



df = pd.DataFrame({"Product Name":Product_name, "Prices": Prices, "Description": Description, "Reviews": Reviews})
print(df)



df.to_excel("WEB SCRAPPED DATA OF FLIPKART")