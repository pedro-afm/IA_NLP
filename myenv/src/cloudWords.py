from matplotlib.colors import ListedColormap
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import urllib.request
from bs4 import BeautifulSoup
import spacy
from spacy.matcher import PhraseMatcher
from IPython.display import display, HTML
from spacy import displacy
import webbrowser
from spacy.lang.pt.stop_words import STOP_WORDS

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

lista_token = []

# Passing each word inside doc to a list of words
for token in doc:
    lista_token.append(token.text)

no_stop = []

# Passing only important words, taking off for instance "de", "onde"
for word in lista_token:
    if pln.vocab[word].is_stop == False:
        no_stop.append(word)

# Configuring the map colors
color_map = ListedColormap(['orange', 'green', 'red', 'magenta'])

cloud = WordCloud(background_color = 'white', max_words = 100, colormap = color_map)

# Transforming the list into a string separating each word with a space
cloud = cloud.generate(' '.join(no_stop))

plt.figure(figsize=(10,10))
plt.imshow(cloud)
plt.axis('off')

plt.show()