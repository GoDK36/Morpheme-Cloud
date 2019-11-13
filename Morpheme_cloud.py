from konlpy.tag import Kkma
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter, defaultdict
import re

tagger = Kkma()

def flat(content):
    return ["{}/{}".format(word,tag) for word, tag in tagger.pos(content)]

rsc = r'D:\Programming\python\창회선배스터디\Morpheme_Cloud\자료\토지2.txt'

#텍스트 태깅 작업
tagged_list = []
with open(rsc, 'r', encoding="utf8") as kr_f:
    for line in kr_f:
        line = line.strip()
        tagged_list += flat(line)

for i in tagged_list:
    if '/V' in i:
        i = i.replace('/V','다/V')
        tagged_list.append(tuple(i.split('/')))
    elif '/A' in i:
        i.replace('/A','다/A')
        tagged_list.append(tuple(i.split('/')))
    else:
        tagged_list.append(tuple(i.split('/')))

#내용어 리스트 생성
word_freq_d = defaultdict(int)
# tag_match = re.compile('\S+[NVAD]S')
for morph, tag in tagged_list:
    if tag.startswith('N'):
        word_freq_d[morph] += 1
    elif tag.startswith('V'):
        word_freq_d[morph] += 1
    elif tag.startswith('A'):
        word_freq_d[morph] += 1
    elif tag.startswith('D'):
        word_freq_d[morph] += 1

#폰트 불러오기
wordcloud = WordCloud(font_path=r"C:\WINDOWS\Fonts\HYBDAL.TTF")
wordcloud = wordcloud.generate_from_frequencies(word_freq_d)

#이미지 사이즈
fig = plt.figure(figsize=(12,12))

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
