from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from utils.sheets import get_subscribers

ADMIN_ID = 123456789  # Replace with your Telegram user ID

async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("❌ You are not authorized to use this command.")
        return

    message = ' '.join(context.args)
    if not message:
        await update.message.reply_text("Please provide a message to broadcast.")
        return

    subscribers = get_subscribers()
    for user_id in subscribers:
        try:
            await context.bot.send_message(chat_id=user_id, text=message)
        except Exception as e:
            print(f"Failed to send message to {user_id}: {e}")

broadcast_handler = CommandHandler("broadcast", broadcast)
