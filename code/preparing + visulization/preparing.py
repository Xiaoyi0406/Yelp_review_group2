#!/usr/bin/env python
# coding: utf-8

# In[66]:


#read the subdataset 
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.corpus import stopwords
import string
import math
#read the data
def read_data(nrow, filepath):
    
    with open(filepath) as f:
        temp = f.readline()
        temp = json.loads(temp.rstrip())
        tdata = pd.DataFrame(temp, index = [0])
        for n in range(1,nrow):
            temp = json.loads(f.readline().rstrip())
            tdata = tdata.append(pd.DataFrame(temp, index = [n]))
    return tdata

#data_df = read_data(10000, '/Users/kzhao46/Downloads/628-2/data/review_train.json')
#data_df=pd.read_csv('/Users/kzhao46/Dropbox/628-2/data/Sw.csv',delimiter=',')
#data=data_df[data_df['circle']==1]
#data.to_csv('/Users/kzhao46/Dropbox/628-2/data/swin.csv', index = False, encoding='utf-8')


# In[26]:


import pandas as pd
Mc =  pd.read_csv('/Users/kzhao46/Dropbox/628-2/data/McDonalds.csv',delimiter=',')
data_df=Mc


# In[ ]:





# In[27]:


print("Shape of the dataset:")
print(data_df.shape)


# In[ ]:





# In[28]:


print("Column names:")
print(data_df.columns)


# In[29]:


print("Datatype of each column:")
print(data_df.dtypes)


# In[30]:


print("Few dataset entries:")
data_df.head()


# In[31]:


#create a new column for the number of words in text
data_df['length'] = data_df['text'].apply(len)
data_df.head()


# In[32]:


#cor stars vs length
graph = sns.FacetGrid(data=data_df,col='stars')
graph.map(plt.hist,'length',bins=50,color='blue')


# In[33]:


#language
#extract the comments do not have language
import re
from langdetect import detect
def not_lang(text):
    text = re.sub('(?::|;|=)(?:-)?(?:\)|\(|D|P)','',text)
    if re.sub('[\W]+','',text) == '':
        return True
    else:
        return False
temp=data_df[data_df['text'].apply(not_lang)].index.values
data_df.loc[temp,'lang_type'] = 'en'
from langdetect import detect
for i in range(data_df.shape[0]):
    if i in temp:
        continue
    else:
        data_df.loc[i,'lang_type'] = detect(data_df['text'][i])
#translate the language
data_df['lang_type'].describe()
data_df=data_df[data_df['lang_type']=='en']
data_df.


# In[34]:



from googletrans import Translator
translator = Translator()
#data_df['lang_type'].describe(include=['O'])
c='你好'
c.encode('utf8')
translator.translate(c).text
#from translate import Translator
#translator= Translator(to_lang="German")
#translator.translate('你好')


# In[35]:


#import nltk
#nltk.download()


# In[36]:


# correct acronym
import re

data_df['text']=data_df['text'].apply(lambda sen: re.sub(r"can\'t", "can not", sen))
data_df['text']=data_df['text'].apply(lambda sen: re.sub(r"cannot", "can not ", sen))
data_df['text']=data_df['text'].apply(lambda sen: re.sub(r"what\'s", "what is", sen))
data_df['text']=data_df['text'].apply(lambda sen: re.sub(r"\'ve ", " have ", sen))
data_df['text']=data_df['text'].apply(lambda sen: re.sub(r"n\'t", " not ", sen))
data_df['text']=data_df['text'].apply(lambda sen: re.sub(r"i\'m", "i am ", sen))
data_df['text']=data_df['text'].apply(lambda sen: re.sub(r"\'re", " are ", sen))
data_df['text']=data_df['text'].apply(lambda sen: re.sub(r"\'d", " would ", sen))
data_df['text']=data_df['text'].apply(lambda sen: re.sub(r"\'ll", " will ", sen))


# In[37]:


