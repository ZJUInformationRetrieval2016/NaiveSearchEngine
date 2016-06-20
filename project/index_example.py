import Index
import pickle
import os
import time
import sys
import VectorSpace
print (sys.version)

path = '../Reuters'
begin = time.perf_counter()
index = Index.Index(path)
end = time.perf_counter()
print('takes {0} seconds to build index'.format(end-begin))

print('N = {0}'.format(index.N))

#term frequency for a given term -- return a dict
print(index.tf('January'))
#term frequency for given term and document id
print(index.tf('January',1))

#use pickle to store the index
begin = time.perf_counter()
with open('index.pickle', 'wb') as f:
	pickle.dump(index, f)
end = time.perf_counter()
print('takes {0} seconds to save index'.format(end-begin))

#read it when you need it
begin = time.perf_counter()
with open('index.pickle', 'rb') as f:
	index_reload = pickle.load(f)
end = time.perf_counter()
print('takes {0} seconds to load index'.format(end-begin))

#document frequency
print(index_reload.tf('January', 1))
print(index_reload.df('January'))
#print(index_reload.words())#get all the words

#print(index_reload.docIDs)
