import sys
import math
from textblob import TextBlob as tb
import os
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize,word_tokenize
import config as cfg

path_to_webapp=cfg.path_to['webapp']
path_to_InputFiles=cfg.path_to['InputFiles']

typ=sys.argv[2]
dirc=sys.argv[1]
directory=dirc.replace("\\","\\\\")
##typ='0'
#directory="C:\\InputFiles\\Input6\\"
os.chdir(directory)
c=""
for path,subdirs,files in os.walk(directory):
        #print files
        for filename in files:
            if filename.endswith('.txt'):
                #x=2
                #print filename
                f=open(filename,"r")
                b=f.read().decode('latin-1')
                c=c+b
                f.close()
                #a.write(filename+"\n")
stop_words=set(stopwords.words("english"))
words=word_tokenize(c)
import string
filtered_sent=[]
for w in words:
    if w.lower() not in stop_words:
        filtered_sent.append(w)
d=" ".join(filtered_sent).lower()
import re
d = re.sub(r'[^\w\s]','',d)
list1=d.split()
#print d
from collections import Counter
import operator

counts = Counter(list1)
A=counts
newA = dict(sorted(A.iteritems(), key=operator.itemgetter(1), reverse=True)[:80])
#print newA


if typ!='0':
    fname=path_to_InputFiles+"InputFiles\\corpus\\"+typ+"_corpus.txt"
    f=open(fname,"w")
    for k in newA:
        f.write(k+'\n')
    f.close()
  


#####tfidf########
#bloblist = [document1]
#for i, blob in enumerate(bloblist):
#    print("Top words in document {}".format(i + 1))
##print 'i am here',len(blob.words)
##scores = {word: tf(word, blob) for word in blob.words}
##print 'thats done now here'
##sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
##print 'sorted arent i'
##for word, score in sorted_words[:10]:
##    print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
