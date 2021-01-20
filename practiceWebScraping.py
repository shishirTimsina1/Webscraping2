import re
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

myUrl2 = "https://www.newegg.com/p/pl?N=100007709%2050001315"
myUrl = "https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=7709"
myUrl3 = "https://www.newegg.com/p/pl?d=monitors"
# opening connection, grabbing page
# use the two options above, or try any newegg webpage that supports functions used below.
uClient = uReq(myUrl)
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

headers = "Brand, Product Name, Price, Shipping \n"
f.write(headers)

# grab each product
containers = page_soup.findAll("div", {"class": "item-container"} )
for container in containers:
    brand = container.div.div.a.img["title"]
    titleContainer = container.findAll("a", {"class": "item-title"})
    productName = titleContainer[0].text
    priceCont = container.findAll("li", {"class": "price-current"})
    price = priceCont[0].text.strip()
    if price.find('('):
        price = price.split('(',1)[0]

    finalPrice = price.split('.',1)[0]
    shippingCont = container.findAll("li", {"class": "price-ship"})
    shipping = shippingCont[0].text.strip()

    # write out to file

    f.write(brand + "," + productName.replace(',','|') + "," + finalPrice.replace(',', '') + "," + shipping + "\n")

f.close()
    #print("\nBrand:"+ brand)
    #print("Product Name:"+ productName)
    #print("Price: " + price)
    #print("Shipping:"+ shipping + "\n")



