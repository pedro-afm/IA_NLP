import urllib.request
from bs4 import BeautifulSoup
import spacy
from spacy.matcher import PhraseMatcher
from IPython.display import display, HTML
import webbrowser

text = ''

# Loading file from browser
dados = urllib.request.urlopen('https://pt.wikipedia.org/wiki/Intelig%C3%AAncia_artificial')

# Reading all variable
dados = dados.read()

# Parsing variable content
dados_html = BeautifulSoup(dados, 'html.parser')

# Taking only the text inside the file between tags <p>
paragrafos = dados_html.find_all('p')

content = ''

# Transforming all paragraphs into 1 with all content
for p in paragrafos:
    content += p.text

# Lower case to facilitate the IA reading
content = content.lower()

# importing portuguese language
pln = spacy.load("pt_core_news_sm")

# The word to be searched inside all text
string = 'turing'

# Setting the token word inside the vocabulary
token_search = pln(string)

# Setting up the methods
matcher = PhraseMatcher(pln.vocab)
matcher.add('SEARCH', None, token_search)

# Finding the word inside the text
doc = pln(content)
matches = matcher(doc)

words_number = 50

# Creating a HTML document with the results and phrases surround
# marked to note it better
with open('output.html', 'w') as f:
    f.write(f'<h1>{string.upper()}</h1>')
    f.write(f'<p><strong>Resultados encontrados {len(matches)}</strong></p>')
    for i in matches:
        begin = i[1] - words_number
        if begin < 0:
            begin = 0
        text += str(doc[begin:i[2] + words_number]).replace(string, f"<mark>{string}</mark>")
        text += "<br/><br/>"
    f.write(text)

webbrowser.open('output.html')