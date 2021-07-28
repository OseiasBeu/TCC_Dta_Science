import pandas as pd

def readFile(pathFile):
    extension = pathFile.split(".")[1]
    if extension == 'csv':
        wb = pd.read_csv(pathFile, header=None)
        df = pd.DataFrame(wb)
    elif extension == 'xlsx':
        wb = pd.read_excel(pathFile)
        df = pd.DataFrame(wb)
    else:
        mensagem = 'Tipo de arquivo não detectato! \n Faça a inserção de um dos seguintes tipos: CSV ou XLSX'
        print(mensagem)
        return mensagem
    return df


