import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext):
    update.message.reply_text("مرحبًا! أنا بوت يعمل على Render! 🚀")

TOKEN = os.environ.get("TOKEN")  # التوكن يُؤخذ من متغيرات البيئة في Render

if __name__ == "__main__":
    updater = Updater(TOKEN)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.start_polling()
    print("✅ البوت يعمل...")
    updater.idle()