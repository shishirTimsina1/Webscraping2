import re
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

myUrl2 = "https://www.newegg.com/p/pl?Submit=StoreIM&Category=38&Depa=1"
myUrl = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38"
myUrl3 = "https://www.newegg.com/p/pl?d=monitors"
# opening connection, grabbing page
# use the two options above, or try any newegg webpage that supports functions used below.
uClient = uReq(myUrl2)
page_html = uClient.read()
uClient.close()

# html parser
page_soup = soup(page_html, "html.parser")
headerOut = page_soup.h1

# open excel file to hold all graphics card

filename = "GraphicsCards.csv"

# if you want to use existing excel file, replace 'w' with 'a' in line below
# use own file name, and eliminate the headers write funtion.
f = open(filename, "w")

headers = "Brand, Product Name, Price, Shipping, URL \n"
f.write(headers)

# grab each product
containers = page_soup.findAll("div", {"class": "item-container"} )
for container in containers:
    titleContainer = container.findAll("a", {"class": "item-title"})
    productName = titleContainer[0].text
    brand = productName[0:3]
    url = container.find("a")
    url = url.get('href')
    url = str(url)
    priceCont = container.findAll("li", {"class": "price-current"})
    price = priceCont[0].text.strip()
    if price.find('('):
        price = price.split('(',1)[0]

    finalPrice = price.split('.',1)[0]
    shippingCont = container.findAll("li", {"class": "price-ship"})
    shipping = shippingCont[0].text.strip()

    # write out to file

    f.write(brand + "," + productName.replace(',','|') + "," + finalPrice.replace(',', '') + "," + shipping + "," + url +"\n")

f.close()
    #print("\nBrand:"+ brand)
    #print("Product Name:"+ productName)
    #print("Price: " + price)
    #print("Shipping:"+ shipping + "\n")


