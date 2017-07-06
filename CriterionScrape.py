print("Crit Scrape...")

from lxml import html
import requests

#setup vars
peopleUrl = "https://www.criterion.com/people/"
lynchPeopleId = 119692
toniBillPeopleId = 119635

pages = []
for x in range(1, 130000):#after a bit of research, seems like 125597 is one of the upper phantom pages (Romero)
	url = peopleUrl + str(x)
	page = requests.get(url)
	htmlTree = html.fromstring(page.content)
	personName = htmlTree.xpath('//div[@class="person_page"]/div/h1/text()') #look for personName
	items = htmlTree.xpath('//div[@class="explore_column with-director hover "]') #look for grid elements
	#TODO: DJL get more general class selector above, this might only work for directors
	if len(personName) > 0 and len(items) == 0:
		pages.append([x, personName[0]])

for z in pages:
	print(z)

#write page to file
filename = "scrapes.txt"
file = open(filename, 'w')
for y in pages:
	file.write(str(y[1]) + ": " + peopleUrl + str(y[0]) + "\n")
file.close()

print("All Crits Scraped.")