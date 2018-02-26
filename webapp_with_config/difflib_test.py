import difflib as dl
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.stem import PorterStemmer
from collections import Counter
import operator

a=open("C:\\InputFiles\\Input3\\sports.txt").read().lower()
b=open("C:\\InputFiles\\Input3\\sports2.txt").read().lower()
##a="Food eating ambience good service not mark".lower()
##b="ambience eat great service staff food bad".lower()

stop_words=set(stopwords.words("english"))
wa=word_tokenize(a)
wb=word_tokenize(b)
import string
import re
stemmer = PorterStemmer()
filtered_senta=[]
for w in wa:
    if w.lower() not in stop_words:
        filtered_senta.append(w)
waf=" ".join(filtered_senta).lower()
waf = re.sub(r'[^\w\s]','',waf)
list1=waf.split()
list1 = [stemmer.stem(t) for t in list1]

filtered_sentb=[]
for w in wb:
    if w.lower() not in stop_words:
        filtered_sentb.append(w)
wbf=" ".join(filtered_sentb).lower()
wbf = re.sub(r'[^\w\s]','',wbf)
list2=wbf.split()
list2 = [stemmer.stem(t) for t in list2]

list1_new=Counter(list1)
newA = dict(sorted(list1_new.iteritems(), key=operator.itemgetter(1), reverse=True)[:10])
list2_new=Counter(list2)
newB = dict(sorted(list2_new.iteritems(), key=operator.itemgetter(1), reverse=True)[:10])
list1=newA.keys()
list2=newB.keys()
sim = dl.get_close_matches

s = 0
for i in list1:
    if sim(i, list2):
        s += 1
print list1
print list2
n = float(s) / float(len(list1))
d = list((set(list1)-set(list2))|(set(list2)-set(list1)))
print '%d%% similarity' % int(n * 100)
print 'difference in words : ',d
