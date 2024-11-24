
class dados:
    def perguntas(self, pergunta):

        with open('perguntas.csv', 'a', encoding='utf-8') as file:
            file.write(f'\n"{pergunta}"')

        print("Dados gravados com sucesso!")

    def resposta(self, resposta):
        with open('respostas.csv', mode='a', encoding='utf-8') as file:
            file.write(f'\n"{resposta}"')
