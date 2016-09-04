# -*- coding: utf-8 -*-
"""

"""
import re
import time
import nltk
lemmatizer =  nltk.stem.WordNetLemmatizer().lemmatize
stemmer = nltk.stem.PorterStemmer().stem

unwanted = {",","&","%","$","^","*","(","}",";",":","\"","\'","``","''","RT","-","_","/"}
urlregex = r'(https?|ftp|file)://[-a-zA-Z0-9+&@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#/%=~_|]'
tweetsout = open("cleantweets.txt","w")
def capitalSplit( word ):
    i = 1
    while(i < len(word)):
        if( word[i].isupper()):
            word = word[:i]+" "+word[i:]
            i = i+1
        i = i+1
    return word
start_time = time.time()
tweets = open("tweets.txt","r")
line = None
count = 0
line = tweets.readline()
while(not line == ""):
    count = count + 1  
    
    line = re.sub(urlregex," ",line)
    line = re.sub('http','',line)  
    line = re.sub("\.+",".",line)
    #print line
    if( line == "\n"):
        line = tweets.readline()    
        continue
    print count
    #print line
    line = line.rstrip()
    line = nltk.tokenize.word_tokenize(line)
    i = 0
    while(i < len(line)):
        if( (line[i] == "#" or line[i] == "@") and i+1 < len(line)):
            temp = capitalSplit(line[i+1])
            line[i+1] = temp    
            line.remove(line[i])
        if( line[i] in unwanted ):
           line.remove(line[i])
           continue
        if( line[i] in {"!","?"}):
            line[i] = "."
        i = i + 1
        line2  = lemmatizer(stemmer(line[0]))
    for i in line[1:]:
        line2 = line2 + " " + lemmatizer(stemmer(i))
    line2 = re.sub("(\. )+",".",line2)
    line2 = line2 + "\n"
    #print line
   # print line2
    tweetsout.write(line2.lower())
    line = tweets.readline()
    #if( count > 10):
    #    print "here"
    #    break
tweets.close()
tweetsout.close()
print "Time:",time.time()-start_time
    

