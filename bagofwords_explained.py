# -*- coding: utf-8 -*-
"""BagOfWords_Explained.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1G8aUX4ZELlNa7b0C4Kt_lEMZqizdvb01

# Bag of Words

A estrutura de **Bag of Words** é a forma mais primitiva de representação de texto em vetores.

Os documentos são representados pela frequência de ocorrência de cada token.

Considerando o seguinte corpus (conjunto de documentos):
* 'Muito bom  gostei do produto atendeu todas as minhas expectativas.recomendo para todos'
* 'Excelente produto recomendo, fácil limpeza e de manuseio.'
"""

import spacy
import pandas as pd
import re
import numpy as np

"""Para a normalização, será utilizada a biblioteca spaCy."""

!spacy download pt_core_news_sm -q

# fazer a carga
nlp = spacy.load('pt_core_news_sm')

sentences = ['Muito bom  gostei do produto atendeu todas as minhas expectativas. recomendo para todos',
             'Excelente produto recomendo, fácil limpeza e de manuseio.']

def normalize(sentence):
  sentence_tokenize = [token.lemma_ for token in nlp(sentence.lower()) 
              if (token.is_alpha & ~token.is_stop)]
  return ' '.join(sentence_tokenize)

preprocessed_sentences = [normalize(sentence) for sentence in sentences]

bow_matrix = np.zeros((len(preprocessed_corpus), len(vocab)))

"""O passo agora é criar o dicionário do corpus, isto é, o conjunto de tokens que compõem os textos."""

set_of_tokens = set()
for sentence in preprocessed_sentences:
  for word in sentence.split():
    set_of_tokens.add(word)
vocab = list(set_of_tokens)
print(vocab)

position = {}
for i, token in enumerate(vocab):
  position[token] = i
print(position)

"""Com a relação de palavras definida, o passo é criar uma matriz para ser preenchida."""

bow_matrix = np.zeros((len(preprocessed_sentences), len(vocab)))
bow_matrix

"""Agora se dá o preenchimento da matriz:"""

for i, preprocessed_sentence in enumerate(preprocessed_sentences):
  for token in preprocessed_sentence.split():
    bow_matrix[i][position[token]] = bow_matrix[i][position[token]] + 1

bow_matrix

"""Essa é a Bag of Words desse corpus de 2 sentenças.

Obviamente, já existe ferramentas python que reduzem e simplificam esse trabalho de criação das BoW.

Trata-se do CountVectorizer disponibilizado na `sklearn` ou `scikit-learn`.
"""

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
bow_matrix = vectorizer.fit_transform(preprocessed_sentences)

print(vectorizer.get_feature_names())
print(bow_matrix.toarray())

"""### Para exercitar, capture 3 sentenças de forma aleatória do dataset carregado abaixo e aplique o CountVectorizer para encontrar a matriz BoW do corpus."""

exercicio = pd.read_csv('https://raw.githubusercontent.com/alexvaroz/data_science_alem_do_basico/master/americanas_analise_sentimento_preparado.csv')

exercicio = exercicio.sample(3)
