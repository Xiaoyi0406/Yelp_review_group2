import keras
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, LSTM
from keras.layers.embeddings import Embedding

import string
import numpy as np
import sys
import json

from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
from nltk.stem.snowball import SnowballStemmer

trainfile = sys.argv[1]
testfile = sys.argv[2]

## Load training set
with open(trainfile, 'r') as f:
	file = json.load(f)
	x_train = file['x']
	y_train = file['y']
	del file

## Load test set
with open(testfile, 'r') as f:
	x_test = json.load(f)['x']

### Create sequence
tokenizer = Tokenizer()
tokenizer.fit_on_texts(x_train)
## For training set
sequences = tokenizer.texts_to_sequences(x_train)
x_train_seq = pad_sequences(sequences, maxlen=150)
del x_train # Free memory
x_train_seq = np.array([sorted(i) for i in x_train_seq])
y_train_labels = keras.utils.to_categorical(y_train, num_classes=6)
del y_train # Free memory
vocabulary_size = len(tokenizer.word_index) + 1
## For test set
sequences = tokenizer.texts_to_sequences(x_test)
x_test_seq = pad_sequences(sequences, maxlen=150)
x_test_seq = np.array([sorted(i) for i in x_test_seq])
del x_test # Free memory

## Train LSTM model
model = Sequential()
model.add(Embedding(vocabulary_size, 128, input_length=150))
model.add(LSTM(64, return_sequences=True, recurrent_dropout=0.9))
model.add(LSTM(32, recurrent_dropout=0.5))
model.add(Dense(6, activation='softmax'))
model.compile(loss="mean_squared_error", optimizer="rmsprop", metrics=['mse'])
model.fit(x_train_seq, y_train_labels, epochs=10, batch_size=64)

del x_train_seq # Free memory
del y_train_labels # Free memory

y_pred = model.predict_classes(x_test_seq)
y_pred = [float(i) for i in y_pred]

with open('result_lstm.csv' , 'w') as f:
    f.write('ID,Expected\n')
    for i in range(len(y_pred)):
        f.write(str(i+1) + ',' + str(y_pred[i]) + '\n')









