import pickle
import time

import Index
import Boolsearch

if (__name__ == '__main__'):
    with open('index.pickle', 'rb') as f:
        index = pickle.load(f)
    
    begin = time.perf_counter()
    print(Boolsearch.parse(index, 'January AND February AND December'))
    end = time.perf_counter()
    print('takes {0} seconds to get hard conditions'.format(end-begin))

    print('Search: ', Boolsearch.query)

    begin = time.perf_counter()
    ret = Boolsearch.search(index, 'January AND February AND December')
    for i in ret:
        print(i)
    end = time.perf_counter()
    print('takes {0} seconds to perform a bool search'.format(end-begin))