import Index
import pickle
import os

path = '../Reuters'
index = Index.Index(path, Debug=True)

#term frequency for a given term -- return a dict
print(index.tf('January'))
#term frequency for given term and document id
print(index.tf('January',1))

#use pickle to store the index
with open('index.pickle', 'wb') as f:
	pickle.dump(index, f)

#read it when you need it
with open('index.pickle', 'rb') as f:
	index_reload = pickle.load(f)


#document frequency
print(index_reload.tf('January'))
print(index_reload.df('January'))

