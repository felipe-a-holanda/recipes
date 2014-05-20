#!/usr/bin/env python
import markdown
import codecs
from bs4 import BeautifulSoup
from IPython import embed
fname = 'recipes'
infname = fname+'.txt'
outfname = fname+'.html'

input_file = codecs.open(infname, mode="r", encoding="utf-8")
text = input_file.read()
html = markdown.markdown(text)
soup = BeautifulSoup(html)
with codecs.open(outfname,'w','utf-8') as f:
    print >>f,'<meta charset="utf-8">'
    print >>f,soup.prettify()
