import json
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')

info = json.loads(data.decode())
lst = info['comments']
print('Count:', len(lst))
sum = 0
for item in lst:
    sum += item['count']

print('Sum:',sum)
