from geotext import GeoText
import sys
import re


file = str(sys.argv[1])
f = open(file, 'r')
text = f.read()


# Extract all text in parentheses
p = re.compile(r'[(](.*?)[)]')
result = re.findall(p,text)


for sentence in result:
    # match items base on city and country
    if GeoText(sentence).cities or GeoText(sentence).countries:
        print(sentence)
 

f.close()




