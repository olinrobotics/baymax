from nltk import *

script = open("big_hero_6.txt", "rU")
script = script.read()
sentences = sent_tokenize(script)
words = word_tokenize(sentences)
text = nltk.Text(words)
text.genertate()
