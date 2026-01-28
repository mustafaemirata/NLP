#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 25 16:12:46 2026

@author: mustafaemirata
"""

import nltk 

#paket
nltk.download("punkt")
nltk.download("punkt_tab")

text="Hello, World! How are you today?"

#kelimeleri tokenlara ayırıyoruz
word_tokens=nltk.word_tokenize(text)
print(word_tokens)

# metni cümlelere ayır
sentence_tokens=nltk.sent_tokenize(text)