import re

import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
from textblob import TextBlob

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

# a. Text cleaning
def clean_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text) # remove punctuation, special characters, and numbers
    text = re.sub(r'\s+', ' ', text).strip() # remove extra spaces
    return text

# b. Convert text to lowercase
def convert_to_lowercase(text):
    return text.lower()

# c. Tokenization
def tokenize_text(text):
    return word_tokenize(text)

# d. Remove stop words
def remove_stop_words(tokens):
    stop_words = set(stopwords.words('english'))
    words = []
    for word in tokens:
        if word not in stop_words:
            words.append(word)
    return words

# e. Correct misspelled words
def correct_spelling(tokens):
    return [str(TextBlob(word).correct()) for word in tokens]

# Main function to perform all tasks
def process_text(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    cleaned_text = clean_text(text)

    cleaned_text = convert_to_lowercase(cleaned_text)

    tokens = tokenize_text(cleaned_text)

    filtered_tokens = remove_stop_words(tokens)

    corrected_tokens = correct_spelling(filtered_tokens)

    print("Cleaned, Tokenized, and Corrected Text:")
    print(" ".join(corrected_tokens))

file_path = "sample.txt" 
process_text(file_path)