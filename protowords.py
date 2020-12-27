# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 19:08:25 2020

@author: r.meester
"""

import os
import csv
import math 
import collections

def average_wordlength(row):
  total_lenght = 0  
  for word in row:
      length = len(word)  
      total_lenght = total_lenght + length
  
  average_lenght = math.floor(total_lenght / len(row))
  return average_lenght

def get_most_frequent_character(row,place):
    character = ''

    for word in row:
      if place < len(word):  
          new_character = word[place]
          character = character + new_character

    frequest_character = collections.Counter(character).most_common(1)[0]
    return frequest_character



f = open('output_protowords.txt', 'a', encoding="utf8")

with open('input_words.csv', encoding="utf8", newline='') as csvfile:
         rows = csv.reader(csvfile, delimiter=';')
         for row in rows:
             wordlength = average_wordlength(row)
             proto_word = ''
             for letter in range(0, wordlength):
                 most_frequent_character = get_most_frequent_character(row,letter)
                 proto_word = proto_word + most_frequent_character[0]
           
             print(proto_word)
             if not proto_word.isspace():
                 f.write(proto_word + '\n')

f.close()
             
             
           