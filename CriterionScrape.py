print("Crit Scrape...")
url = 'https://www.criterion.com/people/119641'
#outputfile = open('c:\\users\\dlawrence\\desktop\\scrapes.txt', 'w') #create scrape outputfile

import urllib.request
phantompage = urllib.request.urlopen(url).read() #scrape mainpage
print(phantompage) 
 
# from lxml import html
# import requests
# page = requests.get(url)
# htmlTree = html.fromstring(page.content)
# print(htmlTree)

#outputFile.close()
print("All Crits Scraped.")

C:\Users\dlawrence\AppData\Local\Programs\Python