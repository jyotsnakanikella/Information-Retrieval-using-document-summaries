from gensim.models import Word2Vec
from nltk.tokenize import sent_tokenize, word_tokenize 
import warnings 
  
warnings.filterwarnings(action = 'ignore') 
  
import gensim
import nltk
#from gensim.models import Word2Vec
nltk.download('punkt')
import os
path='G:/net downloads/docs/'
files = []
f=""
for i in os.listdir('G:/net downloads/docs'):
    if i.endswith('.txt'):
        filename=path+i
        print(i)
        file=open(filename,"r")
        f=f+str(file.read())
       
 
data = [] 
# iterate through each sentence in the file
for i in sent_tokenize(f):
    temp = [] 
      
    # tokenize the sentence into words
    for j in word_tokenize(i):
        temp.append(j.lower()) 
    data.append(temp) 

print(data)
model1 = Word2Vec(data, min_count=1)
# summarize the loaded model
print(model1)
# summarize vocabulary
words = list(model1.wv.vocab)
print(words)
# access vector for one word
print(model1['pattern'])
# save model
model1.save('model1.bin')
# load model
model1.wv.save_word2vec_format('model1.txt', binary=False)
new_model1 = Word2Vec.load('model1.bin')
print(new_model1)
