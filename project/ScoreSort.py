#! python3
import random
import Index
import pickle
import os
import time
import sys
import VectorSpace
DOCNUM = 21577

#def d_weight_t(docID,term):
#    #vec = []
#    #for i in range(len(terms)):
#    #    vec.append(random.random()*100)
#    return random.random()*10

def ShiftHeap(q,x):
    length = len(q)
    i = x
    j = i * 2 + 1
    if j+1<length and q[j+1][1]>q[j][1]:
            j += 1
    while j<length:
        if q[j][1] <= q[i][1]:
            break
        tem = q[j]; q[j] = q[i]; q[i] = tem;
        i = j
        j = i * 2 + 1
        if j+1<length and q[j+1][1]>q[j][1]:
                j += 1
    return

def HeapPop(q):
    if len(q)==0 :
        return -1
    result = q[0]
    q[0] = q[-1]
    del q[-1]
    ShiftHeap(q,0)
    return result

def topK(Scores,K):
    for i in range(len(Scores)//2,-1,-1):
       ShiftHeap(Scores,i)
    result = []
    for i in range(K):
        pair = HeapPop(Scores)
        if (pair == -1):
            break        
        result.append(pair)
    return result

def sort(query,K):
    if K>DOCNUM:
        K = DOCNUM
    if K<=0:
        return []
    terms = []
    for i in range(len(query)):
        if (query[i] in terms):
            continue
        terms.append(query[i])
    with open('space.pickle', 'rb') as f:
        space = pickle.load(f)
    Scores = []
    for i in range(DOCNUM):
        score = 0
        for j in range(len(terms)):
            weight = space.d_weight_t(i,terms[j])
            score += weight
        pair = (i,score)
        Scores.append(pair)
    #Sc = Scores.copy()
    #Sc.sort(reverse=True,key=lambda x:x[1] )
    #test = []
    #for i in range(K):
    #    test.append(Sc[i][0])
    result = topK(Scores,K)
    return result

