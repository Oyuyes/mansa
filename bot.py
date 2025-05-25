import logging
from telegram.ext import ApplicationBuilder
from config import TOKEN
from handlers.menu import menu_handler, callback_handler
from handlers.subscription import subscription_callback_handler
from handlers.odds import odds_handler
from handlers.admin import new_member_handler

logging.basicConfig(level=logging.INFO)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(menu_handler)
app.add_handler(callback_handler)
app.add_handler(subscription_callback_handler)
app.add_handler(odds_handler)
app.add_handler(new_member_handler)

if __name__ == "__main__":
    print("Bot running...")
    app.run_polling()
