# scrapescholar

This github repository contains python code which will scrape research articles from google scholar. Ultimately, you'll need to be able to run this program using python and provide a search term. Since the search term may include spaces and double quotes, you'll need to be able to quote the entire search term on the command line to pass it as a single argument as input into the program. On a Macintosh (or any unix based computer) you can use single quotes.

For instance, if your search term is **indigenous "impact measurement" source:Accounting**
```
joeruff@Josephs-MacBook-Pro scrapescholar % python3 scrape.py 'indigenous "impact measurement" source:Accounting'
```

Unfortunately, python version 2 and python version 3 are quite different and both versions are still widely in use. Thus, it is important that you always know which version you're using and which version your python software is expecting to be run with.

This code will be written to be run with python 3. Ensure that you're using python 3 (It probably doesn't matter **which** python 3).

```
joeruff@Josephs-MacBook-Pro scrapescholar % python --version
Python 2.7.16
joeruff@Josephs-MacBook-Pro scrapescholar % python3 --version
Python 3.8.9
joeruff@Josephs-MacBook-Pro scrapescholar % 
```

In addition to installing python itself, you'll need to then use python to install various modules that we'll be using:

```
joeruff@Josephs-MacBook-Pro scrapescholar % python3 scrape.py 'indigenous "impact measurement" source:Accounting'
Traceback (most recent call last):
  File "scrape.py", line 2, in <module>
    import requests
ModuleNotFoundError: No module named 'requests'
joeruff@Josephs-MacBook-Pro scrapescholar % python3 -m pip install requests
Defaulting to user installation because normal site-packages is not writeable
Collecting requests
  Downloading requests-2.26.0-py2.py3-none-any.whl (62 kB)
     |████████████████████████████████| 62 kB 220 kB/s 
Collecting urllib3<1.27,>=1.21.1
  Downloading urllib3-1.26.7-py2.py3-none-any.whl (138 kB)
     |████████████████████████████████| 138 kB 1.5 MB/s 
Collecting certifi>=2017.4.17
  Downloading certifi-2021.10.8-py2.py3-none-any.whl (149 kB)
     |████████████████████████████████| 149 kB 2.5 MB/s 
Collecting charset-normalizer~=2.0.0; python_version >= "3"
  Downloading charset_normalizer-2.0.9-py3-none-any.whl (39 kB)
Collecting idna<4,>=2.5; python_version >= "3"
  Downloading idna-3.3-py3-none-any.whl (61 kB)
     |████████████████████████████████| 61 kB 2.3 MB/s 
Installing collected packages: urllib3, certifi, charset-normalizer, idna, requests
  WARNING: The script normalizer is installed in '/Users/joeruff/Library/Python/3.8/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed certifi-2021.10.8 charset-normalizer-2.0.9 idna-3.3 requests-2.26.0 urllib3-1.26.7
WARNING: You are using pip version 20.2.3; however, version 21.3.1 is available.
You should consider upgrading via the '/Library/Developer/CommandLineTools/usr/bin/python3 -m pip install --upgrade pip' command.
joeruff@Josephs-MacBook-Pro scrapescholar % python3 scrape.py 'indigenous "impact measurement" source:Accounting'
Traceback (most recent call last):
  File "scrape.py", line 3, in <module>
    from bs4 import BeautifulSoup
ModuleNotFoundError: No module named 'bs4'
joeruff@Josephs-MacBook-Pro scrapescholar % python3 -m pip install bs4     
Defaulting to user installation because normal site-packages is not writeable
Collecting bs4
  Downloading bs4-0.0.1.tar.gz (1.1 kB)
Collecting beautifulsoup4
  Downloading beautifulsoup4-4.10.0-py3-none-any.whl (97 kB)
     |████████████████████████████████| 97 kB 1.2 MB/s 
Collecting soupsieve>1.2
  Downloading soupsieve-2.3.1-py3-none-any.whl (37 kB)
Building wheels for collected packages: bs4
  Building wheel for bs4 (setup.py) ... done
  Created wheel for bs4: filename=bs4-0.0.1-py3-none-any.whl size=1272 sha256=ca42eebef892db48321b09c86bd092f0f2dfa54c3bede64d0d14c78067476063
  Stored in directory: /Users/joeruff/Library/Caches/pip/wheels/75/78/21/68b124549c9bdc94f822c02fb9aa3578a669843f9767776bca
Successfully built bs4
Installing collected packages: soupsieve, beautifulsoup4, bs4
Successfully installed beautifulsoup4-4.10.0 bs4-0.0.1 soupsieve-2.3.1
WARNING: You are using pip version 20.2.3; however, version 21.3.1 is available.
You should consider upgrading via the '/Library/Developer/CommandLineTools/usr/bin/python3 -m pip install --upgrade pip' command.
joeruff@Josephs-MacBook-Pro scrapescholar % python3 scrape.py 'indigenous "impact measurement" source:Accounting'
search term: indigenous "impact measurement" source:Accounting
url: https://scholar.google.com/scholar?q=indigenous+%22impact+measurement%22+source%3AAccounting&hl=en&as_sdt=0&as_vis=1&oi=scholart
```

