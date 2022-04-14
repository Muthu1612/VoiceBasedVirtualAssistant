import yaml
import os
import json
import numpy as np

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.utils import to_categorical

data = yaml.safe_load(open('train.yml').read())



inputs, outputs = [], []

for command in data['commands']:
    inputs.append(command['input'].lower())
    outputs.append('{}\{}'.format(command['entity'], command['action']))



max_sent = max([len(bytes(x.encode('utf-8'))) for x in inputs])



input_data = np.zeros((len(inputs), max_sent, 256), dtype='float32')

for i, inp in enumerate(inputs):
    for k, ch in enumerate(bytes(inp.encode('utf-8'))):
        input_data[i, k, int(ch)] = 1.0

#output_data = to_categorical(output_data, len(output_data))

#print(input_data.shape)

print(input_data[0].shape)

#print(len(chars))
#print('Max input seq:', max_sent)


labels = set(outputs)

fwrite = open('entities.txt', 'w', encoding='utf-8')
for label in labels:
    fwrite.write(label + '\n')
fwrite.close()

labels = open('entities.txt', 'r', encoding='utf-8').read().split('\n')

label2idx = {}
idx2label = {}

for k, label in enumerate(labels):
    label2idx[label] = k
    idx2label[k] = label

output_data = []

for output in outputs:
    output_data.append(label2idx[output])

output_data = to_categorical(output_data, len(labels))

model = Sequential()
model.add(LSTM(128))
model.add(Dense(len(labels), activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])

model.fit(input_data, output_data, epochs=512)

model.save('nlu\model.h5')


def classify(text):
    
    x = np.zeros((1, max_sent, 256), dtype='float32')

    
    for k, ch in enumerate(bytes(text.encode('utf-8'))):
        x[0, k, int(ch)] = 1.0

    out = model.predict(x)
    idx = out.argmax()

    #print('Text: "{}" is classified as "{}"'.format(text, idx2label[idx]))
    return idx2label

'''
if __name__=='__main__':
    while True:
        text = input('Enter some text:')
        classify(text)
'''