# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 17:59:59 2019

@author: 74293
"""
import numpy as np
import config
import gensim
class word_embedding():
    def __init__(self):
        print('Now loading the word embedding')
        self.text = 0
    
    def text(self):
        print(self.text)
    
    def load_my_vecs(self, vocab, k):
        # load the google word2vec model
        Word2vec = gensim.models.KeyedVectors.load_word2vec_format(config.word2vec_path, binary=True)
        
        #load unknown words with avg word embeding
        word_vecs_numpy = []
        dict_word2vec = {}
      #  print ((vocab, k))
        for word in vocab:
            if word in Word2vec:
                word_vecs_numpy.append(Word2vec[word])
                dict_word2vec[word] = Word2vec[word]
        print(len(word_vecs_numpy))
        
        col = []
        for i in range(k):
            sum = 0.0
            # for j in range(int(len(word_vecs_numpy) / 4)):
            for j in range(int(len(word_vecs_numpy))):
                sum += word_vecs_numpy[j][i]
                sum = round(sum, 6)
            col.append(sum)
        zero = []
        for m in range(k):
            # avg = col[m] / (len(col) * 5)
            avg = col[m] / (len(word_vecs_numpy))
            avg = round(avg, 6)
            zero.append(float(avg))
        
        oov = 0
        iov = 0
        for word in vocab:
            if word not in dict_word2vec:
                # word_vecs[word] = np.random.uniform(-0.25, 0.25, k).tolist()
                # word_vecs[word] = [0.0] * k
                oov += 1
                dict_word2vec[word] = zero
            else:
                iov += 1
                
        print("oov count", oov)
        print("iov count", iov)
        return dict_word2vec