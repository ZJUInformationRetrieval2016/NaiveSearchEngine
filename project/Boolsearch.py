import pickle

import Index
import ScoreSort

DOCNUM = 21577
query = []

with open('index.pickle', 'rb') as f:
    index = pickle.load(f)

def search(statement, K=DOCNUM):
    # find the hard conditions
    require = parse(statement)

    # get the result of score sort.
    ret = ScoreSort.sort(query)

    if K > len(require):
        K = len(require)

    # remove the result that doesn't match hard conditions
    k = 0
    result = []
    for i in range(len(ret)):
        if (ret[i][0] in require):
            result.append(ret[i])
            k += 1
            if (k >= K):
                break;

    return result

#merge two list using and
def _and(la, lb):
    if (not la): 
        return lb;
    if (not lb): 
        return la;
    res = []
    i = 0
    j = 0
    while (i < len(la) or j < len(lb)):
        if (i < len(la) and j < len(lb) and la[i] == lb[j]):
            res.append(la[i])
            i += 1
            j += 1
        else:
            if (i < len(la) and (j >= len(lb) or la[i] < lb[j])):
                i += 1
            else:
                j += 1
    return res

#merge two list using or
def _or(la, lb):
    if (not la): 
        return lb;
    if (not lb): 
        return la;
    res = []
    i = 0
    j = 0
    while (i < len(la) or j < len(lb)):
        if (i < len(la) and j < len(lb) and la[i] == lb[j]):
            res.append(la[i])
            i += 1
            j += 1
        else:
            if (i < len(la) and (j >= len(lb) or la[i] < lb[j])):
                res.append(la[i])
                i += 1;
            else:
                res.append(lb[j])
                j += 1;
    return res

# negate a list
def _not(l):
    res = []
    for j in range(0, l[0]):
        res.append(j)
    for i in range(len(l) - 1):
        for j in range(l[i] + 1, l[i + 1]):
            res.append(j)
    return res
    
# get the hard condition
def parse(statement):
    query.clear()
    ors = statement.split('OR')
    # disjunctions
    res_or = []
    for term in ors:
        ands = term.split('AND')
        # conjunctions
        res_and = []
        for s in ands:
            s = s.strip()
            if (s[0:3].startswith('NOT')):
                ret = [x for x in index.tf(s[4:].strip())]
                ret = _not(ret)
            else:
                query.append(s)
                ret = [x for x in index.tf(s)]

            ret.sort()
            res_and = _and(res_and, ret)
        res_or = _or(res_or, res_and)
    return res_or