import re

textfile = open('prod_traffic.log', 'r')
filetext = textfile.read()
textfile.close()
match = re.findall(r'<TilingRQ.*</TilingRQ>', filetext)
count = 0
for m in match:
    count = count + 1
    print m
    if count == 1000:
        break
