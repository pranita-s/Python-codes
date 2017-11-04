import os
import pandas as pd
import nltk
import gensim
from nltk.corpus import stopwords
from gensim import corpora, models, similarities

### File path consts.
file_path = "E:/First Sem/Python/word2vec"
train_file_name = "jokes.csv"

default_character_support = 'utf-8'
x_column = 'Question'
y_column = 'Answer'

### cd to train file
os.chdir(file_path)

### create data frame
data_frame = pd.read_csv(train_file_name)

### load data from csv
questions = data_frame[x_column].values.tolist()
answers = data_frame[y_column].values.tolist()

### create corpus bulk
corpus = questions + answers

### tokenize each sentence/row in the corpus using NLTK
### default char set supported for now is utf-8

tokenized_corpus = [sentence.lower().split() for sentence in corpus]
tokenized_corpus = [i for i in tokenized_corpus if i not in stopwords.words('english')]
tokenized_corpus = [nltk.word_tokenize(sentence) for sentence in corpus]

#([i for i in sentence.lower().split() if i not in stop])

#tokenized_corpus = [word for word in tokenized_corpus if word not in stopwords.words('english')]

### create the training model
model = gensim.models.Word2Vec(tokenized_corpus, min_count=1, size=32)

model.save('testmodel')
model = gensim.models.Word2Vec.load('testmodel')
print(model.most_similar('joke'))