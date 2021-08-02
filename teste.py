# -*- coding: utf-8 -*-
import pandas as pd
from pandas.core.reshape.concat import concat
import toolbox_text_mining
import extract_file
import extract_tweet
import os
from textblob import TextBlob
os.system('cls' if os.name == 'nt' else 'clear')

def phrases_polarity(array_lines,criterio_de_pesquisa):
  print('-[] Efetuando a análise de sentimento.')
  try:
    dict = {}
    key = 0
    for line in array_lines:
        frase = TextBlob(line)
        frase2 =frase
        dict[key] = {'criterio_de_pesquisa':criterio_de_pesquisa,'frase_original': frase, 'frase_traduzida': frase2, 'polaridade':frase2.sentiment[0],'subjetividade':frase2.sentiment[1]}
        key+=1

    sense_df = pd.DataFrame(dict.items()) 
    sense_df.to_csv('datasets/base_com_sentimentos_new.csv',sep=';',encoding='utf-8',index=False)

    df_exsitis = pd.read_csv('datasets/base_com_sentimentos.csv',sep=';',encoding='utf-8')
    df_exsitis = pd.DataFrame(df_exsitis)

    sense_df_old = pd.read_csv('datasets/base_com_sentimentos_new.csv',sep=';',encoding='utf-8')
    sense_df_old = pd.DataFrame(sense_df_old)

    dataframes_concate  = pd.concat([sense_df_old,df_exsitis],ignore_index=False)
    dataframes_concate.reset_index()
    print(dataframes_concate.columns)
    dataframes_concate = dataframes_concate['1']
    dataframes_concate.to_csv('datasets/base_com_sentimentos.csv',sep=';',encoding='utf-8',index=False)
    print('Analise de sentimento realizado com sucesso!')
    return dict
  except Exception as e:
      print(e)


wb = pd.read_csv('datasets/FMU_base_comentarios_ingles.csv',sep=';',encoding='utf-8')
df = pd.DataFrame(wb)
print(df.head())

lista_de_frases = df['text'].to_list()
lista_de_frases_tratadas = toolbox_text_mining.Limpeza_dados(lista_de_frases)
lista_de_palavras = toolbox_text_mining.array_to_word_list(lista_de_frases_tratadas)
lista_de_palavras_s_stop_words = toolbox_text_mining.RemoveStopWords(lista_de_palavras)
frequencia_de_palavras = toolbox_text_mining.freq_word(lista_de_palavras_s_stop_words.split())

criterio_de_pesquisa = 'FMU'
frases_com_sentimento = phrases_polarity(lista_de_frases_tratadas,criterio_de_pesquisa)

respostas = []
for i in frases_com_sentimento:
  print(f'Frase: {frases_com_sentimento[i]["frase_original"]}\n Polaridade:{frases_com_sentimento[i]["polaridade"]} | Subjetividade:{frases_com_sentimento[i]["subjetividade"]} \n')
  respostas.append(frases_com_sentimento[i]["polaridade"])

nps = toolbox_text_mining.calc_nps(respostas)