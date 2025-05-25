from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from utils.constants import MAIN_MENU

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = (
        "👑 *Welcome to TIPS MANSA VIP!*\n\n"
        "🔥 We deliver *2+ odds daily*, carefully selected to *double your money*. 💸\n"
        "📊 Our betting tips are premium, researched, and trusted.\n\n"
        "👇 Tap a button below to begin your winning journey!"
    )
    await update.message.reply_text(message, reply_markup=MAIN_MENU, parse_mode="Markdown")

start_handler = CommandHandler("start", start)