#takes to long time to correct the spelling error
#from textblob import TextBlob 
#data_df['text'][:20]=data_df['text'].apply(lambda x: str(TextBlob(x).correct()))


# In[38]:


'''
#the frist step to get the dict
data_dict=data_df

data_dict['text'] = data_dict['text'].apply(lambda x: x.lower())
#remove the punctuation
#data_dict['text'] = data_dict['text'].apply(lambda x: ''.join([c for c in x if c not in punctuation]))
'''


# In[39]:


'''
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

stop_words = set(stopwords.words('english')) 
import nltk 
from nltk import *
data_dict['NN'] =None
data_dict['JJ']=None
data_dict['RB']=None

import numpy as np
def detect(text):
    NN = []
    JJ = []
    RB = []
    text =  word_tokenize(text)
    temp = nltk.pos_tag(text)
    i = 0
    for word, tag in temp:
        if word in stop_words:
            continue
        if re.match('JJ[*]?', tag) != None:
            JJ.append(word)
        if re.match('NN[*]?', tag) != None:
            NN.append(word)
        if re.match('RB[*]?', tag) != None:
            RB.append(word)
    return list([NN, JJ, RB])

temp = pd.DataFrame(list(data_dict['text'].apply(detect)))
data_dict['NN'], data_dict['JJ'], data_dict['RB'] = temp[:][0], temp[:][1], temp[:][2]
'''


# In[12]:


'''data_dict.head()


# In[13]:


#star1=data_dict[data_dict['stars']==1]
#star2=data_dict[data_dict['stars']==2]
#star3=data_dict[data_dict['stars']==3]
#star4=data_dict[data_dict['stars']==4]
#star5=data_dict[data_dict['stars']==5]
#star1.to_csv('/Users/kzhao46/Dropbox/628-2/data/s1.csv', index = False, encoding='utf-8')
#star2.to_csv('/Users/kzhao46/Dropbox/628-2/data/s2.csv', index = False, encoding='utf-8')
##star3.to_csv('/Users/kzhao46/Dropbox/628-2/data/s3.csv', index = False, encoding='utf-8')
##star5.to_csv('/Users/kzhao46/Dropbox/628-2/data/s5.csv', index = False, encoding='utf-8')


# In[14]:


'''
s1 =  pd.read_csv('/Users/kzhao46/Dropbox/628-2/data/s1.csv',delimiter=',')
s1.head()
'''


# In[ ]:


'''
NN = []
for item in data_dict['NN']:
    NN += item
#count the words
from collections import Counter

words=NN
# words wrong datatype
counts = Counter(words)
vocab = sorted(counts, key=counts.get, reverse=True)
vocab_to_int_n = {word: ii for ii, word in enumerate(vocab, 1)}

reviews_ints_n = []
reviews_ints_n.append([vocab_to_int_n[word] for word in NN])
print('Unique words: ', len((vocab_to_int_n)))
use=dict(counts.most_common(60))
use()
'''


# In[ ]:





# In[ ]:


'''
use
name=[]
rate=[]
for key in use:
    name.append(key)
    rate.append(use[key]/10)
'''


# In[ ]:


'''
JJ = []
for item in data_dict['JJ']:
    JJ += item
#count the words
from collections import Counter

words=JJ
# words wrong datatype
counts = Counter(words)
vocab = sorted(counts, key=counts.get, reverse=True)
vocab_to_int_j = {word: ii for ii, word in enumerate(vocab, 1)}

reviews_ints_j = []
reviews_ints_j.append([vocab_to_int_j[word] for word in JJ])
#常见J
print('Unique words: ', len((vocab_to_int_j)))
counts.most_common(100)
'''


# In[ ]:


'''
#####################
RB = []
for item in data_dict['RB']:
    RB += item
#count the words
from collections import Counter

words=RB

# words wrong datatype
counts = Counter(words)
vocab = sorted(counts, key=counts.get, reverse=True)
vocab_to_int_r = {word: ii for ii, word in enumerate(vocab, 1)}
#常见R
print('Unique words: ', len((vocab_to_int_r)))
counts.most_common(20)

