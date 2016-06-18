import Index
import pickle
import os
import time
import sys
import VectorSpace
print (sys.version)

path = '../Reuters'
index = Index.Index(path)

begin = time.perf_counter()
space = VectorSpace.VectorSpace(index)
end = time.perf_counter()
print('takes {0} seconds to build vector space'.format(end-begin))

begin = time.perf_counter()
with open('space.pickle', 'wb') as f:
	pickle.dump(space, f)
end = time.perf_counter()
print('takes {0} seconds to save vector space'.format(end-begin))

begin = time.perf_counter()
with open('space.pickle', 'rb') as f:
	space = pickle.load(f)
end = time.perf_counter()
print('takes {0} seconds to load vector space'.format(end-begin))

#for term in space.terms:
	#print("term weight in query if tf = 1 for term \"{0}\" = {1}".format(term, space.q_weight_t(term)))

#for docID in space.docIDs:
	#print("lenth of vector for Doc {0} is {1}".format(docID, space.doc_vec_len[docID]))

#for term in space.terms:
	#if index.tf(term, space.docIDs[0]):
		#print("tf for \"{0}\" in Doc {1} is {2}".format(term, space.docIDs[0], index.tf(term, space.docIDs[0])))

#for term in space.terms:
	#if space.d_weight_t(space.docIDs[0], term):
		#print("term weight for term \"{0}\" in Doc {1} is {2}".format(term, space.docIDs[0], space.d_weight_t(space.docIDs[0], term)))
