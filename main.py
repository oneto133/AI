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
        """
        Como se trata do código principal, não há atributos inicialmente, pois
        o código vai se moldando conforme o laço de repetição está funcionando.

        No diálogo, o laço de repetição vai funcionar recebendo dados do usuário
        e gerando assim uma interação com a IA

        Args:
            While True: O laço de recepção para o código ficar em um loop

            pergunta (str): Recebe a pergunta do usuário a IA

            IA (str): Quando a IA não souber o que responder, ou seja, quando a probilidade for baixa demais, ela pedirá ao usuário que ajude-a a responder da próxima vez.

            
        Returns:
            probabilidade (float): Após a pergunta recebida, é feito um teste de comparação para se ter noção se a IA está preparada ou não para responder a pergunta

            resposta (str): A resposta da IA já está tratada como string, apenas para ser usada
        """
        evento = {}
        try:
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
                        enviar_mensagem(titulo="Teste IA", mensagem=resposta, mensagem_final="")
        except Exception as e:
            print(e)
                    

    def carregar_modelo(self):
        """
        Carrega o modelo já treinado em formato .pkl
        """
        with open("Minha_IA.pkl", "rb") as arquivo:
            self.vetorizar, self.modelo, self.respostas_map = pickle.load(arquivo)
        return self.vetorizar, self.modelo, self.respostas_map

    def responder(self, pergunta):
        """
        Args:
            pergunta (str): Recebe a pergunta do usuário

            pergunta_vetorizada (str): Método para vetorizar a pergunta

            predicao: Realizar a previsão da possível resposta

            probabilidade: Pega números para se ter noção do quão preparada a IA está para a pergunta    
        

        Returns:
            resposta (str): contém a reposta da IA
            """
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