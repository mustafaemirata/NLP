#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 25 15:42:56 2026

@author: mustafaemirata
"""
import string #noktalama
import re #özel karakter
from textblob import TextBlob
from bs4 import BeautifulSoup


# ham metin -> parçalara ayırıp aralarına bir boşluk ekledik.
text="Hello,      World?       2026"
text.split()
cleaned_text1=" ".join(text.split())

# büyükten küçüğe harf çevrimi
text="Hello, World? 2026"
cleaned_text2=text.lower()


# noktalama işaretlerini kaldırma -> noktalama işaretlerini "" ile değiştirdik
text="Hello, World? 2026"
cleaned_text3=text.translate(str.maketrans("","",string.punctuation))
print(cleaned_text3)

# özel karakterleri kaldır.
text="Hello, World? 2026"
cleaned_text4 = re.sub(r"[^A-Za-z0-9\s]", "", text) # AZaz09a kalsın, boşlukla değiştir, text
print(cleaned_text4)


# yazım hataları
text="Hella, Wirld? 2026"
cleaned_text5=str(TextBlob(text).correct())

# HTML URL
html_text="<div>Hello, World? 2026</div>"
cleaned_text6=BeautifulSoup(html_text,"html.parser").getText()
print(cleaned_text6)
