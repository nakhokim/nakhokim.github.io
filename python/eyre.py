# loading the package nltk, load it for this file.
import nltk

def open_file_and_get_text(filename):
    # open the file, as a read-only.
    with open(filename, 'r') as our_file:
        # takes the file and reads it.
        text = our_file.read()
    return text

def clean_tokens(words):
    # creates an empty list
    clean_words = []
    for word in words:
        # fills with lowercased words
        clean_words.append(word.lower())
    return clean_words


# variable 'filename' for where our file is.
filename = "eyre.txt"

# print the first 99 characters of the text.
# print(text[0:100])

text = open_file_and_get_text(filename)


# take long string and break into words.
words = nltk.word_tokenize(text)
# print(words[0:10])

clean_words = clean_tokens(words)
word_counts = nltk.FreqDist(clean_words)
print(word_counts.most_common(10))
print(word_counts['jane'])
nltk.Text(clean_words).dispersion_plot(['he','she','jane','tony'])
