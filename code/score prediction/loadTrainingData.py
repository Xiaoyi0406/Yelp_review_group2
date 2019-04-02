import sys
import string
import re
import numpy as np
import json
from nltk.corpus import stopwords

from langdetect import detect
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords

infile = sys.argv[1]
outfile = sys.argv[2]


def clean_text(text):
    
    ## Remove puncuation
    text = text.translate(string.punctuation)
    
    ## Convert words to lower case and split them
    text = text.lower().split()
    
    ## Remove stop words
    stops = set(stopwords.words("english"))
    text = [w for w in text if not w in stops and len(w) >= 3]
    
    ## Merge strings    
    text = " ".join(text)
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
    ## Stemming
    text = text.split()
    stemmer = SnowballStemmer('english')
    stemmed_words = [stemmer.stem(word) for word in text]
    text = " ".join(stemmed_words)
    return text

def getTrainData(fileName):
    x = list()
    y = list()
    with open(fileName, 'r') as f:
        line = f.readline()
        while len(line) > 0:
            sample = json.loads(line)
            try:
                text = sample['text']
                ## Only return reviews written by English without empty reviews
                if len(text) > 0 and detect(text) == 'en':#may have exception like text = '...'
                    add_text = clean_text(text)
                    x.append(add_text)
                    y.append(sample['stars'])
            except:
                line = f.readline()
                next
            line = f.readline()
    return(x, y)


x_train, y_train = getTrainData(infile)

with open(outfile, 'w') as f:
	json.dump({'y':y_train, 'x':x_train}, f)

