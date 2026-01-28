#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 25 16:56:49 2026

@author: mustafaemirata
"""

import nltk
nltk.download("wordnet") #lemmatization
from nltk.stem import PorterStemmer #stemming

#nesne oluştur

stemmer=PorterStemmer()

words=["running","runner","ran","runs","better","go","went"]

stems=[stemmer.stem(w) for w in words] # listede tarayarak fonksiyonu uygulayıp kök bulma işlemi

print(f"Stem: {stems}")

#lemmatization
from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
words=["running","runner","ran","runs","better","go","went"]

lemmas=[lemmatizer.lemmatize(w,pos="v")   for w in words]  #verb olarak işlemesini istedik verblerin anlamlı işlevsel kökleri
print(f"Lemas: {lemmas}")
