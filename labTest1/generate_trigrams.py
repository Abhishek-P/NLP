# -*- coding: utf-8 -*-
"""
Created on Sat Sep 03 18:55:06 2016

@author: Abhishek P Taula
"""

import nltk
import pickle
import time
start_time = time.time()

thresholdtweets = open("thresholdtweets.txt","r")
trigrams_dump = open("trigrams.pickle","wb")
line = thresholdtweets.readline()
count = 0
trigrams = dict()
while( not line == ""):
    count = count+1
    print count
    line = line.rstrip()
    sent_list = line.split(".")
    for i in sent_list:
        i = i.split(" ")
        if "" in i:
            i.remove('')
        #print i
        for j in range(len(i) - 2 ):
            temp_trigram = (i[j],i[j+1],i[j+2])
            if temp_trigram  not in trigrams:
                trigrams[temp_trigram] = 0
            trigrams[temp_trigram] = trigrams[temp_trigram] + 1       
    line = thresholdtweets.readline()
print len(trigrams)
pickle.dump(trigrams,trigrams_dump)
trigrams_dump.close()
"""
avg = 0
count = 0

for i in trigrams:
    if( trigrams[i] > 0):
        count = count + 1
        print i,trigrams[i]
    avg = avg + trigrams[i]
    #print i,trigrams
print avg/len(trigrams), count"""

print "Time:",time.time() -  start_time