reviews_ints_r = []
reviews_ints_r.append([vocab_to_int_r[word] for word in RB])
'''


# In[ ]:





# In[ ]:


'''
plt.style.use('ggplot')
tt = ' '.join(NN)
np.random.seed(321)
sns.set(rc={'figure.figsize':(14,8)})
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
wordcloud = WordCloud(background_color="white").generate(tt)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.margins(x=0, y=0)
plt.title('Reviews',size=20)
plt.show()
'''


# In[ ]:


'''
plt.style.use('ggplot')
tt = ' '.join(JJ)
np.random.seed(321)
sns.set(rc={'figure.figsize':(14,8)})
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
wordcloud = WordCloud(background_color="white").generate(tt)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.margins(x=0, y=0)
plt.title('Reviews',size=20)
plt.show()
'''


# In[ ]:


'''
plt.style.use('ggplot')
tt = ' '.join(RB)
np.random.seed(321)
sns.set(rc={'figure.figsize':(14,8)})
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
wordcloud = WordCloud(background_color="black").generate(tt)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.margins(x=0, y=0)
plt.title('Reviews',size=20)
plt.show()
'''


# In[ ]:





# In[15]:


'''
#Lemmatization 改到放最后
nltk.download('wordnet')
from nltk.stem.wordnet import WordNetLemmatizer

#Reduce the word to their root form (eg. ones->one)
data_df['text']=data_df['text'].apply(lambda sen: [WordNetLemmatizer().lemmatize(x) for x in sen.split()])
'''


# In[40]:


#but & although
#built the dictionary called but and although
#but=['but','however','yet','nonetheless','whereas','nevertheless']
#although=['although','though','notwithstanding','albeit','withal','natheless']
'''
text =  word_tokenize("The food is really great.")
nltk.pos_tag(text)
'''


# In[41]:


'''
text =  word_tokenize("The food is really bad.")
nltk.pos_tag(text)
'''


# In[42]:



'''text =  word_tokenize("The food is the  best.")
nltk.pos_tag(text)
'''


# In[16]:


#'''
'''
import nltk 
from nltk import *
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
dic=["bathroom"]
def dic_detect(text):
    s = []
    i = 0
    text =  word_tokenize(text)
    temp = nltk.pos_tag(text)
    for word,tag in temp:
        if i>=1:
            if re.match('JJ[*]?', temp[i-1][1]) and word in dic :
                s.append((temp[i-1][0], word,"None"))
            if word in dic and re.match('JJ[*]?', temp[i-1][1]) != None :
                s.append((word,temp[i-1][0],"None"))
        
        if i>=2:
            if  re.match('RB[*]?', temp[i-2][1]) != None and re.match('JJ[*]?', temp[i-1][1]) != None and word in dic:
                s.append((word,temp[i-1][0], temp[i-2][0]))
            if   temp[i-2][0] in dic and re.match('RB[*]?', temp[i-1][1]) != None and re.match('JJ[*]?', tag) != None:
                s.append((temp[i-2][0], word, temp[i-1][0]))
        if i>=2:
            if temp[i-2][0] in dic and re.match('VB[*]?', temp[i-1][1]) != None and re.match('JJ[*]?', tag) != None:
                s.append((temp[i-2][0],  word,'None'))
        if i>=3:
            if  temp[i-3][0] in dic and re.match('VB[*]?', temp[i-2][1]) != None and re.match('RB[*]?', temp[i-1][1]) != None and re.match('JJ[*]?', tag) != None:
                s.append((temp[i-3][0],  word, temp[i-1][0]))
        if i>=4:
            if temp[i-4][0] in dic and re.match('VB[*]?', temp[i-3][1]) != None and re.match('RB[*]?', temp[i-2][1]) != None and re.match('RB[*]?', temp[i-1][1]) != None and re.match('JJ[*]?', tag) != None:
                s.append((temp[i-4][0], word, temp[i-2][0] +  ' ' + temp[i-1][0]))
        i  = i + 1
    return s

data_df.head()
'''


