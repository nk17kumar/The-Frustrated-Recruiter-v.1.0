import sys
#y=sys.argv[1]

import os
import re
from textblob import TextBlob
import json
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from datetime import datetime
import operator
import string
import collections
from nltk.stem import PorterStemmer
#from sklearn.cluster import KMeans
#from sklearn.feature_extraction.text import TfidfVectorizer
from pprint import pprint
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
import config as cfg

path_to_webapp=cfg.path_to['webapp']
path_to_InputFiles=cfg.path_to['InputFiles']

pos=0
neg=0
neu=0

def fun(dirctry,fname):
    os.chdir(dirctry)
    f = open(fname,'r')
    p=f.read().decode('latin-1')
    #print "****",p
    q = p.replace("\n"," ")
    #print "----",q
    regexMatch = re.findall('[^.!?)]+[.!?)]+',q)
    #print "####",regexMatch
    f.close()
    htmls=[]
    i=0
    for s in regexMatch:
        #print "$$$$",s
        i=i+1
        #print(s)
        t=TextBlob(s)
        x="%.2f" % t.sentiment.polarity
        if t.sentiment.polarity > 0:
            global pos
            pos+=1
        elif t.sentiment.polarity == 0:
            global neu
            neu+=1
        else:
            global neg
            neg+=1
        htmls.append("<tr><td>"+fname+"</td><td>"+str(i)+"</td><td>"+s+"</td><td>"+x+"</td></tr>")

    b=open(path_to_webapp+"webapp_with_config\\index_general.html","r")
    ft=b.read()
    #print ft
    b.close()
    a=open(path_to_webapp+"webapp_with_config\\index_general.html","w")
    ind=ft.find("<tbody>")+8
    ind2=ft.find("</tbody>")
    a.write(ft[:ind2])
    for h in htmls:
        a.write(h.encode('utf-8')+"\n")
    #ind3=ft.find("</tbody>")
    a.write(ft[ind2:])
    a.close()

    return

if __name__=="__main__":
    
    dirc=sys.argv[1]
    directory=dirc.replace('\\','\\\\')
    #print directory
    #a=open("w1.txt","w")
    b=open(path_to_webapp+"webapp_with_config\\index_general.html","r")
    ft=b.read()
    #print ft
    b.close()
    a=open(path_to_webapp+"webapp_with_config\\index_general.html","w")
    ind=ft.find("<tbody>")+8
    a.write(ft[:ind])
    ind3=ft.find("</tbody>")
    a.write(ft[ind3:])
    a.close()
    for path,subdirs,files in os.walk(directory):
        #print files
        for filename in files:
            if filename.endswith('.txt'):
                #x=2
                #print filename
                fun(directory,filename)
                #a.write(filename+"\n")
    #a.close()

    data=["function drawChart() {","var data = google.visualization.arrayToDataTable([","['Sentiment','Number'],"]
    data.append("['Positive',"+str(pos)+"],['Negative',"+str(neg)+"],['Neutral',"+str(neu)+"]]);")
    data.append("var chart = new google.visualization.PieChart(document.getElementById('chart_div'));")
    data.append("chart.draw(data, options);}")
    da='\n'.join(data)
    #print ft
    b=open(path_to_webapp+"webapp_with_config\\index_general.html","r")
    ft=b.read()
    b.close()
    a=open(path_to_webapp+"webapp_with_config\\index_general.html","w")
    ind=ft.find("function drawChart() {")
    a.write(ft[:ind])
    a.write(da)
    ind3=ft.find("</script>",ind)
    a.write(ft[ind3:])
    a.close()

    
