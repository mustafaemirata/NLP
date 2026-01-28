#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 02:16:53 2026

@author: mustafaemirata
"""
# --- 1. Kütüphaneler ---
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

# Gerekli NLP paketini indir
nltk.download('stopwords')

# --- 2. Veri Yükleme ve Hazırlık ---
df = pd.read_csv("spam.csv", encoding="latin-1")

# Gereksiz boş sütunları at
df = df[['v1', 'v2']]
df.columns = ['label', 'text']

# --- 3. Gelişmiş Metin Temizleme Fonksiyonu ---
def clean_text(text):
    # Küçük harf ve rakam temizliği
    text = str(text).lower()
    text = re.sub(r"\d+", "", text)
    
    # Özel karakter temizliği
    text = re.sub(r"[^\w\s]", "", text)
    
    # Stopwords temizliği 
    stop_words = set(stopwords.words("english"))
    
    # Kelimelere ayır, 2 harften uzun ve stopword olmayanları filtrele
    words = text.split()
    cleaned_words = [w for w in words if len(w) > 2 and w not in stop_words]
    
    # Listeyi tekrar metne (string) çevirerek döndür
    return " ".join(cleaned_words)

#  4. Temizlik İşlemini Uygula ve Yeni DataFrame Oluştur 
print("Metinler temizleniyor, lütfen bekleyin...")
cleaned_list = [clean_text(doc) for doc in df['text']]

# Sadece ihtiyacımız olan sütunlarla tertemiz bir DataFrame
df_clean = pd.DataFrame({
    'cleaned_text': cleaned_list,
    'label': df['label']
})

vectorizer = TfidfVectorizer(max_features=5000) # RAM'i korumak için en iyi 5000 kelime
X = vectorizer.fit_transform(df_clean['cleaned_text'])

# Kelime kümesini al
feature_names = vectorizer.get_feature_names_out()
tfidf_score=X.mean(axis=0).A1.tolist() #her kelimenin tfidf değerleri

#df oluştur
df_tfidf=pd.DataFrame({"word": feature_names, "tfidf_score": tfidf_score})

# sıralama yap

df_tfidf_sort=df_tfidf.sort_values(by="tfidf_score",ascending=False) #büyükten küçüğe sırala
print(df_tfidf_sort.head(10))

