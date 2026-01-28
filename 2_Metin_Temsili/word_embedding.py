#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 22:44:05 2026

@author: mustafaemirata
"""

#kütüphaneler
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA #principle compenent analysis -> verideki boyutu azaltarak veriyi koruyup yeni özellik seti oluşturur.

from gensim.models import Word2Vec,FastText
from gensim.utils import simple_preprocess


#örnek veri seti
sentences=[
    "Köpek çok tatlı bir hayvandır.",
    "Köpekler evcil hayvanlardır.",
    "Kediler genellikle bağımsız hareket etmeyi severler.",
    "Köpekler sadık ve dost canlısı hayvanlardır.",
    "Hayvanlar insanlar için dost canlısı hayvanlardır."
    ]
tokenized_sentences =[simple_preprocess(sentence)for sentence in sentences] # liste return edecek!

# wrod2vec
word2_vec_model=Word2Vec(sentences=tokenized_sentences,vector_size=50,window=5,min_count=1,sg=0)
"""
    sentences -> kullanılacak data set.
    vector_size -> kelimelerin embedding vekötrlerinin boyutu.
    window -> kelime bağlamı oluşturacak kelimelerin max uzuaklğı.
    min_count -> dikkat edilecek kelimelerin min. görülme sayısı.
    sg -> Word2Vec mimarisini belirler , sg= 0 -> kelimenin çevresindeki kelimelerden tahmin eder.
"""

#fasttext
fasttext_model=FastText(sentences=tokenized_sentences,vector_size=50,window=5,min_count=1,sg=0)


#görselleştirme -> PCA


