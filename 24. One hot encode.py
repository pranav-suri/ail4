import os
import re

import numpy as np

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def clean_text(text):
    text = re.sub(r'[^A-Za-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.strip().lower()
    return text

def tokenize(text):
    return text.split()

def one_hot_encode(corpus: list[str]):
    # create a list of all words in the corpus
    all_words: set[str] = set()
    for text in corpus:
        all_words.update(tokenize(text))
    
    # create a mapping from word to index
    word_to_index = {word: idx for idx, word in enumerate(sorted(all_words))}
    
    # encode each sentence into a one-hot vector
    one_hot_encoded_corpus = []
    for text in corpus:
        words = tokenize(text)
        one_hot_vector = np.zeros(len(word_to_index))
        for word in words:
            if word in word_to_index:
                one_hot_vector[word_to_index[word]] = 1
        one_hot_encoded_corpus.append(one_hot_vector)
    
    return one_hot_encoded_corpus, word_to_index

# read, clean, tokenize, and encode text files
def process_files(file_paths):
    corpus = []
    for file_path in file_paths:
        content = read_file(file_path)
        cleaned_content = clean_text(content)
        corpus.append(cleaned_content)
    
    one_hot_encoded_corpus, word_to_index = one_hot_encode(corpus)
    
    return one_hot_encoded_corpus, word_to_index

# Main function to process the text files
def main():
    file_paths = ['sample1.txt', 'sample2.txt', 'sample3.txt']  # Add your file paths here
    
    # Process the files
    one_hot_encoded_corpus, word_to_index = process_files(file_paths)
    
    # Display the results
    print(f"Vocabulary (word-to-index mapping): {word_to_index}\n")
    for idx, sentence_vector in enumerate(one_hot_encoded_corpus):
        print(f"Sentence {idx + 1} One-Hot Encoding: {sentence_vector}\n")

if __name__ == "__main__":
    main()