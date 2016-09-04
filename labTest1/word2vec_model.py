# -*- coding: utf-8 -*-
"""
Created on Sun Sep 04 10:11:40 2016

@author: Abhishek P Taula
"""
import time
import nltk
import gensim
start_time = time.time()
with open("cleantweets.txt","r") as cleantweets:
    text = cleantweets.readlines()
for i in range(len(text)):
    text[i] = text[i].split(" ")

word2vec_model = gensim.models.Word2Vec(text, window = 3 ,min_count = 5)
print word2vec_model.similarity("speech","visit")
print "Time:",time.time()- start_time