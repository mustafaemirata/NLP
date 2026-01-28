#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 02:04:04 2026

@author: mustafaemirata
"""

#import library
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
#örnek oluştur
documents=[
    "Köpek çok tatlı bir hayvandır.",
    "Köpek ve kuşlar çok tatlı hayvanlardır.",
    "Inekler süt üretirler"
    ]


#vectorizer
tfidf_vectorizer=TfidfVectorizer()


#metni sayısala çevir
X=tfidf_vectorizer.fit_transform(documents)

#kelime kümesini incele -> her kelimeyi çantaya aktarmak gibi
feature_names=tfidf_vectorizer.get_feature_names_out()

#vektör temsili incele
vektor_temsili=X.toarray()
print(f"td-idf: {vektor_temsili}")
df_tfidf=pd.DataFrame(vektor_temsili,columns=feature_names)

#ortalama td_idf değerlerini incele
tf_idf=df_tfidf.mean(axis=0)

#tf-idf yüksekse çok yerde geçiyordur