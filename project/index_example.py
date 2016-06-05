import Index
import os

path = '../Reuters'
index = Index.Index(path, Debug=True)

#term frequency for a given term -- return a dict
print(index.tf('January'))
#term frequency for given term and document id
print(index.tf('January',1))

#document frequency
print(index.df('January'))

