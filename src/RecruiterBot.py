from PdfExtractor import *

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
        for skill in skills:
            h = words.index(skill)
            l = 0
            r = len(words)
            gcnt=1
            gscore=0.0
            for i in range(l,r):
                tmp = words[i]
                f = True
                for elem in Recruiter.preposition:
                    if elem == tmp:
                        f = False
                if f:
                    cnt=1
                    score=0.0
                    if skill in Recruiter.pool:
                        for s in Recruiter.pool[skill]:
                            arr = s.txt.split(' ')
                            if tmp in arr:
                                cnt+=1
                                score+=float(s.score)
                        score = score / cnt
                        gcnt+=1
                        gscore+=score
            gscore = gscore/gcnt
            score_card[skill] = gscore
        return score_card

txt = PdfExtractor.getResumeText("resume.pdf")

skills = Recruiter.fetchTechSkills(txt)

Recruiter.buildPool("c++")

print Recruiter.getScore(txt,skills)
