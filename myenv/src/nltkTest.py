import nltk
import bs4 as bs
import urllib.request
import spacy

nltk.download('rslp')

pln = spacy.load('pt_core_news_sm')

document = pln('Estou aprendendo processamento de linguagem natural, curso em Braganca')

stemmer = nltk.stem.RSLPStemmer()
stemmer.stem('aprender')

for token in document:
    print(token.text, token.lemma_, stemmer.stem(token.text))