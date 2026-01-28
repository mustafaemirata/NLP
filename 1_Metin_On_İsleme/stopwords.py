#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 25 21:40:18 2026

@author: mustafaemirata
"""

import nltk
from nltk.corpus import stopwords
nltk.download("stopwords")

# ingilizce
stop_words_eng= set(stopwords.words("english"))
text="There are some examples of handling stop words from a some texts."
text_list=text.split()
# stop wordslerden arınmış metin
filtered_words=[word for word in text_list if word.lower() not in stop_words_eng]
print(f"filtered_words: {filtered_words}")

#türkçe
stop_words_tr=set(stopwords.words("turkish"))
metin="merhaba arkadaşlar , çok güzel bir ders işliyoruz. Bu ders ve ama "
metin_list=metin.split()
filtered_words_tr=[word for word in metin_list if word.lower() not in stop_words_tr]

#kütüphane kullanmadan yapma

#stop words liste yap

tr_stopwords=["için","bu","ile","mı","mi","special"]
kendi_metnimiz="Deneme metnidir. Bu metin ile birlikte special karakterleri atmalı mı lazım?"
kendi_list=kendi_metnimiz.split()

filtered_words_kendi=[word for word in kendi_list if word.lower() not in tr_stopwords]
print(filtered_words_kendi)

