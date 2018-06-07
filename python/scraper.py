from bs4 import BeautifulSoup
from urllib import request

# Making the initial list of target links
url="https://www.nytimes.com/series/us-morning-briefing"
html = request.urlopen(url).read()
soup = BeautifulSoup(html, "lxml")
urls = []
for item in soup.find_all('a', class_='story-link')[0:6]:
    urls.append(item.get('href'))
print(urls)

#Scraping and saving the text of target links into corpus
corpus_texts = []
for item in urls:
    html = request.urlopen(item).read()
    soup = BeautifulSoup(html, "lxml")
    for crap in soup.find_all('div', class_='css-18sbwfn'):
        corpus_texts.append(crap.text)
    #print(corpus_texts)

print(corpus_texts)


    # print('=======')
    # print(item.text.replace('\n', ''))
    #print(item.get('href'))



#print (url)

# html = request.urlopen(url).read()

#print("Printout 500 characters from the full HTML")
#print(html[0:500])

# soup = BeautifulSoup(html, 'lxml')

#print("Printout 10 links from the page")
#print(soup.find_all('a')[0:10])

#print("Parse out only the text from the html")
#print(soup.text[0:2000])

#print("Replace linebreaks with space")
#print(soup.text.replace('\n',' ')[0:1000])

#print(type(soup.find_all('a')))
#print(type(soup.find_all('a')).__name__)
#print(type(soup.find_all('a')[0]).__name__)
#print(soup.find_all('a')[0].text)



# print(urls)


#for link in soup.select("td.content a"):
#    print(link.text)

# links_html = soup.select('a', class_='story-link')[0:6]
# urls = []
# for link in links_html:
#     url = link['href'] #.replace('blob/', '')
# #    urls.append("https://raw.githubusercontent.com" + url)
# print(urls)


# import time
# import random
# def download(url, sleep=True):
#     if sleep:
#         time.sleep(random.random() * max_sleep)
#     html = request.urlopen(url).read().decode('utf8', errors='replace')
#     return BeautifulSoup(html)


#convert list to str to save to file with write method
# str1 = ''.join(corpus_texts)
# print(str1)
#
# with open('my_text.txt', 'w') as f:
#      f.write(str1)
