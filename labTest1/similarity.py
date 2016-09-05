# -*- coding: utf-8 -*-
"""
Created on Sat Sep 03 19:23:13 2016

@author: Abhishek P Taula
"""
import time
import pickle
start_time = time.time()
wordpairs = [("taliban","terror"),("speech","terror"),("india","dubai"),\
("india","uae"),("indian","aaptard"),("visit","speech"),("visit","terror")\
,("congress","bjp"),("aap","bjp"),("aap","congress"),("aap","taliban")\
,("bjp","taliban"),("congress","taliban")]
trigram_counts = dict()
delta = 0
z = 0
with open("trigrams.pickle","rb") as trigrams_dump:
    trigrams = pickle.load(trigrams_dump)

for i in wordpairs:
    delta = 0
    z = 0
    for j in trigrams:
        k = (j[0],j[2])
        if(not k in trigram_counts):
                trigram_counts[k] = [0,0]
        if i[0] == j[1]:
            trigram_counts[k][0] = trigram_counts[k][0] + trigrams[j]
        if i[1] == j[1]:
            trigram_counts[k][1] = trigram_counts[k][1] + trigrams[j]
            
    for x in trigram_counts:
        k = trigram_counts[x]
        #print i,k
        if( k[0]!=0 and k[1]!=0 ):
            delta  = delta + abs(k[0] - k[1])
            z = z + k[0] + k[1]
    print i[0], i[1], 1 - float(delta)/float(z)
            
#print len(trigram_counts),count
#print delta,z
print "Time:",time.time() - start_time
            