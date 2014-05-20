import codecs
from bs4 import BeautifulSoup
from IPython import embed

soup = BeautifulSoup(codecs.open('data/recipes.html','r','utf8').read())
embed()
