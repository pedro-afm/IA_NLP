import urllib.request
from bs4 import BeautifulSoup
import spacy
from spacy.matcher import PhraseMatcher
from IPython.display import display, HTML

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

token_search = pln(string)

matcher = PhraseMatcher(pln.vocab)
matcher.add('SEARCH', None, token_search)

doc = pln(content)
matches = matcher(doc)
print(matches)
print(doc[3463:3464])

words_number = 50
doc = pln(content)
matches = matcher(doc)

display(HTML(f'<h1>{string.upper()}</h1>'))
display(HTML(f"""<p><strong>Resultados encontrados {len(matches)}</strong></p>"""))

for i in matches:
    begin = i[1] - words_number
    if begin < 0:
        begin = 0
    text += str(doc[begin:i[2] + words_number]).replace(string, f"<mark>{string}</mark>")
    text += "<br/><br/>"
display(HTML(f"""... {text} ..."""))