# In[46]:


'''
data_df['JJ'] = None
data_df['NN'] = None
data_df['RB'] = None
data_df['use']=None
#data_df[]

data_df['use']=data_df['text'].apply(lambda word: ' '.join(word))
'''


# In[47]:



'''#' '.join(data_df['text'])
data_df.head()
data_df['detect'] = data_df['use'].apply(lambda sen: dic_detect(sen))
'''


# In[ ]:


'''
data_df.head()
data_df['NN'] = data_df['detect'].apply(lambda sen: [x[0] for x in sen])
data_df['JJ'] = data_df['detect'].apply(lambda sen: [x[1] for x in sen])
data_df['RB'] = data_df['detect'].apply(lambda sen: [x[2] for x in sen])
data_df.head()
flag = []
for i in range(len(data_df)):
    if data_df['detect'][i]==[]:
        flag.append(False)
    else:
        flag.append(True)
toilet = data_df[flag]
s1=toilet[toilet['stars']==5]
len(s1)
s1#1-2 never clean,limited,horrid,moldy,filthy,unclean,dirty,gross,bad,egregious,atrocious,terrible,messy,homeless,worse
#6/36 无发判断，lady， public，most
#3 clean quick 4/10
##too little gross unairconditioned dirty 6/10
# 4-5 ultra-modern [clean glamorous nice quick 13/17 ####separate free ] 
#3/17### dirtiest(comes from questioned review)1/17
'''


# In[437]:





# In[48]:


'''
import nltk 
from nltk import *
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
def recommondation(text):
    s = []
    i = 0
    text =  word_tokenize(text)
    temp = nltk.pos_tag(text)
    for word,tag in temp:
        if i>=1:
            if re.match('JJ[*]?', tag) != None and re.match('NN[*]?', temp[i-1][1]) != None :
                s.append((temp[i-1][0], word,"None"))
            if re.match('NN[*]?', tag) != None and re.match('JJ[*]?', temp[i-1][1]) != None :
                s.append((word,temp[i-1][0],"None"))
        
        if i>=2:
            if  re.match('RB[*]?', temp[i-2][1]) != None and re.match('JJ[*]?', temp[i-1][1]) != None and re.match('NN[*]?', tag) != None:
                s.append((word,temp[i-1][0], temp[i-2][0]))
            if  re.match('NN[*]?', temp[i-2][1]) != None and re.match('RB[*]?', temp[i-1][1]) != None and re.match('JJ[*]?', tag) != None:
                s.append((temp[i-2][0], word, temp[i-1][0]))
        if i>=2:
            if re.match('NN[*]?', temp[i-2][1]) != None and re.match('VB[*]?', temp[i-1][1]) != None and re.match('JJ[*]?', tag) != None:
                s.append((temp[i-2][0],  word,'None'))
        if i>=3:
            if re.match('NN[*]?', temp[i-3][1]) != None and re.match('VB[*]?', temp[i-2][1]) != None and re.match('RB[*]?', temp[i-1][1]) != None and re.match('JJ[*]?', tag) != None:
                s.append((temp[i-3][0],  word, temp[i-1][0]))
        if i>=4:
            if re.match('NN[*]?', temp[i-4][1]) != None and re.match('VB[*]?', temp[i-3][1]) != None and re.match('RB[*]?', temp[i-2][1]) != None and re.match('RB[*]?', temp[i-1][1]) != None and re.match('JJ[*]?', tag) != None:
                s.append((temp[i-4][0], word, temp[i-2][0] +  ' ' + temp[i-1][0]))
        i  = i + 1
    return s
#(NN,JJ,RB)
# 需要的词义信息
# FW foreign word
# CC 并列连词
# IN 介词或者从属连词
# JJ，JJR， JJS 形容词 比较级，最高级
# NN NNS NNP NNPS 名词 复数名词 专有名词 复数专有
# RB RBR RBS 副词 比较级 最高级
# SYM 符号  
# VB VBD VBG VBN VBP VBZ 动词
```
'''


