import nltk
import pickle
import time
start_time = time.time()
cleantweets = open("cleantweets.txt","r")
vocab_dump = open("vocab.pickle","wb")
vocab = dict()
line = cleantweets.readline()
#print line,type(line)
count = 0
while( not line == ""):
    count = count + 1
    print count
    line  = nltk.tokenize.word_tokenize(line)
    for i in line:
        if( not i  in vocab):
            vocab[i] = 0
        vocab[i] = vocab[i] + 1
    line = cleantweets.readline()
print len(vocab)
count = 0
for i in vocab:
    if(vocab[i] > 50):
        count = count + 1
        print i,vocab[i]
pickle.dump(vocab,vocab_dump)
vocab_dump.close()
cleantweets.close()
print count,len(vocab)
print "Time:",time.time() - start_time