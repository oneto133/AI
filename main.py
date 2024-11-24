import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from adicionar import dados
from treinamento import AI

dado = dados()

def carregar_modelo():
    with open("Minha_IA.pkl", "rb") as arquivo:
        vetorizar, modelo, respostas_map = pickle.load(arquivo)
    return vetorizar, modelo, respostas_map

def responder(pergunta):
    pergunta_vetorizada = vetorizar.transform([pergunta])
    predicao = modelo.predict(pergunta_vetorizada)
    probabilidade = modelo.predict_proba(pergunta_vetorizada).max()
    resposta_invertida = {v: k for k, v in respostas_map.items()}
    if predicao[0] in resposta_invertida:  # Verificar se a chave existe no dicionário
        resposta = resposta_invertida[predicao[0]]
    else:
        resposta = "Resposta não encontrada"
    return resposta, probabilidade
evento = {}
while True:
    
    pergunta = input("Você: ")
    vetorizar, modelo, respostas_map = carregar_modelo()  # Carrega o modelo a cada interação
    resposta, probabilidade = responder(pergunta)

    if probabilidade < 0.00540:
        print("Ainda não fui treinado para responder a essa pergunta")
        print(probabilidade)
        IA = input("Adicione o que eu devo responder para essa pergunta... ")
        dado.perguntas(pergunta)  # Atualiza o modelo com a nova pergunta e resposta
        dado.resposta(IA)
        AI()
    else:
        if resposta == "O que você não entendeu?":
            print(f"IA: {resposta}\nVocê me perguntou '{evento['usuário']}' \nE eu respondi \n'{evento['IA']}'\n"
            "Fique a vontade para tirar suas dúvidas")
        else:
            evento.clear()
            evento['usuário'] = pergunta
            evento['IA'] = resposta
            print("IA: ", resposta)
            print(probabilidade)
