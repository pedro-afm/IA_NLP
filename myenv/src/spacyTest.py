import bs4 as bs
import spacy

pln = spacy.load('pt_core_news_sm')

document = pln('Estou aprendendo processamento de linguagem natural, curso em Braganca')

for token in document:
    print(token.text, token.pos_)

# Changing aprendendo to the verb aprender
for token in document:
    print(token.text, token.lemma_)

doc = pln('encontrei encontraram encontrarao encontrariam cursando curso cursei')

# Changing aprendendo to the verb aprender
for token in doc:
    print(token.text, token.lemma_)