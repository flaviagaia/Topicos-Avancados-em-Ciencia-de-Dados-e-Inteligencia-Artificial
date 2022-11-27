# -*- coding: utf-8 -*-
"""Stemizacao.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19ssQ6SDaw1EspgEZhwxYriQZ_7sda_kv

### Explorando operações de stemização
"""

# carrega conjunto de stemmers
from nltk.stem import *

# carrega apenas o stemmer Porter
from nltk.stem.porter import PorterStemmer

# carrega apenas o stemmer Snowball
from nltk.stem.snowball import SnowballStemmer

stemmer = PorterStemmer()

exemplos_pt = ['canções', 'cantiga', 'canção', 'ordenado', 'ordem', 'ordens', 
            'ator', 'ativo', 'carros', 'carro', 'carrinho', 'carrão', 'vendados', 
            'venda', 'vendas', 'invencível', 'cavalo', 'cavaleiro', 'cavalheiro',
            'correio', 'correr', 'corredor', 'comparar', 'comportamento']

resultado = [stemmer.stem(exemplo) for exemplo in exemplos_pt]
resultado

# Utilizando palavras em inglês:
exemplos_en= ['dogs', 'programming', 'programs', 'programmed', 'cakes', 'indices', 'matrices']
resultado = [stemmer.stem(exemplo) for exemplo in exemplos_en]
resultado

"""O `stemmer` Porter não é especificado para outros idiomas que não o inglês.

O `stemmer` Snowball atende essa lacuna, mas deve ser orientado quanto ao idioma que será trabalhado. 
"""

# Lista de idiomas atendidos:
SnowballStemmer.languages

# Indicando o idioma na instanciação do `stemmer`
stemmer = SnowballStemmer("portuguese")

resultado = [stemmer.stem(exemplo) for exemplo in exemplos_pt]
resultado

"""A stemização das palavras 'vendas', 'venda' e 'vendado' é um exemplo de `over-stemming`(excesso) visto que a palavra 'vendado' tem significado diferente das palavras 'vendas' e 'venda', mas foi reduzida ao mesmo radical."""
