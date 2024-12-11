import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = '7638003015:AAFKf61H_uTaC2BEzQxUxgd4Mlo9o2LGFG0'

async def start(update, context):
    await update.message.reply("Olá! Eu sou um bot.")
    logger.info(f"Mensagem recebida: {update.message.text}")

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.ALL, start))
    logger.info("Bot está iniciando...")
    application.run_polling()

if __name__ == '__main__':
    main()