# -*- coding: utf-8 -*-
"""
Created on Sat Sep 03 18:09:01 2016

@author: Abhishek P Taula
"""
import time
import nltk
import pickle
start_time = time.time()
threshold = 5
count = 0
cleantweets = open("cleantweets.txt","r")
thresholdtweets = open("thresholdtweets.txt","w")
with open("vocab.pickle","rb") as vocab_dump:
    vocab = pickle.load(vocab_dump)

below_threshold = set()
for i in vocab:
    if( vocab[i] < threshold):
        below_threshold.add(i)
print len(below_threshold)

line  = cleantweets.readline()
#print line,type(line)
while( not line == "" ):
    count = count+1
    print count
    line = line.rstrip()
    if( line == ""):
        line = cleantweets.readline()
        continue
    line  = nltk.tokenize.word_tokenize(line)
    line2 = line[0]
    for i in line[1:]:
        if(i in below_threshold):
             i = "$XX$"
        line2 = line2 + " " +i 
    line2 = line2 + "\n"
    thresholdtweets.write(line2)
    line = cleantweets.readline()

cleantweets.close()
thresholdtweets.close()
print "Time:",time.time() - start_time
