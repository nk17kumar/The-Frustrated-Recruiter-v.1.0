import sys
import math
from textblob import TextBlob as tb
import os
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize,word_tokenize
import config as cfg

path_to_webapp=cfg.path_to['webapp']
path_to_InputFiles=cfg.path_to['InputFiles']

##typ=sys.argv[2]
dirc=sys.argv[1]
directory=dirc.replace("\\","\\\\")
typ='0'
#directory=path_to_InputFiles+"InputFiles\\Input8\\"
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
if len(A)>80:
    newA = dict(sorted(A.iteritems(), key=operator.itemgetter(1), reverse=True)[:80])
else:
    newA = dict(sorted(A.iteritems(), key=operator.itemgetter(1), reverse=True))
#print newA
if typ=='0':
    from sklearn.cluster import KMeans
    from sklearn.feature_extraction.text import TfidfVectorizer
    t=' '.join(newA.keys())    
    #print t
    dire=path_to_InputFiles+"InputFiles\\corpus\\"
    os.chdir(dire)
    c=""
    maxs=0
    maxn=''
    vectorizer = TfidfVectorizer(min_df=1,lowercase=True)
    for path,subdirs,files in os.walk(dire):
        for filename in files:
            if filename.endswith('.txt'):
                f=open(filename,'r')
                b=f.read().decode('latin-1')
                f.close()
##                listb=b.split("\n")
##                listt=t.split(" ")
##                score=len(set(listb)&set(listt))
                b.replace('\n',' ')
                texts=[t,b]
                tfidf = vectorizer.fit_transform(texts)
                score=(tfidf*tfidf.T).A[0,1]
                #print filename,(tfidf*tfidf.T).A[0,1]
                #print filename,float(score)/float(len(listt))
                if score>maxs:
                    maxs=score
                    maxn=filename
    if maxs>0.05:
        
        print maxn.split("_")[0]
        b=open(path_to_webapp+"webapp_with_config\\loaded.html","r")
        ft=b.read()
        #print ft
        b.close()
        a=open(path_to_webapp+"webapp_with_config\\loaded.html","w")
        ind=ft.find('<div class="ntext">')
        a.write(ft[:ind])
        a.write('<div class="ntext">TextPool thinks that this corpus is about '+maxn.split('_')[0]+'.')
        ind2=ft.find('</div>',ind)
        a.write(ft[ind2:])
        a.close()

        b=open(path_to_webapp+"webapp_with_config\\loaded.html","r")
        ft=b.read()
        #print ft
        b.close()
        a=open(path_to_webapp+"webapp_with_config\\loaded.html","w")
        ind=ft.find('<div id="imgs">')
        a.write(ft[:ind])
        a.write('<div id="imgs"><img src="http://localhost:8081/images/'+maxn.split('_')[0]+'/2.png" height="750px" width="800px">')
        ind2=ft.find('</div>',ind)
        a.write(ft[ind2:])
        a.close()

    else:
        print maxn.split("_")[0]
        b=open(path_to_webapp+"webapp_with_config\\loaded.html","r")
        ft=b.read()
        #print ft
        b.close()
        a=open(path_to_webapp+"webapp_with_config\\loaded.html","w")
        ind=ft.find('<div class="ntext">')
        a.write(ft[:ind])
        a.write('<div class="ntext">We think this corpus is about '+maxn.split('_')[0]+'. But we are not sure.')
        ind2=ft.find('</div>',ind)
        a.write(ft[ind2:])
        a.close()

        b=open(path_to_webapp+"webapp_with_config\\loaded.html","r")
        ft=b.read()
        #print ft
        b.close()
        a=open(path_to_webapp+"webapp_with_config\\loaded.html","w")
        ind=ft.find('<div id="imgs">')
        a.write(ft[:ind])
        a.write('<div id="imgs">')
        ind2=ft.find('</div>',ind)
        a.write(ft[ind2:])
        a.close()


else:
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
