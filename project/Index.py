import nltk
import os
from collections import defaultdict

def dd():
	return defaultdict(int)

class Index(object):
	def __init__(self, path, StopwordRemoval=False, Stemming=False, Debug=False):
		#run in corpus folder
		for root, directories, documents in os.walk(path):
			# filter
			documents = [f for f in documents if f.endswith('.html')]
			# use a small part of the corpus
			if Debug:
				documents = [f for f in documents if int(f.split('.')[0])<1000]

		# build index
		self._documents = documents
		if Debug:
			print('stopword removal:{0}, stemming:{1}'.format(StopwordRemoval, Stemming))
		if StopwordRemoval:
			self._stop = nltk.corpus.stopwords.words('english')
		if Stemming:
			self._stemmer = nltk.PorterStemmer()
		
		#index is a dict of dict
		#self._index = defaultdict(lambda : defaultdict(int))
		self._index = defaultdict(dd)

		for document in documents:
			if Debug:
				print('processing document {0}...'.format(document))
			try:
				'''example of document : 21393.html
				documentID : 21393
				split document name by dot and parse first part as int'''
				documentID = int(document.split('.')[0])
				#read content and tokenization
				content = open(path+'/'+document, errors='ignore')
				raw = content.read()
				raw = raw.lower()
				tokens = nltk.word_tokenize(raw)
				if StopwordRemoval:
					tokens = [token for token in tokens
								if token not in self._stop]

				def StemToken(token):
					return self._stemmer.stem(token)

				if Stemming:
					tokens = map(StemToken(token), tokens)
					#tokens = map(lambda token:self._stemmer.stem(token), tokens)
				'''
				index[token][documentID] -- term frequency -- tf
				size of dict index[token] -- document frequency -- df
				'''
				for token in tokens:
					self._index[token][documentID]+=1
			except Exception as e:
				print('error occur when reading {0}'.format(documentID))
				raise e
			

	def _preprocess(self, term):
		term = term.lower()

		if hasattr(self, '_stemmer'):
			return self._stemmer.stem(term)

		return term

	def tf(self, term, document=None):
		term = self._preprocess(term)
		if document is None:
			if term in self._index:
				return self._index[term]
			else:
				return dd()
		else:
			if term in self._index and document in self._index[term]:
				return self._index[term][document]
			else:
				return 0

	def df(self, term):
		term = self._preprocess(term)
		if term in self._index:
			return len(self._index[term])
		else:
			return 0

	def words(self):
		return self._index.keys()



		