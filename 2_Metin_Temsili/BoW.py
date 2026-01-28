#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 25 22:29:30 2026

@author: mustafaemirata
"""

#count vectorizer
from sklearn.feature_extraction.text import CountVectorizer


#dataset 
documnets=[
    "kedi bahçede",
    "kedi evde"
    
    ]

#vectorizer tanımlaması
vectorizer=CountVectorizer()

#metni sayısal vektöre çevir
X=vectorizer.fit_transform(documnets)

#inceleme ve vekötr temsili -> bahçede , evde , kedi
feature_names=vectorizer.get_feature_names_out() #küme oluşturma
print(f"kelime kümesi: {feature_names}")


#vektör temsili
vektor_temsili=X.toarray()
print(f"vektör temsili: {vektor_temsili}")


