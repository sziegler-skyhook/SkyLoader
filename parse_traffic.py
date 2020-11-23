import re

textfile = open('prod_traffic.log', 'r')
filetext = textfile.read()
textfile.close()
match = re.findall(r'<RGeoRQ.*</RgeoRQ>', filetext)
count = 0
for m in match:
    count = count + 1
    print m
    print "---"
print count
