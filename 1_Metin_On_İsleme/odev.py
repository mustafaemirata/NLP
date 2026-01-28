#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 25 22:12:19 2026

@author: mustafaemirata
"""

import nltk
import string
import re
from textblob import TextBlob
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download("punkt")
nltk.download("wordnet")
nltk.download("stopwords")
nltk.download("punkt_tab")

raw_html = "<div>Merhaba! Bu bir NLP projesidir... 2026'da başarılar dilerim.</div>"
soup = BeautifulSoup(raw_html, "html.parser").get_text()
clean_step2 = " ".join(soup.lower().split())
clean_step3 = re.sub(r"[^a-zA-ZğüşıöçĞÜŞİÖÇ\s]", "", clean_step2)

print(f"Temiz Metin: {clean_step3}")

tokens = word_tokenize(clean_step3)
print(f"Tokenlar: {tokens}")

tr_stop_list = set(stopwords.words("turkish"))
extra_stops = {"özel", "projesidir"} 
full_stop_words = tr_stop_list.union(extra_stops)

filtered_words = [w for w in tokens if w not in full_stop_words]
print(f"Filtrelenmiş: {filtered_words}")

stemmer = PorterStemmer()
eng_words = ["running", "runner", "runs", "ran"]
stems = [stemmer.stem(w) for w in eng_words]

lemmatizer = WordNetLemmatizer()
lemmas = [lemmatizer.lemmatize("running", pos="v"), lemmatizer.lemmatize("ran", pos="v")]

print(f"Stemming: {stems}")
print(f"Lemmatization: {lemmas}")