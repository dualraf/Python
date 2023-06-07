import urllib.request , urllib.parse , urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
cou = input('Enter count: ')
position = input('Enter position: ')
html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')

counts = int(cou)
tags = soup('a')

print(url)
print(tags[int(position)- 1].get('href', None))
count = 1

while count < counts:
	url = tags[int(position)- 1].get('href', None)
	html = urllib.request.urlopen(url, context = ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')
	print(tags[int(position)- 1].get('href', None))
	count = count + 1
