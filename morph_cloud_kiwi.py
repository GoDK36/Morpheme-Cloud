# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function
from kiwipiepy import Kiwi, Option
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import codecs

tagger = Kiwi()
tagger.prepare()

target_corpus = codecs.open(r'E:\Programming\python\창회선배스터디\Morpheme_Cloud\자료\토지2.txt', 'r', encoding='utf-8')

#텍스트 태깅
tagged_temp = []

for i in target_corpus:
    i = i.strip()
    temp_tagging = [x[0] for x in tagger.analyze(i, top_n=1)]
    inner_temp = ["{}/{}".format(word, tag) for word, tag, score1, score2 in temp_tagging[0]]
    tagged_temp.append(tuple(inner_temp))

tagged_list = []

for i in tagged_temp:
    for j in i:
        if '/V' in j:
            j = j.replace('/VV','다/VV')
            tagged_list.append(j)
        elif '/A' in j:
           j.replace('/VA','다/VA')
           tagged_list.append(j)
        else:
            tagged_list.append(j)

print(tagged_list[:20])

#내용어 리스트 생성
word_freq_Dict = {}
for morph_tag in tagged_list:
    morph = morph_tag.split('/')[0]
    tag = morph_tag.split('/')[1]
    if tag.startswith('N' or 'VV' or 'VA' or 'D'):
        if morph in word_freq_Dict:
            word_freq_Dict[morph] += 1
        else:
            word_freq_Dict[morph] = 1

print(word_freq_Dict)

#폰트 불러오기
# font_path = r'C:\Windows\Fonts\NanumPen.ttf'
wordcloud = WordCloud(font_path=r"C:\WINDOWS\Fonts\HYBDAL.TTF",
    width = 800,
    height = 800,
    background_color="white",
    prefer_horizontal = 0.9999,
    min_font_size = 10)
wordcloud = wordcloud.generate_from_frequencies(word_freq_Dict)

#이미지 사이즈
fig = plt.figure(figsize=(12,12))

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()