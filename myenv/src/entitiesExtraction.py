
import urllib.request
from bs4 import BeautifulSoup
import spacy
from spacy.matcher import PhraseMatcher
from IPython.display import display, HTML
from spacy import displacy
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

for entity in doc.ents:
    print(entity.text, entity.label_)

# Rendering named entities and saving into a file
with open('entityOutput.html', 'w') as f:
    html_content = displacy.render(doc, style='ent', jupyter=False)
    f.write(html_content)

# Opening the HTML file in a web browser
webbrowser.open('entityOutput.html')