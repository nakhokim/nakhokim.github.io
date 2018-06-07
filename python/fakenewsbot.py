from bs4 import BeautifulSoup
from urllib import request

# Making the initial list of target links
url="https://www.nytimes.com/series/us-morning-briefing"
html = request.urlopen(url).read()
soup = BeautifulSoup(html, "lxml")
urls = []
for item in soup.find_all('a', class_='story-link')[0:6]:
    urls.append(item.get('href'))
# print(urls)

#Scraping and saving the text of target links into corpus
corpus_texts = []
for item in urls:
    html = request.urlopen(item).read()
    soup = BeautifulSoup(html, "lxml")
    for crap in soup.find_all('div', class_='css-18sbwfn'):
        corpus_texts.append(crap.text)
# print(corpus_texts)

#convert list to str to save to file with write method
str1 = ''.join(corpus_texts)
with open('junk.txt', 'w') as f:
    f.write(str1)


import random

person1 = input("Who is in the news? ")
person1 = str(person1)
person2 = input("Who else is in it? ")
person2 = str(person2)
length = input("How many words? ")
length = int(length)

def title():
    print ("[Exclusive] " + person1 + " is feuding with " + person2 + "!" + "\n")


def open_file_and_get_text(filename):
    # open the file, as a read-only.
    with open(filename, 'r') as our_file:
        # takes the file and reads it.
        text = our_file.read()
    return text
# the text from which to pull the junk news.
filename = "junk.txt"
text = open_file_and_get_text(filename)

# next step: tokenize words so it starts and ends with words.
def main_body():
    # text_word=text.split()    :: want to make it in word
    rand_seg = random.randint(1,5000)
    text2 = text.split(" ")
    text3 = text2[rand_seg:(rand_seg+length)]
    text4 = ' '.join(text3)
    print (text4)

# The outputs
title()
main_body()

print("\n" + "[What just happened: this code has scraped past week's worth of NYT morning briefings, and pulled out random bits from it. Makes things look so much more like authentic news.]")
