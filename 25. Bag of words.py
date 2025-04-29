import os
import re

from numpy import ndarray
from sklearn.feature_extraction.text import CountVectorizer

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def clean_text(text):
    text = re.sub(r'[^A-Za-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.strip().lower()
    return text

# read, clean, tokenize, and vectorize text files
def process_files(file_paths):
    corpus = []
    for file_path in file_paths:
        content = read_file(file_path)
        cleaned_content = clean_text(content)
        corpus.append(cleaned_content)
    
    # implementing Bag of Words using CountVectorizer
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(corpus)
    
    return X, vectorizer.get_feature_names_out()

# main function to process the text files
def main():
    file_paths = ['sample1.txt', 'sample2.txt', 'sample3.txt'] 

    X, feature_names = process_files(file_paths)
    
    print("Bag of Words Model (Word Count Matrix):\n")
    print(type(X))
    print(X.toarray()) # type: ignore
    print("\nFeature Names (Vocabulary):\n")
    print(feature_names)

if __name__ == "__main__":
    main()