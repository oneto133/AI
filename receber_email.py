from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os.path
import pickle

# Escopo para acessar mensagens
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def autenticar_gmail():
    """Autentica na Gmail API e retorna o serviço"""
    creds = None
    # Verifica se já existe um token salvo
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # Se não existir, autentica usando o credentials.json
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Salva o token para reutilização futura
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return build('gmail', 'v1', credentials=creds)

def listar_mensagens():
    """Lista as mensagens mais recentes"""
    try:
        service = autenticar_gmail()
        # Pega as mensagens na caixa de entrada
        results = service.users().messages().list(userId='me', maxResults=5).execute()
        messages = results.get('messages', [])

        if not messages:
            print("Nenhuma mensagem encontrada.")
        else:
            print("Mensagens:")
            for message in messages:
                msg = service.users().messages().get(userId='me', id=message['id']).execute()
                print(f"- Assunto: {msg['snippet']}")
    except Exception as e:
        print(f"Erro ao listar mensagens: {e}")

if __name__ == '__main__':
    listar_mensagens()