This approach relies on the Beautiful Soup module parsing (scraping) the webpage properly:
[https://www.crummy.com/software/BeautifulSoup/bs4/doc/]


Because Google sometimes bocks us when we do a lot of testing, just use this test harness while developing new code. The test harness just reads a webpage which has been saved locally on the hard disk: `index.html`

```
joeruff@Josephs-MacBook-Pro scrapescholar % python3 test.py                                            
paper: Critical success factors in managing sustainable indigenous businesses in Australia
paper: Social impact measurement: Classification of methods
paper: Corporate environmental impact: measurement, data and information
paper: Using accountability to shape the common good
paper: Towards an accounting of socio-environmental conflicts in South America
paper: Full Cost Accounting—A Stepping Stone for Corporate Sustainability Reporting
paper: Sustainability and accountability of social enterprise
paper: Disclosures of social value creation: A case study of three global social enterprises
paper: Accountability and the privateness of private ancillary funds
paper: Literature Discourse
link: Critical success factors in managing sustainable indigenous businesses in Australia
link: Social impact measurement: Classification of methods
link: Corporate environmental impact: measurement, data and information
link: Using accountability to shape the common good
link: Towards an accounting of socio-environmental conflicts in South America
link: Full Cost Accounting—A Stepping Stone for Corporate Sustainability Reporting
link: Sustainability and accountability of social enterprise
link: Disclosures of social value creation: A case study of three global social enterprises
link: Accountability and the privateness of private ancillary funds
link: Literature Discourse
author: K Bodle, M Brimble, S Weaven, L Frazer… - Pacific Accounting …, 2018 - emerald.com
author: K Maas, K Liket - … management accounting and supply chain …, 2011 - Springer
author: D Freiberg, DG Park, G Serafeim… - … School Accounting & …, 2021 - papers.ssrn.com
author: C Pesci, E Costa, M Andreaus - Critical Perspectives on Accounting, 2020 - Elsevier
author: M Gómez-Villegas - … Handbook of Environmental Accounting, 2021 - taylorfrancis.com
author: K Chatterjee - Studies in Accounting and Finance: Contemporary …, 2010 - books.google.com
author: NH Ab Samad, R Arshad, SH Asat… - … & Accounting Review …, 2017 - ir.uitm.edu.my
author: MA Islam - … Asia Pacific Interdisciplinary Research in Accounting …, 2013 - papers.ssrn.com
author: A Williamson, B Luke, C Furneaux - … Research in Accounting  …, 2016 - eprints.qut.edu.au
author: F Oladele, TG Oyewole - … and Cloud Technology Use in Accounting …, 2020 - emerald.com
joeruff@Josephs-MacBook-Pro scrapescholar % 
```