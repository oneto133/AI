import smtplib
import email.message

def enviar_mensagem(titulo, mensagem):
  corpo_mensagem = f"""
  <p>{mensagem}<p>
  <p>Segue o email automático<p>
  """
  msg = email.message.Message()
  msg['Subject'] = titulo
  msg['From'] = 'rodriguesarmando225@gmail.com'
  msg['To'] = 'allmyfilesondrive@gmail.com'
  password = "pctvcerdlwekufbg"
  msg.add_header('Content-Type', 'text/html')
  msg.set_payload(corpo_mensagem)

  s = smtplib.SMTP('smtp.gmail.com: 587')
  s.starttls()
  # Login Credentials for sending the mail
  s.login(msg['From'], password)
  s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
  print("Email enviado")


if __name__ == "__main__":
    enviar_mensagem()


