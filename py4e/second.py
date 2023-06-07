import re

name = input('Enter file name: ')
handle = open(name)
sum = 0
numbers = list()

for line in handle:
    line = line.rstrip()
    y = re.findall('[0-9]+',line)
    if len(y) < 1: continue
    for i in y:
        x = int(i)
        numbers.append(x)
        sum += x
print(sum)
