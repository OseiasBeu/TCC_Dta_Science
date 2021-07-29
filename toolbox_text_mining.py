# -*- coding: utf-8 -*-
import nltk
import re
from nltk.corpus import wordnet
from nltk import FreqDist
from nltk.corpus import brown
import pandas as pd
from googletrans import Translator
import time

# %matplotlib inline
import numpy as np
# import matplotlib.pyplot as plt
from textblob import TextBlob

import logging as logger
logger.basicConfig(filename='logs/logs.log', filemode='w', level=logger.DEBUG)

"""## Entrada de dados!
É nessa parte do script por onde as API's serão consultadas e as bases serão lidas.
"""

def load_dataframe(link):
  print('-[] Efetuando o carregamento do datafreme.')
  try:
    logger.info('Efetuando o carregamento do datafreme.')
    file = link
    dataBase = pd.read_csv(file, sep=';', header=None)
    df = pd.DataFrame(dataBase)
    logger.info('Carregamento efetuado com sucesso!')
    return df
  except Exception as e:
    logger.error(f'Houve um erro no carregamento do dataset: {e}')

"""## Verificando a frequência das palavras"""

def array_to_word_list(lista_de_frases):
  print('-[] Convertendo lista de frases em lista de palavras.')
  logger.info('Convertendo lista de frases em lista de palavras.')
  try:
    lista_de_palavras = []
    for x in lista_de_frases:
      lista_de_palavras += x.split()
    logger.info('Lista de palavras gerada com sucesso!')
    return lista_de_palavras
  except Exception as e:
    logger.error(f'Houve um erro na conversão:{e}')

def freq_word(array_lista_de_palavras):
  logger.info("Gerando frequência de palavras.")
  try:
    frequencia_de_palavras = FreqDist(array_lista_de_palavras)
    logger.info("Frequência de palavras gerada com sucesso!")
    return frequencia_de_palavras
  except Exception as e:
    logger.error(f'Houve um erro na geração da frequência das palavras: {e}')
    
# def plot_freq_word(frequencia_de_palavras):
#   logger.info("Gerando gráfico de frequência de palavras")
#   try:
#     palavras = frequencia_de_palavras.keys()
#     y_pos = np.arange(len(palavras))
#     contagem = frequencia_de_palavras.values()
#     plt.bar(y_pos, contagem, align='center', alpha=0.5)
#     plt.xticks(y_pos, palavras)
#     plt.ylabel('Frequencia')
#     plt.title('Frequencia das palavras na frase')
#     logger.info('Gráfico Gerado com sucesso!')
#     plt.show()
#   except Exception as e:
#     logger.error(f"Houve um erro na plotagem da frequência das palavras: {e}")

def Limpeza_dados(lista_de_frases):
  print('-[] Efetuando Data Cleaning...')
  lista_de_frases_tratadas = []
  for instancia in lista_de_frases:
    # remove links, pontos, virgulas,ponto e virgulas dos tweets
    instancia = re.sub(r"http\S+", "", instancia).lower().replace('.','').replace(';','').replace('-','').replace(':','').replace(')','')
    lista_de_frases_tratadas.append(instancia)

  return (lista_de_frases_tratadas)

"""## Removendo a stop_words
* Palavras ou termos que são muito usadas mas normalmente não tem nenhum significado como artigos: 'é','o','a'
* Técnica usada para pré-processamento de dados
"""

def RemoveStopWords(instancia):
  print('-[] Removendo StopWords.')
  logger.info('Removendo Stop Words')
  try:
    stopwords = set(nltk.corpus.stopwords.words('portuguese'))
    palavras = [i.lower() for i in instancia if not i in stopwords]
    logger.info("Stop Wrods removidas com sucesso!")
    return (" ".join(palavras))
  except Exception as e:
    print(e)
    logger.error(f"Houve um erro na remoção das stop words: {e}")

"""## Analise de sentimento"""
def phrases_polarity(array_lines):
  print('-[] Efetuando a análise de sentimento.')
  translator = Translator()
  logger.info('Efetuando a análise de sentimento.')
  try:
    dict = {}
    key = 0
    for line in array_lines:
      frase = TextBlob(line)
      detect = translator.detect(frase)
      # print(detect.lang)
      if detect.lang != 'en':
        translate_frase = translator.translate(frase,dest='en')
        frase2 =TextBlob(translate_frase.text)
        dict[key] = {'frase_original': frase, 'frase_traduzida': frase2, 'polaridade':frase2.sentiment[0],'subjetividade':frase2.sentiment[1]}
        key+=1
      else:
        frase2 =frase
        dict[key] = {'frase_original': frase, 'frase_traduzida': frase2, 'polaridade':frase2.sentiment[0],'subjetividade':frase2.sentiment[1]}
        key+=1
      logger.info('Dicionario com polaridades gerado com sucesso!')
    return dict
  except Exception as e:
    logger.error(f'Houve um erro na análise de sentimento: {e}')

def calc_nps(arrays_respostas):
  print('-[] Calculando NPS.')
  promotores = []
  detratores = []
  neutros = []
  for resposta in arrays_respostas:
    if resposta > 0:
      promotores.append(resposta)
    elif resposta < 0: 
      detratores.append(resposta)
    else:
      neutros.append(resposta)
  
  print(f'>Quantidade de Promotores:{len(promotores)} \n>Quantidade de detratores:{len(detratores)}\n>Quantidade de neutros:{len(neutros)}')

  nps = ((len(promotores) - len(detratores))/len(arrays_respostas))*100
  print(f'Valor de NPS: {nps}')
  return nps


lista_de_frases =['https://oseias.beu esse e o site','Eu odeio. Testes!','isto, não é um cachimbo.']
a = Limpeza_dados(lista_de_frases)
print(a)