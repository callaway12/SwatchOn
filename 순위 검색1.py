from dataclasses import dataclass
from collections import defaultdict

@dataclass
class Info:
    lang: str
    pos: str
    career: str
    food: str
    score: int
    
def infoParser(infos):
    infoDict = defaultdict(Info)
    
    for idx, info in enumerate(infos):
        splitedInfo = info.split(' ')
        infoDict[idx] = Info(lang=splitedInfo[0], pos=splitedInfo[1], career=splitedInfo[2], food=splitedInfo[3], score=int(splitedInfo[4]))
    return infoDict

def queryParser(queries):
    queryDict = defaultdict(list)
    for idx1, query in enumerate(queries):
        splitedQuery = query.split(' ')
        
        while 'and' in splitedQuery:
            splitedQuery.remove('and')
            
        for idx2, q in enumerate(splitedQuery):
            if idx2 == 0:
                if q != '-':
                    queryDict[idx1].append(q)
                elif q == '-':
                    queryDict[idx1].append(-1)
            if idx2 == 1:
                if q != '-':
                    queryDict[idx1].append(q)
                elif q == '-':
                    queryDict[idx1].append(-1)
            if idx2 == 2:
                if q != '-':
                    queryDict[idx1].append(q)
                elif q == '-':
                    queryDict[idx1].append(-1)
            if idx2 == 3:
                if q != '-':
                    queryDict[idx1].append(q)
                elif q == '-':
                    queryDict[idx1].append(-1)
            if idx2 == 4:
                if q != '-':
                    queryDict[idx1].append(int(q))
                elif q == '-':
                    queryDict[idx1].append(-1)
    return queryDict
                

def findMatch(infos, queries):
    countList = []
    infoDict = infoParser(infos)
    queryDict = queryParser(queries)
    
    for query in queryDict.values():
        count = 0
        if len(query) != 5:
            print('query length error')
        else:
            for info in infoDict:
                flag = True
                tmpInfo = infoDict[info]
                if query[0] != -1:
                    if query[0] == tmpInfo.lang:
                        pass
                    else:
                        flag = False
                if query[1] != -1:
                    if query[1] == tmpInfo.pos:
                        pass
                    else:
                        flag = False
                if query[2] != -1:
                    if query[2] == tmpInfo.career:
                        pass
                    else:
                        flag = False
                if query[3] != -1:
                    if query[3] == tmpInfo.food:
                        pass
                    else:
                        flag = False
                if query[4] != -1:
                    if query[4] <= tmpInfo.score:
                        pass
                    else:
                        flag = False
                if flag == True:
                    count += 1
        countList.append(count)
    return countList  
                        

def solution(infos, queries):
    answer = []

    answer = findMatch(infos, queries)


    return answer
