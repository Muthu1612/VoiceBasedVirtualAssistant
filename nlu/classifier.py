from tensorflow.keras.models import load_model
import numpy as np

labels = open('nlu\entities.txt', 'r', encoding='utf-8').read().split('\n')
model = load_model('nlu\model.h5')

label2idx = {}
idx2label = {}

for k, label in enumerate(labels):
    label2idx[label] = k
    idx2label[k] = label



def classify(text):

    # x = np.zeros((1, 48, 256), dtype='float32')
    x = np.zeros((1, 26, 256), dtype='float32')   
    # if len(text) > 48:
    if len(text) > 26:
        text = text[:26]

    for k, ch in enumerate(bytes(text.encode('utf-8'))):
        x[0, k, int(ch)] = 1.0

    out = model.predict(x)
    idx = out.argmax()

    #print('Text: "{}" is classified as "{}"'.format(text, idx2label[idx]))
    return {"entity" : idx2label[idx], "conf" : max(out[0])}

'''
if __name__=='__main__':
    while True:
        text = input('Enter some text:')
        print(classify(text))
'''