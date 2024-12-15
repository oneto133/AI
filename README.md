# Documentação

Esse projeto é apenas para fins de pesquisas, os dados aqui contidos são temporários e irrelevantes, sendo assim, não adianta tentar usar desses dados para atacar quem desenvolveu o projeto.

Se sinta à vontade para contribuir com esse trabalho.


## Dependências

**Instale as dependências desse projeto**

Todas as dependências com suas versões compatíveis em -> `requeriments.txt`

Versão do python para o projeto `Python 3.11`

**A versão do python usada nesse projeto é a diferente da ultima versão, que se encontra até o momento na 3.13, pois a versão python que até o momento é compatível com o `skleanr`é a versão 3.11**

* Clone esse repositório

```
https://github.com/oneto133/AI.git
```

## main

O arquivo principal deste programa onde será dado inicio as atividades do programa é o arquivo [main.py](main.py) esse arquivo contém a classe AI que é onde se terá as funções `diálogo`, `carregar_modelo` e `responder`.

### Explicando as funções

* diálogo:

Como se trata do código principal, não há atributos inicialmente, pois o código vai se moldando conforme o laço de repetição está funcionando.

No diálogo, o laço de repetição vai funcionar recebendo dados do usuário e gerando assim uma interação com a IA

        Args:
            While True: O laço de recepção para o código ficar em um loop

            pergunta (str): Recebe a pergunta do usuário a IA

            IA (str): Quando a IA não souber o que responder, ou seja, quando a probilidade for baixa demais, ela pedirá ao usuário que ajude-a a responder da próxima vez.

            
        Returns:
            probabilidade (float): Após a pergunta recebida, é feito um teste de comparação para se ter noção se a IA está preparada ou não para responder a pergunta

            resposta (str): A resposta da IA já está tratada como string, apenas para ser usada


* carregar modelo:

Carrega o modelo já treinado que está no arquivo [Minha_IA.pkl](Minha_IA.pkl)

O treinamento acontece dentro do arquivo [treinamento.py](treinamento.py) e lá é gerado o arquivo .pkl, pois é o melhor formato para a ia fazer reconhecimento dos dados treinados.

treinamento
    Os arquivos csv de perguntas e respostas são lidos e todos os dados são colocados dentro de suas listas correspondentes, em seguida as respostas são maepeadas e indexadas

        Args:
            x: vetoriza as perguntas

            modelo: recebe um regressão logistica para se obter a previsão de um resultado, usada para treinar a IA. O treino acontece com as perguntas e suas respostas correspondentes.

    Após os dados são salvos no arquivo pickle com a função:

        with open("Minha_IA.pkl", "wb") as arquivo:
            pickle.dump((vetorizar, modelo, respostas_map), arquivo)

            