#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import string
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.corpus import stopwords
import string
import math
import re
from langdetect import detect
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import *

task_name = 'burger'
path = '/Users/jupeng.d/Downloads/newdata/Burger/'
path_out = path + task_name + '_exout.csv'
data_df=pd.read_csv(path + task_name + '_r.csv')
food = pd.read_csv(path+ task_name+ '_food.csv',delimiter=',')
service = pd.read_csv(path+ task_name+'_se.csv',delimiter=',')
food_l = list(food['food'])
service_l = list(service['service'])

def not_lang(text):
    text = re.sub('(?::|;|=)(?:-)?(?:\)|\(|D|P)','',text)
    if re.sub('[\W]+','',text) == '':
        return True
    else:
        return False

def Not_null(x):
    return x!=[]
'''
def Detect(x):
    return detect(x)
'''
def find_same_food(x):
    return list((set(x).union(set(food_l)))^(set(x)^set(food_l)))
def find_same_se(x):
    return list((set(x).union(set(service_l)))^(set(x)^set(service_l)))


def dic_detect(text):
    s = []
    i = 0
    temp = nltk.pos_tag(text)
    for word, tag in temp:
        # print ((word,tag))
        if i >= 1:
            if re.match('JJ[*]?', temp[i - 1][1]) and word in dic:
                s.append((word, temp[i - 1][0],  "None"))
                continue
            if word in dic and re.match('JJ[*]?', temp[i - 1][1]) != None:
                s.append((word, temp[i - 1][0], "None"))
                continue

        if i >= 2:
            if re.match('RB[*]?', temp[i - 2][1]) != None and re.match('JJ[*]?',
                                                                       temp[i - 1][1]) != None and word in dic:
                s.append((word, temp[i - 1][0], temp[i - 2][0]))
                continue
            if temp[i - 2][0] in dic and re.match('RB[*]?', temp[i - 1][1]) != None and re.match('JJ[*]?', tag) != None:
                s.append((temp[i - 2][0], word, temp[i - 1][0]))
                continue
        if i >= 2:
            if temp[i - 2][0] in dic and re.match('VB[*]?', temp[i - 1][1]) != None and re.match('JJ[*]?', tag) != None:
                s.append((temp[i - 2][0], word, 'None'))
                continue
        if i >= 3:
            if temp[i - 3][0] in dic and re.match('VB[*]?', temp[i - 2][1]) != None and re.match('RB[*]?', temp[i - 1][
                1]) != None and re.match('JJ[*]?', tag) != None:
                s.append((temp[i - 3][0], word, temp[i - 1][0]))
                continue
        if i >= 4:
            if temp[i - 4][0] in dic and re.match('VB[*]?', temp[i - 3][1]) != None and re.match('RB[*]?', temp[i - 2][
                1]) != None and re.match('RB[*]?', temp[i - 1][1]) != None and re.match('JJ[*]?', tag) != None:
                s.append((temp[i - 4][0], word, temp[i - 2][0] + ' ' + temp[i - 1][0]))
                continue
        i = i + 1
    return s

temp=data_df[data_df['text'].apply(not_lang)].index.values
#data_df['lang_type'] = data_df['text'].apply(Detect)
data_df.head()
temp123 = data_df
data_df['text']=data_df['text'].apply(lambda sen: re.sub(r"can\'t", "can not", sen))
data_df['text']=data_df['text'].apply(lambda sen: re.sub(r"cannot", "can not ", sen))
data_df['text']=data_df['text'].apply(lambda sen: re.sub(r"what\'s", "what is", sen))
data_df['text']=data_df['text'].apply(lambda sen: re.sub(r"\'ve ", " have ", sen))
data_df['text']=data_df['text'].apply(lambda sen: re.sub(r"n\'t", " not ", sen))
data_df['text']=data_df['text'].apply(lambda sen: re.sub(r"i\'m", "i am ", sen))
data_df['text']=data_df['text'].apply(lambda sen: re.sub(r"\'re", " are ", sen))
data_df['text']=data_df['text'].apply(lambda sen: re.sub(r"\'d", " would ", sen))
data_df['text']=data_df['text'].apply(lambda sen: re.sub(r"\'ll", " will ", sen))



data_df['text'] = data_df['text'].apply(lambda x: ''.join([c for c in x if c not in string.punctuation]))
#nltk.download('wordnet')
#data_df['text']=data_df['text'].apply(lambda sen: [WordNetLemmatizer().lemmatize(x) for x in sen.split()])
data_df['text'] = data_df['text'].apply(lambda x: nltk.word_tokenize(x))
data_df['food_ex'] = data_df['text'].apply(find_same_food)
data_df['service_ex'] = data_df['text'].apply(find_same_se)
data_df.index=[i for i in range(data_df.shape[0])]


#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
dic=food_l
data_df['food_near'] = data_df['text'].apply(dic_detect)


dic=service_l
data_df['service_near'] = data_df['text'].apply(dic_detect)
print (data_df.head())
#data_df[data_df['text_new']!=[]]
#data_df['Not_null'] = data_df['food_near'].apply(Not_null)

def split_NN(x):
    # print (x)
    NN = ''
    for item in x[tag]:
        # print (item)
        NN = NN + ' ' + item[0]
    return NN


def split_JJ(x):
    # print (x)
    JJ = ''
    for item in x[tag]:
        # print (item)
        JJ = JJ + ' ' + item[1]
    return JJ


def split_RB(x):
    # print (x)
    RB = ''
    for item in x[tag]:
        # print (item)
        RB = RB + ' ' + item[2]
    return RB

tag = 'food_near'
data_df['food_NN'] = data_df.apply(split_NN, axis=1)
data_df['food_JJ'] = data_df.apply(split_JJ, axis=1)
data_df['food_RB'] = data_df.apply(split_RB, axis=1)
tag = 'service_near'
data_df['service_NN'] = data_df.apply(split_NN, axis=1)
data_df['service_JJ'] = data_df.apply(split_JJ, axis=1)
data_df['service_RB'] = data_df.apply(split_RB, axis=1)
data_df.to_csv(path_out, header = True)