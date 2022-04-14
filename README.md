# TelegramBot
 bot base para frases aleatorias 
Un chatbot inteligente para el ocio, capaz de interactuar con usuarios de telegram. Utiliza pythom 3.6 | botpress | telegram API | Nginx

&https://botpress.com/docs

#flujosnodos inteligencia artificial. 
 reconocer lo que el usuario quiere.
Extracción de entidades:
fechas, horas, ciudades, nombres y más.
Etiquetado de ranuras: identifique los parámetros necesarios para cumplir con las tareas dadas.
Identificación de idioma:
 saber en qué idioma está escribiendo el usuario.
Verificación ortográfica: le brinda una cosa menos de qué preocuparse al asegurarse de que la entrada de texto de su usuario esté escrita correctamente al corregir errores tipográficos y otros.
Reconocimiento fuera de alcance:
identificar instancias cuando un usuario dice algo que el chatbot no puede entender.

Todo lo anterior te ayudará a crear conversaciones más naturales y placenteras.
INTEGRACION CON TELEGRAM: 
Telegrama
Requisitos
Un punto final HTTPS para su chatbot:

Establezca el campo externalUrl en botpress.config.json
Cree un túnel HTTPS a su máquina usando Ngrok (Tutorial).
Uso de Nginx y Let's Encrypt (Tutorial). IMPLEMENTAR CON NGINX
Crear un robot
Para crear un bot en Telegram, use BotFather de Telegram. El BotFather le pedirá un nombre y un nombre de usuario, luego generará un token de autorización para su nuevo bot.

El nombre de su bot se muestra en los detalles de contacto y en otros lugares.

El nombre de usuario es un nombre corto que se utilizará en menciones y enlaces t.me. Los nombres de usuario tienen entre 5 y 32 caracteres y no distinguen entre mayúsculas y minúsculas, pero solo pueden incluir caracteres latinos, números y guiones bajos. El nombre de usuario de su bot debe terminar en bot, como tetris_bot o TetrisBot.

Configuración
Generar un token de autorización
Cuando crea un bot de Telegram, Botfather generará automáticamente un token. El token es una cadena que se requiere para autorizar el bot y enviar solicitudes a la API de bot. Mantenga su token seguro y guárdelo de forma segura; cualquiera puede usarlo para controlar tu bot.

Si su token existente está comprometido o lo perdió por algún motivo, use el comando /token para generar uno nuevo.

Configuración
Edite data/bots/<SU_BOT_ID>/bot.config.json. En la sección messenger.channels.telegram escriba esta configuración:
habilitado: establecido en verdadero

botToken: su token de bot

Su bot.config.json debería verse así:

{
  // ... otros datos
  "mensajería": {
    "canales": {
      "telegrama": {
        "habilitado": cierto,
        "botToken": "tu_bot_token"
      }
      // ... aquí también se pueden configurar otros canales
    }
  }
}
Reinicie Botpress y hable con su bot de Telegram. El webhook se configurará automáticamente para apuntar a <EXTERNAL_URL>/api/v1/messaging/webhooks/<YOUR_BOT_ID/telegram.
