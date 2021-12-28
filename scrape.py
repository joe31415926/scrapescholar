import sys
import requests
from bs4 import BeautifulSoup
import urllib.parse

# define header to access google scholar website
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}

def get_paperinfo(paper_url):

  #download the page
  response=requests.get(url,headers=headers)

  # check successful response
  if response.status_code != 200:
    print('Status code:', response.status_code)
    raise Exception('Failed to fetch web page ')

  #parse using beautiful soup
  paper_doc = BeautifulSoup(response.text,'html.parser')

  return paper_doc

print('search term: ' + sys.argv[1])

url = f"https://scholar.google.com/scholar?q=" + urllib.parse.quote_plus(sys.argv[1]) + "&hl=en&as_sdt=0&as_vis=1&oi=scholart"
print('url: ' + url)

