import pickle
import time

import Index
import Boolsearch

if (__name__ == '__main__'):
    with open('index.pickle', 'rb') as f:
        index = pickle.load(f)
    
    querry = 'January AND February AND December OR September AND October'

    #simple classical bool search
    begin = time.perf_counter()
    print(Boolsearch.parse(index, querry))
    end = time.perf_counter()
    print('takes {0} seconds to get hard conditions'.format(end-begin))

    print('Search: ', Boolsearch.query)

    #score sort filter by bool search
    begin = time.perf_counter()
    ret = Boolsearch.search(index, querry, 15)
    for i in ret:
        print(i)
    end = time.perf_counter()
    print('takes {0} seconds to perform a bool search'.format(end-begin))