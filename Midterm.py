#!/usr/bin/env python
# coding: utf-8

# Input text file
data = sc.textFile("ANYFILE.txt")


#Split characters
chars = data.flatMap(lambda chars: list(chars))


#Count characters
chars_without_space = chars.filter(lambda x: x.isalnum())
charsCount = chars_without_space.map(lambda word: (word, 1)).reduceByKey(lambda x,y: x+y)


# Find the shifting key
index_of_most_common_letter = 4

charsCountSorted = charsCount.sortBy(lambda a: a[1], ascending=False)

def find_Common_Letter_in_cipher(x):

    commonLetter = ''

    for (alphabet, frequency) in charsCountSorted.take(1):

        commonLetter = alphabet
        
        return commonLetter

    print(commonLetter)
    
common_letter_in_cipher = find_Common_Letter_in_cipher(charsCountSorted)

common_Letter_in_cipher_Index = ord(common_letter_in_cipher) - 65

key = common_Letter_in_cipher_Index - index_of_most_common_letter


# Decrypt the txt file
def Decrypt(message, key):
    
    translated = ""
    
    for symbol in message.collect():

        if symbol.isalpha():
            num = ord(symbol)
            num -= key

            if num < 65:
                num += 26

            translated += chr(num)

        else:
            translated += symbol
    return translated

decryptData = Decrypt(chars, key)


# Testing if is Enlgish Language
from langdetect import detect_langs

detect_langs(decryptData)





