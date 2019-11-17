import multidict as multidict

import os
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

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

rsc = r'E:\Programming\python\창회선배스터디\Morpheme_Cloud\자료'

text = open(path.join(rsc, '토지2.txt'), encoding='utf-8')
text = text.read()
txt = freq_dict(text)

star_mask = np.array(Image.open(r"E:\Programming\python\창회선배스터디\Morpheme_Cloud\자료\star_mask.png"))

wc = WordCloud(font_path=r"C:\WINDOWS\Fonts\HYBDAL.TTF",
		     width=400,
		     height=200,
		     prefer_horizontal=0.9999,
		     mask = star_mask,
		     background_color = "white",
		     min_font_size = 1
)
wc.generate_from_frequencies(txt)

fig = plt.figure(figsize=(12,12))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()