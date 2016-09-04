# -*- coding: utf-8 -*-
"""
Created on Sat Sep 03 19:23:13 2016

@author: Abhishek P Taula
"""
import time
import pickle
start_time = time.time()
wordpairs = [("speech","visit")]
trigram_counts = dict()
delta = 0
z = 0
with open("trigrams.pickle","rb") as trigrams_dump:
    trigrams = pickle.load(trigrams_dump)

for i in wordpairs:
    for j in trigrams:
        k = (j[0],j[2])
        if(not k in trigram_counts):
                trigram_counts[k] = [0,0]
        if i[0] == j[1]:
            trigram_counts[k][0] = trigram_counts[k][0] + trigrams[j]
        if i[1] == j[1]:
            trigram_counts[k][1] = trigram_counts[k][1] + trigrams[j]
            
count = 0
for i in trigram_counts:
    k = trigram_counts[i]
    #print i,k
    if( k[0]!=0 and k[1]!=0 ):
        delta  = delta + abs(k[0] - k[1])
        count = count + 1
        z = z + k[0] + k[1]
print len(trigram_counts),count
print delta,z
print 1 - float(delta)/float(z)
print "Time:",time.time() - start_time
            