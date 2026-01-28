#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 01:03:29 2026

@author: mustafaemirata
"""

#library
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import re #-> metin temizliği
from collections import Counter
import nltk
from nltk.corpus import stopwords


#dataset aktar
df=pd.read_csv("IMDB Dataset.csv")

#metin verilerini al
documents=df["review"] #inceleme yazısını dokümana kaydet
labels=df["sentiment"] #cümlenin etiketi pozitif mi negatif mi?


# metin temizliği
def clean_text(text):
    #büyük küçük harf 
    text=text.lower()
    
    #rakam temizliği
    text=re.sub(r"\d+", "", text)
    
    #özel karakter kaldır
    text=re.sub(r"[^\w\s]", "", text)
    
    
    #kısa kelime temizliği -> I,in there... (anlamsız olanlar)
    text=" ".join([word for word in text.split() if len(word)>2])
    
    #stopword temizliği
    stopwords_eng=set(stopwords.words("english"))
    text_list=text.split()
    text=[word for word in text_list if word not in stopwords_eng]
    
    #sonda temizlenmiş texti return et
    return " ".join(text) 
# metinleri temizle
cleaned_doc=[clean_text(row) for row in documents]

#bow

#vectorizer
vectorizer=CountVectorizer()

#sayısala çevir -> ilk 400 yorumu inceleyelim.
X=vectorizer.fit_transform(cleaned_doc[:400])

#kelime kümesi
feature_names=vectorizer.get_feature_names_out()


#vektör temsili
vektor_temsili2=X.toarray()
print(f"Vektor temsili: {vektor_temsili2}")

df_bow=pd.DataFrame(vektor_temsili2,columns=feature_names)

#kelime frekansı -> Hangi kelimeden kaç tane var
word_counts=X.sum(axis=0).A1.tolist()
word_freq=dict(zip(feature_names,word_counts))


#ilk 5 kelime
most_common_5_words=Counter(word_freq).most_common(5)
print(f"most_common_5_words: {most_common_5_words}")


#ÖDEV -> sopword çıkarılacak. -> TAMAMLANDI

