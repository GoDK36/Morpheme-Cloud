import multidict as multidict

import numpy as np

import os
import re
from PIL import Image
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def freq_dict(sentence):
    fullTermsDict = multidict.MultiDict()
    tmpDict = {}

    # making dict for counting frequencies
    for text in sentence.split(" "):
        val = tmpDict.get(text, 0)
        tmpDict[text] = val + 1
    for key in tmpDict:
        fullTermsDict.add(key, tmpDict[key])
    return fullTermsDict

rsc = r'D:\Programming\python\창회선배스터디\Morpheme_Cloud\자료'

text = open(path.join(rsc, '토지2.txt'), encoding='utf-8')
text = text.read()
txt = freq_dict(text)
wc = WordCloud(font_path=r"C:\WINDOWS\Fonts\HYBDAL.TTF",
               background_color="white",
               max_words=500,
               # mask=alice_mask, 워드클라우드의 형태
               width=800,
               height = 800,
               # prefer_horizontal = 0.9999,
               # min_font_size = 20,
               # max_font_size= 60,
               #stopwords=stopwords  불용어 처리
               )
wc.generate_from_frequencies(txt)

fig = plt.figure(figsize=(12,12))

plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()