# -*- coding: utf-8 -*-
import toolbox_text_mining
import extract_file
import extract_tweet

print('O que você deseja fazer? ')
print('''
1 - Analise de sentimento a partir do twitter?\n
2 - Analise de sentimento a partir de um arquivo?\n
''')

resposta = input('Digite sua resposta: [1] - [2]: ')
if resposta == '1':
    print('tw')
    palavras_chave = input('Digite as palavras chave:')
    df = extract_tweet.extractTweet(palavras_chave)
    lista_de_frases = df['text'].to_list()
    # print(lista_de_frases)
    
elif resposta == '2':
    print('arquivo')
    pathFile = input('Digite o caminho do arquivo:')
    pathFile = 'datasets/news.csv'
    df = extract_file.readFile(pathFile)
    lista_de_frases = df[0].to_list()
else: 
    print('opcao não encontrada')


##### COMENTAR ######
print(type(df))
print(df.head())
# lista_de_frases = df['text'].to_list()
# lista_de_frases = df[0].to_list()
# print(lista_de_frases)
# lista_de_frases = ['Eu odeio a FMU!','A FMU é a pior universidade do mundo!','A FMU é péssima','Estudar no google é maravilhoso']

##### COMENTAR ######
lista_de_palavras = toolbox_text_mining.array_to_word_list(lista_de_frases)
lista_de_palavras_s_stop_words = toolbox_text_mining.RemoveStopWords(lista_de_palavras)
frequencia_de_palavras = toolbox_text_mining.freq_word(lista_de_palavras_s_stop_words.split())
# toolbox_text_mining.plot_freq_word(frequencia_de_palavras)

frases_com_sentimento = toolbox_text_mining.phrases_polarity(lista_de_frases)
for i in frases_com_sentimento:
  print(f'Frase: {frases_com_sentimento[i]["frase_original"]}\n Polaridade:{frases_com_sentimento[i]["polaridade"]} | Subjetividade:{frases_com_sentimento[i]["subjetividade"]} \n')