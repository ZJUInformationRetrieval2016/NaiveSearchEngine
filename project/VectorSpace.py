import Index
import pickle
import os
import time
import sys
import math
from collections import defaultdict

def dd():
    return defaultdict(float)

class VectorSpace(object):
    """vector space for score calculation"""
    def __init__(self, index):

        self.N = index.N
        self.docIDs = index.docIDs
        self.terms = list(index.words())
        #calculate idf
        self.term_idf = defaultdict(float);

        for term in self.terms:
            self.term_idf[term] = math.log(self.N / index.df(term))


        #calculate vectors for documents
        self.doc_weight_t = defaultdict(dd)
        self.doc_vec_len = defaultdict(float)

        cnt = 0

        for docID in self.docIDs:
            print("computing vector space for Doc {0}".format(cnt))
            self.doc_vec_len[docID] = 0.
            for term in self.terms:
                #if index.tf(term, docID) and docID == self.docIDs[0]:
                    #print("{0}, {1}, {2}".format(term, docID, index.tf(term, docID)))
                if index.tf(term, docID):
                    self.doc_weight_t[docID][term] = index.tf(term, docID)
                    self.doc_vec_len[docID] += self.doc_weight_t[docID][term]**2
            for term in self.terms:
                if term in self.doc_weight_t[docID]:
                    self.doc_weight_t[docID][term] /= math.sqrt(self.doc_vec_len[docID])
            cnt += 1

    def q_weight_t(self, term):
        term = Index.Index._preprocess(Index.Index, term)
        return self.term_idf[term]

    def d_weight_t(self, docID, term):
        term = Index.Index._preprocess(Index.Index, term)
        if term in self.doc_weight_t[docID]:
            return self.doc_weight_t[docID][term]
        else:
            return 0
