# -*- coding: utf-8 -*-
"""
Created on Mon Sep 05 21:06:05 2016

@author: Abhishek P Taula
"""

import time
import nltk
import gensim
import pickle
start_time = time.time()
wordpairs = [("taliban","terror"),("speech","terror"),("india","dubai"),\
("india","uae"),("indian","aaptard"),("visit","speech"),("visit","terror")\
,("congress","bjp"),("aap","bjp"),("aap","congress"),("aap","taliban")\
,("bjp","taliban"),("congress","taliban")]
with open("word2vec_model.pickle","rb") as word2vec_model_dump:
    word2vec_model = pickle.load(word2vec_model_dump)

for i in wordpairs:
    print i[0],i[1],word2vec_model.similarity(i[0],i[1])
    
print  "Time:", time.time() - start_time