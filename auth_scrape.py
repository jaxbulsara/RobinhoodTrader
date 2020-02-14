from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import re

req = Request("https://robinhood.com/login", headers={'User-Agent': 'Mozilla Chrome Safari'})
webpage = urlopen(req).read()
urlopen(req).close()

page_soup = soup(webpage, "lxml")
container = str(page_soup.findAll("script"))

device_token = re.search('clientId: "(.+?)"', container).group(1)
print(device_token)