# In[49]:


recommondation('"bathroom is really clean"')


# In[53]:


data_df['JJ'] = None
data_df['NN'] = None
data_df['RB'] = None
data_df['recommondation'] = data_df['text'].apply(lambda sen: recommondation(sen))


# In[54]:


data_df['NN'] = data_df['recommondation'].apply(lambda sen: [x[0] for x in sen])
data_df['JJ'] = data_df['recommondation'].apply(lambda sen: [x[1] for x in sen])
data_df['RB'] = data_df['recommondation'].apply(lambda sen: [x[2] for x in sen])


# In[1]:


data_df.head(10)


# In[70]:


import csv
import pandas as pd
data_df.to_csv('/Users/kzhao46/Dropbox/628-2/data/Mc_use.csv', index = False, encoding='utf-8')


# In[ ]:





# In[ ]:





# In[ ]:


#去掉常用无用词
#去掉或替换不常用词


# In[ ]:


'''
#常见
print('Unique words: ', len((vocab_to_int)))
counts.most_common(20)
'''


# In[ ]:


'''#
freq = pd.Series(' '.join(data_df['text']).split()).value_counts()[-20:]
freq
'''


# In[ ]:





# In[ ]:





# In[ ]:


'''
text = 'she is beatiful, kangyi is so cute, although kangyi is bad'
text =  word_tokenize(text)
temp = nltk.pos_tag(text)
temp
import string
print(string.punctuation)
print(although)
print(but)
re.match('[,.?]', ',')
'''


# In[ ]:


'''
dict = ['kangyi']
def store_nearby(text):
    s = []
    i = 0
    text =  word_tokenize(text)
    temp = nltk.pos_tag(text)
    for word,tag in temp:
        if word in dict:
            left  =  max(0, i-4)
            right = min(len(temp), i+5)
            near = []
            for j in range(left, right):
                if j == i:
                    near.append(temp[j][0])
                    continue 
                print((temp[j][0], temp[j][1]))
                if re.match('JJ[*]?',temp[j][1])!=None or re.match('RB[*]?', temp[j][1])!=None or re.match('IN', temp[j][1]):
                    near.append(temp[j][0])
            print (near)
            s.append(near)
        i += 1
    return s
    '''


# In[ ]:


'''
store_nearby('she is beatiful, kangyi is so cute, although kangyi is bad')
'''


# In[ ]:


'''
def turn(text):
    s = []
    i = 0
    text =  word_tokenize(text)
    temp = nltk.pos_tag(text)
    l = len(temp)
    for i in range(0, l):
        if temp[i][0] in although:
            left = i
            flag = 2
            near = []
            for right in range(left, l):
                if re.match('[,.!?;]', temp[right][0]) != None:
                    flag -= 1
                if flag == 0:
                    break
            for j in range(left, right):
                if re.match('JJ[*]?',temp[j][1])!=None or re.match('RB[*]?', temp[j][1])!=None or re.match('NN[*]?', temp[j][1]) or temp[j][0] in although or temp[j][0] == ',':
                    near.append(temp[j][0])
            print(left, right)
            s.append(near)
        if temp[i][0] in but:
            near = []
            left = max(0, i-2)
            while(left>=0):
                if re.match('[,.!?;]', temp[left][0]) != None:
                    break
                left -= 1
            right = min(l, i+2)
            while(right<l):
                if re.match('[,.!?;]', temp[right][0]) != None:
                    break
                right += 1
            for j in range(left, right):
                if re.match('JJ[*]?',temp[j][1])!=None or re.match('RB[*]?', temp[j][1])!=None or re.match('NN[*]?', temp[j][1]) or temp[j][0] in although or temp[j][0] == ',':
                    near.append(temp[j][0])
            print(left, right)
            s.append(near)
    return s
    '''


# In[ ]:


'''
print(turn(data_df['text'][1]))
print(data_df['text'][1])
'''

