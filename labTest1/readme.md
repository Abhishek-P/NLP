#LAB 1 - Similarity Assignment
##Methodolgy to be added
Legend:
tweets.txt -  initial input
cleantweets.txt - cleanedn input
thresholdtweets.txt - output of below_threshold
unigram_counts.py  - generates vocab - dict of words vs counts, stored as 'vocab.pickle'
below_threshold -  uses 'vocab.pickle' to replace the words below threshold( set as a variable in the code) to $XX$, output is thresholdtweets.txt
generate_trigrams -  generates trigrams from 'thresholdtweets.txt', stored and 'trigrams.pickle'
similarity  - implements the algo to generate the similarity score( range 0 to 1 ), wordpairs can be set in the wordpair list
vocab_counts - a program to display the unigrams in a decreasing order of counts - just for visualiztion and other purposes
word2vec -  similarity of wordpairs using word2vec model using the same 'cleantweets.txt' as input



