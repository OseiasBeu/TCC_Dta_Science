# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# <a href="https://colab.research.google.com/github/OseiasBeu/TCC_Dta_Science/blob/main/trabalho_final.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
# %% [markdown]
# ## Importação das bibliotecas

# %%
import nltk
import re
from nltk.corpus import wordnet
from nltk import FreqDist
from nltk.corpus import brown
import pandas as pd


# %%
nltk.download()


# %%


# %% [markdown]
# ## Entrada de dados! 
# %% [markdown]
# É nessa parte do script por onde as API's serão consultadas e as bases serão lidas.

# %%
file = '/content/drive/MyDrive/MBA/ProjetoFinal/news.csv'
df_dataBase = pd.read_csv(file, sep=';', header=None)


# %%



