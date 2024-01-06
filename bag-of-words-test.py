# Make sure to install the necessary packages first
# pip install --upgrade pip
# pip install tensorflow
from tensorflow import keras
from typing import List
from keras.preprocessing.text import Tokenizer

text = open("audio0.txt","r")
print(text.read())
sentence = [text.read()]
text.close()
def print_bow(sentence: List[str]) -> None:
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(sentence)
    sequences = tokenizer.texts_to_sequences(sentence)
    word_index = tokenizer.word_index 
    bow = {}
    for key in word_index:
        bow[key] = sequences[0].count(word_index[key])

    print(f"Bag of word sentence 1:\n{bow}")
    print(f"We found {len(word_index)} unique tokens.")

print_bow(sentence)
