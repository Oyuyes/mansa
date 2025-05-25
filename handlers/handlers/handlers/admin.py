from telegram.ext import ChatMemberHandler, ContextTypes
from telegram import Update

async def welcome_new(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.chat_member.new_chat_members:
        await context.bot.send_message(
            chat_id=member.id,
            text="🎉 Welcome to TIPS MANSA!\n\n💰 Get daily 2+ odds to double your money. Use /start to get started!"
        )

new_member_handler = ChatMemberHandler(welcome_new, ChatMemberHandler.CHAT_MEMBER)
