from kiwipiepy import Kiwi, Option
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter, defaultdict
import codecs

tagger = Kiwi()
tagger.prepare()

# def flat(content):
#     return ["{}/{}".format(word,tag) for word, tag in tagger.pos(content)

rsc = r'E:\Programming\python\창회선배스터디\Morpheme_Cloud\자료\토지2.txt'

target_corpus = codecs.open(rsc, 'r', encoding='utf-8')

#텍스트 태깅 작업
tagged_temp = []

# with open(rsc, 'r', encoding="utf8") as kr_f:
#     for line in kr_f:
#         line = line.strip()
#         tagged_temp += flat(line)

for i in target_corpus:
    i = i.strip()
    temp_tagging = [x[0] for x in tagger.analyze(i, top_n=1)]
    inner_temp = ["{}/{}".format(word, tag) for word, tag, score1, score2 in temp_tagging[0]]
    tagged_temp.append(tuple(inner_temp))

print(tagged_temp[:3])

tagged_list = []

# for i in tagged_temp:
#     if '/V' in i:
#         i = i.replace('/V','다/V')
#         tagged_list.append(tuple(i.split('/')))
#     elif '/A' in i:
#         i.replace('/A','다/A')
#         tagged_list.append (tuple (i.split ('/')))
#     else:
#         tagged_list.append(tuple(i.split('/')))

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

print(tagged_list[:30])

#내용어 리스트 생성
word_freq_d = defaultdict(int)
# tag_match = re.compile('\S+[NVAD]S')
for lst in tagged_list:
    morph = lst.split('/')[0]
    tag = lst.split('/')[1]
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
# wordcloud = WordCloud(font_path = font_path,
#     width = 800,
#     height = 800,
#     background_color="white",
#     prefer_horizontal = 0.9999,
#     min_font_size = 10)

#이미지 사이즈
fig = plt.figure(figsize=(12,12))

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
