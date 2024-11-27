from enviar_email import enviar_mensagem
def mensagem():
    cont= 0
    for c in range(1, 5):
        mensagem = ("Olá, esse é o teste ", c)
        import time
        cont += 1
        enviar_mensagem("teste", mensagem)
        time.sleep(20)


mensagem()
