from nltk.corpus import stopwords
import re
import nltk
import itertools
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
from nltk.corpus import wordnet
nltk.download('stopwords')
nltk.download('wordnet')

def clean_text(text):
    ## Clean the text
    text = re.sub(r"[^A-Za-z0-9^,!.\/'+-=]", " ", text)
    text = re.sub(r"what's", "what is ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"\'ve", " have ", text)
    text = re.sub(r"n't", " not ", text)
    text = re.sub(r"i'm", "i am ", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    text = re.sub(r",", " ", text)
    text = re.sub(r"\.", " ", text)
    text = re.sub(r"!", " ! ", text)
    text = re.sub(r"\/", " ", text)
    text = re.sub(r"\^", " ^ ", text)
    text = re.sub(r"\+", " + ", text)
    text = re.sub(r"\-", " - ", text)
    text = re.sub(r"\=", " = ", text)
    text = re.sub(r"'", " ", text)
    text = re.sub(r"(\d+)(k)", r"\g<1>000", text)
    text = re.sub(r":", " : ", text)
    text = re.sub(r" e g ", " eg ", text)
    text = re.sub(r" b g ", " bg ", text)
    text = re.sub(r" u s ", " american ", text)
    text = re.sub(r"\0s", "0", text)
    text = re.sub(r" 9 11 ", "911", text)
    text = re.sub(r"e - mail", "email", text)
    text = re.sub(r"j k", "jk", text)
    text = re.sub(r"\s{2,}", " ", text)
    
    ## Split the text and get part-of-speech tag
    split_text = nltk.pos_tag(word_tokenize(text))
    add_text = list()
    stops = set(stopwords.words("english"))

    ## Remain only adjective
    for j in range(len(split_text)):
        if split_text[j][0] not in stops and re.search('JJ.*', split_text[j][1]) is not None:
            word = lemmatizer.lemmatize(split_text[j][0].lower(), pos = wordnet.ADJ)
            if j > 0 and split_text[j-1][0] == 'not':
                add_text.append('not ' + word)
            else:
                add_text.append(word)
    return add_text

import json
from langdetect import detect

## Load training data
def getTrainData(fileName):
    x = list()
    y = list()
    with open(fileName, 'r') as f:
        line = f.readline()
        while len(line) > 0:
            sample = json.loads(line)
            try:
                text = sample['text']
                if len(text) > 0 and detect(text) == 'en': # may have exception like text = '...'
                    add_text = clean_text(text)
                    x.append(add_text)
                    y.append(sample['stars'])
            except:
                line = f.readline()
                next
            line = f.readline()
    return(x, y)

## Load test data
def getTestData(fileName):
    x = list()
    ID = list()
    with open(fileName, 'r') as f:
        line = f.readline()
        while len(line) > 0:
            sample = json.loads(line)
            try:
                text = sample['text']
                ID.append(sample['business_id'])
                if len(text) > 0 and detect(text) == 'en': # may have exception like text = '...'
                    add_text = clean_text(text)
                    x.append(add_text)
                else:
                    x.append([])
            except:
                x.append([])
                line = f.readline()
                next
            line = f.readline()
    return(x, ID)

x_train_raw, y_train = getTrainData('train_sub.json')
x_test_raw, testID = getTestData('review_test.json')

## Creat training array
def convert(text_list):
    n = len(text_list)
    p = len(vocabList)
    seq = np.zeros((n, p))
    for i in range(n):
        for j in range(len(text_list[i])):
            word = text_list[i][j]
            if word in vocabList:
                index = vocabList.index(word)
                seq[i,index] = 1
    #return(seq)
    return(seq)

vocabList = list(set(itertools.chain.from_iterable(x_train_raw)))
x_train = convert(x_train_raw)
x_test = convert(x_test_raw)

from sklearn.naive_bayes import BernoulliNB
clf = BernoulliNB().fit(x_train, y_train)

y_test_pred = clf.predict(x_test)

with open('result.csv' , 'w') as f:
    f.write('ID,Expected\n')
    for i in range(len(y_test_pred)):
        f.write(str(testID[i]) + ',' + str(y_test_pred[i]) + '\n')





