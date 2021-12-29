import sys
import requests
from bs4 import BeautifulSoup
import urllib.parse
import re
from parse import *

print('search term: ' + sys.argv[1])

max_number=9

start_number=0
while start_number < max_number:
    url = f"https://scholar.google.com/scholar?start={start_number}&q=" + urllib.parse.quote_plus(sys.argv[1]) + "&hl=en&as_sdt=0&as_vis=1&oi=scholart"
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
    
    print(url)
    response=requests.get(url,headers=headers)
    
    if response.status_code == 429:
        print('Status code:', response.status_code)
        print(response.headers)
        raise Exception('Too Many Requests response status code indicates the user has sent too many requests in a given amount of time')

    if response.status_code != 200:
        print('Status code:', response.status_code)
        raise Exception('Failed to fetch web page ')
    
    doc = BeautifulSoup(response.text,'html.parser')
    
    for idx, p in enumerate(doc.find_all("div", {"class" : "gs_ab_mdw"})):
      r = parse('Page {} of about {} results', p.text)
      if r is not None and r[1] is not None:
          max_number = int(r[1])
      else:
          r = parse('Page {} of {} results', p.text)
          if r is not None and r[1] is not None:
              max_number = int(r[1])
          else:
              r = parse('About {} results', p.text)
              if r is not None and r[0] is not None:
                  max_number = int(r[0])
              else:
                  r = parse('{} results', p.text)
                  if r is not None and r[0] is not None:
                      max_number = int(r[0])
        
    for idx, paper in enumerate(doc.select('[data-lid]')):
      print(f"paper {start_number+idx}: " + paper.select('h3')[0].get_text())
    
    for idx, cite in enumerate(doc.select('[title=Cite] + a')):
      tmp = re.search(r'\d+', cite) # its handle the None type object error and re use to remove the string " cited by " and return only integer value
      print(f"cite {start_number+idx}: " + cite.text)
      print(f"citere {start_number+idx}: " + int(tmp.group()))
    
    for idx, link in enumerate(doc.find_all('h3',{"class" : "gs_rt"})):
      print(f"link {start_number+idx}: " + link.text)
    
    
    for idx, author in enumerate(doc.find_all("div", {"class": "gs_a"})):
      print(f"author {start_number+idx}: " + author.text)

    start_number = start_number + 10
