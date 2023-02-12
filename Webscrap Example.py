from bs4 import BeautifulSoup
import requests

source  = requests.get('https://shyambv.com/').text

soup = BeautifulSoup(source, 'html.parser')

div = soup.find('div')

#print(div.prettify())

#headline = div.h2.text
#print(headline)

subparagraph = div.find('header', class_='major').p.text
print(subparagraph)

#summary = article.find('div', class_='ml-3').p.text
#print(summary)
