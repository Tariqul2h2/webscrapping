from urllib import request
from bs4 import BeautifulSoup
from googlesearch import search

#the url you wanted to get data
url = "http://www.ugc-universities.gov.bd/private-universities"

soup = BeautifulSoup(request.urlopen(url).read(), features = "lxml")
SAVE_SEARCH = []
#my required data in span 
for span in soup.findAll('table')[0].findAll('span'):
    #converting tag into string
    SAVE_SEARCH.append(str(span))
UNIVERSITY_LIST = []
for i in SAVE_SEARCH:
    if 'www.' not in i:
        UNIVERSITY_LIST.append(i.split('>')[1])
print('UGC Registered University\'s of Bangladesh')

with open(f"university_list.txt", "w") as f:
    for i in UNIVERSITY_LIST:
        name = i.split('<')[0]
        f.write(f'{name}\n')