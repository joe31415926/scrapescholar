from bs4 import BeautifulSoup
import re

local_web_page_file = open("index.html", "r")
page_html = local_web_page_file.read()
local_web_page_file.close()

doc = BeautifulSoup(page_html, 'html.parser')
print(doc.prettify())

for idx, paper in enumerate(doc.select('[data-lid]')):
    print('paper: ' + paper.select('h3')[0].get_text())

for idx, cite in enumerate(doc.select('[title=Cite] + a')):
    tmp = re.search(r'\d+', cite) # its handle the None type object error and re use to remove the string " cited by " and return only integer value
    print("cite: " + cite.text)
    print("citere: " + int(tmp.group()))

for idx, link in enumerate(doc.find_all('h3',{"class" : "gs_rt"})):
    print(f"link: " + link.text)

for idx, author in enumerate(doc.find_all("div", {"class": "gs_a"})):
    print(f"author: " + author.text)
