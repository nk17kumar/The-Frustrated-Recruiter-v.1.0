from PdfExtractor import *
from progress import *
from textblob import TextBlob

import time

class Response:

    def __init__(self, score, txt):
        self.score = score
        self.txt = txt

class Recruiter:

    pool = {}
    preposition = ['a','the','of','in','and','i','have','also','but']

    @staticmethod
    def fetchTechSkills(resume):
        skills = []
        skillSet = ["c++","java","python","html","css","database"]
        words = resume.split(' ')
        for skill in skillSet:
            for w in words:
                tmp = w.lower()
                if tmp == skill:
                    skills.append(tmp)
        return skills

    @staticmethod
    def buildPool(lang):
        fin = open(str(lang)+"res.txt")
        arr = fin.readlines()
        a = []
        for elem in arr:
            tmp = elem.split(',')
            e = Response(tmp[0],tmp[1])
            a.append(e)
        Recruiter.pool[lang] = a

    @staticmethod
    def getScore(resume,skills):
        words = resume.split(' ')
        score_card = {}
        # for all skill in the skillset
        for skill in skills:
            # h = words.index(skill)
            l = 0
            r = len(words)
            cnt=0
            score=0.0
            # for all words in the resume
            for i in range(l,r):
                tmp = words[i]
                f = True
                #checking if it is preposition
                for elem in Recruiter.preposition:
                    if elem == tmp:
                        f = False
                #if not prepositon
                if f:
                    # checking if current skill is in pool
                    if skill in Recruiter.pool:
                        # for all data for this skill
                        for s in Recruiter.pool[skill]:
                            arr = s.txt.split(' ')
                            if tmp in arr:
                                cnt+=1
                                score+=float(s.score)
            if cnt != 0:
                gscore = score/cnt
            score_card[skill] = gscore
        return score_card

print "Initializing the recruiter bot\n"
arr = ['c++','java','python','html-css','database','leadership','communication']

for s in arr:
    Recruiter.buildPool(s)

total = 6
i = 0
while i <= total:
    progress(i, total, status='Training on dataset for '+arr[i]+'\n')
    time.sleep(0.1)  # emulating long-playing job
    i += 1
print '\n'

resume = raw_input("enter the resume file location : ")
print "\n"
txt = PdfExtractor.getResumeText(resume)

total = 3
i = 0
while i <= total:
    progress(i, total, status='Extracting Text\n')
    time.sleep(0.1)  # emulating long-playing job
    i += 1
print '\n'

skills = Recruiter.fetchTechSkills(txt)
# skills.append("leadership")
# skills.append("communication")

print Recruiter.getScore(txt,skills)
