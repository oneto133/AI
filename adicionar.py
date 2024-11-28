
class dados:
    def perguntas(self, pergunta):
        """
        Adiciona dados no meu arquivo csv de perguntas.
        essas são as perguntas fornecidas para realizar o treinamento do IA
        Args:
            pergunta (str): A pergunta que será adicionadapelo usuário à máquina
        """

        with open('perguntas.csv', 'a', encoding='utf-8') as file:
            file.write(f'\n"{pergunta}"')

    def resposta(self, resposta):
        """
        As respostas são, as respostas com as quais a IA será treinada
        cada resposta tem sua pergunta correspondente
        por isso que no arquivo csv, todas as perguntas e respostas devem estar organizadas
        de acordo com o seu índice

        Args:
            resposta (str): A resposta que correspondente que a máquina deverá fornecer ao usuário...
        """
        with open('respostas.csv', mode='a', encoding='utf-8') as file:
            file.write(f'\n"{resposta}"')

