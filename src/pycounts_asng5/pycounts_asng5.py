from string import punctuation
from collections import Counter

def load_text(input_file):
    "Load text from a text file and return it as a string."
    with open(input_file, 'r') as file:
        text = file.read()
    return text
    
def clean_text(text):
    "Remove punctuation and convert text to lowercase."
    text = text.lower()
    for p in punctuation:
        text = text.replace(p, "")
    return text

def count_words(input_file):
    "Count unique words in a string"
    text = load_text(input_file)
    text = clean_text(text)
    words = text.split()
    word_counts = Counter(words)
    return word_counts