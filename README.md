# ZJU Information Retrieval 2016 Final Project

## Setup Steps:

### 1. install nltk & ntlk data

nltk:

``sudo pip install -U nltk``

nltk data:

``import nltk``

``nltk.download()``

and then pick **punkt** and **stopwords** to install

result: ![nltk_package](nltk_package.png)

references:

http://www.nltk.org/install.html

http://www.nltk.org/data.html

### 2. Test

run index_example.py

```python index_example.py```

## Vector Space Specifications:

Use pickle to read ``space.pickle`` to obtain a VectorSpace object

The VectorSpace class is defined in VectorSpace.py

It provides with two methods:

```q_weight_t(term)``` to get the idf of a term

```d_weight_t(self, docID, term)``` to get the normalized term weight for a term in a doc

Examples in ```space_example.py```
## Score Sort Specifications:

The ScoreSort is defined in ScoreSort.py

It provides with one method:

```sort(query,K)``` to get a list of (docID, score) after sorting. query is a list of terms, and K indicates top K

Examples in ```scoresort_example.py```


