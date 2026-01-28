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
def plot_word_embedding(model,title):
    word_vectors=model.wv
    
    words=list(word_vectors.index_to_key)[:1000]
    vectors=[word_vectors[word] for word in words]
    
    #PCA
    pca=PCA(n_components=3) #kaç boyutlu olacak -> 50'den 3 boyutluya indirme
    reduced_vectors=pca.fit_transform(vectors)
    
    #3d görselleştirme
    
    fig=plt.figure(figsize=(12,10))
    ax=fig.add_subplot(111,projection="3d")
    
    #vekötr çizdir
    ax.scatter(reduced_vectors[:,0],reduced_vectors[:,1],reduced_vectors[:,2])
    
    #kelimeleri etiketle
    for i, word in enumerate(words):
        ax.text(reduced_vectors[i,0],reduced_vectors[i,1],reduced_vectors[i,2],word, fontsize=12)
        
    ax.set_title(title)
    ax.set_xlabel("PC -1")
    ax.set_ylabel("PC -2")
    ax.set_zlabel("PC -3")
plot_word_embedding(word2_vec_model, "Word2vec")
plot_word_embedding(fasttext_model, "FastText")
    
    
    
    
    
    
    
    
    
    
    


