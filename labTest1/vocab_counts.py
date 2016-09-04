# -*- coding: utf-8 -*-
"""
Created on Sat Sep 03 21:21:57 2016

@author: Abhishek P Taula
"""
import time
import pickle
vocab_list = []
with open("vocab.pickle","rb") as vocab_dump:
        vocab = pickle.load(vocab_dump)
        
for i in vocab:
    vocab_list.append((i,vocab[i]))

vocab_list = sorted(vocab_list,key = lambda x: x[1], reverse = True)
for i in vocab_list[:50]:
    print i
    
