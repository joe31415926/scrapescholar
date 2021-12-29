import sys
import requests
from bs4 import BeautifulSoup
import urllib.parse
import re

print('search term: ' + sys.argv[1])

url = f"https://scholar.google.com/scholar?q=" + urllib.parse.quote_plus(sys.argv[1]) + "&hl=en&as_sdt=0&as_vis=1&oi=scholart"
print('url: ' + url)

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}

response=requests.get(url,headers=headers)

if response.status_code != 200:
    print('Status code:', response.status_code)
    raise Exception('Failed to fetch web page ')

doc = BeautifulSoup(response.text,'html.parser')

for idx, paper in enumerate(doc.select('[data-lid]')):
  print(f"paper {idx}: " + paper.select('h3')[0].get_text())

for idx, cite in enumerate(doc.select('[title=Cite] + a')):
  tmp = re.search(r'\d+', cite) # its handle the None type object error and re use to remove the string " cited by " and return only integer value
  print(f"cite {idx}: " + cite.text)
  print(f"citere {idx}: " + int(tmp.group()))

for idx, link in enumerate(doc.find_all('h3',{"class" : "gs_rt"})):
  print(f"link {idx}: " + link.text)


for idx, author in enumerate(doc.find_all("div", {"class": "gs_a"})):
  print(f"author {idx}: " + author.text)

