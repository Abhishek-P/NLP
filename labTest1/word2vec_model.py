# -*- coding: utf-8 -*-
"""
Created on Sun Sep 04 10:11:40 2016

@author: Abhishek P Taula
"""
import time
import nltk
import gensim
import pickle
start_time = time.time()
with open("cleantweets.txt","r") as cleantweets:
    text = cleantweets.readlines()
for i in range(len(text)):
    text[i] = text[i].split(" ")

word2vec_model_dump = open("word2vec_model.pickle","wb")
word2vec_model = gensim.models.Word2Vec(text, window = 3 ,min_count = 5)
pickle.dump(word2vec_model,word2vec_model_dump)
word2vec_model_dump.close()
print "Time:",time.time()- start_time