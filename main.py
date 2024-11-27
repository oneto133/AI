import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from adicionar import dados
from treinamento import AI
from enviar_email import enviar_mensagem

dado = dados()
class AI():
    def __init__(self):
        pass

    def diálogo(self):
        evento = {}
        while True:
            pergunta = input("Você: ")
            vetorizar, modelo, respostas_map = self.carregar_modelo()  # Carrega o modelo a cada interação
            resposta, probabilidade = self.responder(pergunta)

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
                    enviar_mensagem("Teste IA", resposta)
                    
                    

    def carregar_modelo(self):
        with open("Minha_IA.pkl", "rb") as arquivo:
            self.vetorizar, self.modelo, self.respostas_map = pickle.load(arquivo)
        return self.vetorizar, self.modelo, self.respostas_map

    def responder(self, pergunta):
        pergunta_vetorizada = self.vetorizar.transform([pergunta])
        predicao = self.modelo.predict(pergunta_vetorizada)
        probabilidade = self.modelo.predict_proba(pergunta_vetorizada).max()
        resposta_invertida = {v: k for k, v in self.respostas_map.items()}
        if predicao[0] in resposta_invertida:  # Verificar se a chave existe no dicionário
            resposta = resposta_invertida[predicao[0]]
        else:
            resposta = "Resposta não encontrada"
        return resposta, probabilidade
    
ia = AI()
ia.diálogo()