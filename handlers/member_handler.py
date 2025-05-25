from telegram.ext import ChatMemberHandler, ContextTypes
from telegram import Update

async def greet_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.chat_member.new_chat_members:
        await context.bot.send_message(
            chat_id=update.chat_member.chat.id,
            text=f"👋 Welcome {member.mention_html()} to *TIPS MANSA*! Let's win together! 💰",
            parse_mode="HTML"
        )

member_join_handler = ChatMemberHandler(greet_new_member, ChatMemberHandler.CHAT_MEMBER)
