from telegram.ext import Updater, CommandHandler

#declarando token variables y funciones
TOKEN = 'Tu token' # encriptar o algo.xd

def start(update, context):
       update.message.reply_text('Hola, mortal')
       # name = update.message.from_user.username {}
       
def getBotInfo(update, context):
      name = update.message.from_user.username
      update.message.reply_text(f"Soy un bot creado por TU NOMBRE  \n administro y filtro  informacion de clientes provedores \n Gracias por invocarme, {name} ")
if __name__=='__main__': 
       updater=Updater(token=TOKEN, use_context=True)
       #creando el dispatcher
       dp=updater.dispatcher
       #comandos creados
       dp.add_handler(CommandHandler('start', start))
       dp.add_handler(CommandHandler("botInfo", getBotInfo))
       
       updater.start_polling() # seguir escuchando por mensajes entrantes
       updater.idle()
 
