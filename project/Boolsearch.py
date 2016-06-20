import Index
import ScoreSort

query = []

def search(index, statement):
    # find the hard conditions
    require = dict(parse(index, statement))

    # get the result of score sort.
    ret = ScoreSort.sort(query, 20)

    # remove the result that doesn't match hard conditions
    for i in ret:
        if not(i[0] in require):
            ret.remove(i)
    return ret

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
        if (i < len(la) and j < len(lb) and la[i][0] == lb[j][0]):
            res.append((la[i][0], la[i][1] and lb[j][1]))
            i += 1
            j += 1
        else:
            if (i < len(la) and (j >= len(lb) or la[i][0] < lb[j][0])):
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
        if (i < len(la) and j < len(lb) and la[i][0] == lb[j][0]):
            res.append((la[i][0], la[i][1] or lb[j][1]))
            i += 1
            j += 1
        else:
            if (i < len(la) and (j >= len(lb) or la[i][0] < lb[j][0])):
                res.append(la[i])
                i += 1;
            else:
                res.append(lb[j])
                j += 1;
    return res

# negate a list
def _not(l):
    res = []
    for i in l:
        res.append(i[0], not i[0][1])
    return res
    
def parse(index, statement):
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
                ret = [(x, 0) for x in index.tf(s[4:].strip())]
            else:
                query.append(s)
                ret = [(x, 1) for x in index.tf(s)]

            ret.sort(key=lambda doc : doc[0])
            res_and = _and(res_and, ret)
        res_or = _or(res_or, res_and)
    return res_or