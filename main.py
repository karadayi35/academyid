from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import Application, MessageHandler, filters, CallbackContext

# Bot token'ınızı ve grup ID'sini tanımlayın
BOT_TOKEN = '7711744456:AAFyR4VThSovVegj35LAlCmPx6lsnqrR7tM'
GROUP_ID = -1002188591527

# Admin ve sponsor mesajını tanımlayın
admin_mesaj = """
⚠️ !admin yazarak yetkililere ulaşabilirsiniz.
⭐️Adminlerimiz size ilk mesajı atmaz, Adminlerimizin isimlerini kullanarak size yazanlara itibar etmeyin !!!

⭐️Boran @borandeojan
⭐️Denver @denverr35

👑 Reklam ve İşbirliği 
⭐️Nolan X @nolanbyte

<a href='https://rouletteacademyturkey.vercel.app/'>Sponsor Sitelrimiz</a>
"""

# Mesajları kontrol eden fonksiyon
async def mesaj_kontrol(update: Update, context: CallbackContext) -> None:
    mesaj_text = update.message.text.lower()  # Küçük harfe çevirerek kontrol ediyoruz
    if '!admin' in mesaj_text or 'mod' in mesaj_text:
        # Eğer mesajda !admin veya mod geçiyorsa cevap gönder
        await update.message.reply_text(admin_mesaj, parse_mode=ParseMode.HTML)

def main() -> None:
    # Application oluşturun ve bot token'ınızı iletin
    application = Application.builder().token(BOT_TOKEN).build()

    # Mesajları kontrol eden handler ekleyin
    application.add_handler(MessageHandler(filters.TEXT & filters.Chat(GROUP_ID), mesaj_kontrol))

    # Botu başlatın
    application.run_polling()

if __name__ == '__main__':
    main()
