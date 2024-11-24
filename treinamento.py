import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import csv

class AI():
    def __init__(self):

        perguntas = []
        respostas = []

        with open("perguntas.csv", 'r', encoding='utf-8') as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                perguntas.extend(linha)
        with open("respostas.csv", 'r', encoding='utf-8') as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                respostas.extend(linha)


        respostas_map = {resposta: i for i, resposta in enumerate(respostas)}
        respostas_numericas = [respostas_map[resposta] for resposta in respostas]


        vetorizar = TfidfVectorizer()
        x = vetorizar.fit_transform(perguntas)

        modelo = LogisticRegression()
        modelo.fit(x, respostas_numericas)

        with open("Minha_IA.pkl", "wb") as arquivo:
            pickle.dump((vetorizar, modelo, respostas_map), arquivo)

        print("Treinado com sucesso")

if __name__ == "__main__":
    AI()