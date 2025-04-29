import re

import nltk
from nltk.corpus import stopwords
from nltk import PorterStemmer, WordNetLemmatizer, word_tokenize, ngrams

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def clean_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text) # remove punctuation, special characters, and numbers
    text = re.sub(r'\s+', ' ', text).strip() # remove extra spaces
    return text

def convert_to_lowercase(text):
    return text.lower()

def stemming_and_lemmatization(tokens):
    ps = PorterStemmer()
    lemmatizer = WordNetLemmatizer()

    stemmed_words = [ps.stem(word) for word in tokens]
    lemmatized_words = [lemmatizer.lemmatize(word) for word in stemmed_words]
    
    return lemmatized_words

# create a list of 3 consecutive words after lemmatization
def generate_consecutive_ngrams(tokens):
    trigrams = list(ngrams(tokens, 3))
    return trigrams

def process_text(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    cleaned_text = clean_text(text)

    cleaned_text = convert_to_lowercase(cleaned_text)

    tokens = word_tokenize(cleaned_text)

    lemmatized_words = stemming_and_lemmatization(tokens)

    # create a list of 3 consecutive words (trigrams)
    trigrams = generate_consecutive_ngrams(lemmatized_words)

    print("3 consecutive words after lemmatization:")
    for trigram in trigrams:
        print(trigram)

file_path = "sample2.txt"
process_text(file_path)