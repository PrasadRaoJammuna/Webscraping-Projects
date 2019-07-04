import requests
from bs4 import BeautifulSoup

wiki_link = "http://worldpopulationreview.com/continents/capitals-of-asia/"

url = requests.get(wiki_link).text
#print(url)

soup = BeautifulSoup(url,'html')
print(soup.prettify()) #for getting Tree-structure

print(soup.title)
print(soup.title.string) #for getting only text

#findig hyperlinks

print(soup.a) #return a single link

print(soup.find_all('a'))

links = soup.find_all('a')
count = 0
for link in links:
    count +=1
    print(link)
print('Total No.of Links: ',count)


print(soup.find('table',class_='table'))

tables = soup.find('table',class_='table')

tab_links = tables.findAll('a')
print(tab_links)

countries = []
for link in tab_links:
    countries.append(link.get('href'))
print(countries)
print(len(countries))



import pandas as pd

df = pd.DataFrame()
df['Links']=countries

print(df)
