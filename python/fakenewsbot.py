import random

person1 = input("Who is in the news? ")
person1 = str(person1)
person2 = input("Who else is in it? ")
person2 = str(person2)
length = input("How long? ")
length = int(length)

def title():
    print ("Exclusive: " + person1 + " is feuding with " + person2 + "!")


def open_file_and_get_text(filename):
    # open the file, as a read-only.
    with open(filename, 'r') as our_file:
        # takes the file and reads it.
        text = our_file.read()
    return text

# the text from which to pull the junk news.
filename = "eyre.txt"
text = open_file_and_get_text(filename)

# next step: tokenize words so it starts and ends with words.
def main_body():
    rand_seg = random.randint(1,5000)
    print (text[rand_seg:(rand_seg+length)])

# The outputs
title()
main_body()
