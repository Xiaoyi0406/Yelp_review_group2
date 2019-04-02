# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 17:59:21 2019

@author: 74293
"""

import pandas as pd
from word2vec import word_embedding
import config
import numpy as np
import Svm


#load data
df = pd.read_csv(config.path_csv, engine='python',header = True)
JJ = [item for item in df['JJ']]
JJ_unique = []
for item in JJ:
    for subitem in str(item).split():
        if subitem not in JJ_unique:
         ##   print (subitem)
            JJ_unique.append(subitem)

#load word2vec
Word_embedding = word_embedding()
Word2vec = Word_embedding.load_my_vecs(vocab = JJ_unique, k = config.word2vec_dim) # 返回一个词向量字典

#get the X_train Y_train
X_train = []
Y_train = []
for i in range(len(df)):
    if pd.isnull(df['food_JJ'][i])==True:
        continue
    temp1 = str(df.loc[i]['food_JJ']).split()
    temp2 = str(df.loc[i]['food_RB']).split()
    for j in range(len(temp1)):
        X_train.append(Word2vec[temp1[j]])
        if temp2[j] in config.deny_word:
            Y_train.append(6-int(df.loc[i]['stars']))
        else:
            Y_train.append(int(df.loc[i]['stars']))

for i in range(len(df)):
    if pd.isnull(df['service_JJ'][i])==True:
        continue
    temp1 = str(df.loc[i]['service_JJ']).split()
    temp2 = str(df.loc[i]['service_RB']).split()
    for j in range(len(temp1)):
        X_train.append(Word2vec[temp1[j]])
        if temp2[j] in config.deny_word:
            Y_train.append(6-int(df.loc[i]['stars']))
        else:
            Y_train.append(int(df.loc[i]['stars']))

    
X_train = np.array(X_train)
Y_train = np.array(Y_train)


# do Svm training
svc = Svm.svm_train_model(X_train, Y_train)

# do Svm predict
X_text = []
X_text.append(Word2vec['good'])
X_text.append(Word2vec['great'])
X_text.append(Word2vec['excellent'])
X_text.append(Word2vec['bad'])
X_text = np.array(X_text)
svc.predict(X_text)
path = "/Users/kzhao46/Dropbox/score/data/"
    names = []
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.splitext(file_path)[1] == '.csv':
            names.append(file_path)
    for name in names:
        f=pd.read_csv("/Users/kzhao46/Dropbox/score/data/"+name+'.csv','r',encoding='utf8')
        f['score_food']=f['food_JJ'].apply(lambda x: x.find_score())
        f.to_csv('/Users/kzhao46/Dropbox/score/out/'+name+'.csv', index = False, encoding='utf-8')