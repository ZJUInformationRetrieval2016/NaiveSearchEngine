import nltk
import os
import time
import pickle

import Index
import ScoreSort
import Boolsearch

if (__name__ == '__main__'):
    while (1):
        _input = ''
        _input = input('# ')
        if (_input.endswith('-b')):
            ret = Boolsearch.search(_input, 16)
            for i in ret:
                print(i)
        else:
            tokens = Index.parse(_input)
            print("Search: ", tokens)
            if tokens:
                ret = ScoreSort.sort(tokens, 16)
            for i in ret:
                print(i)