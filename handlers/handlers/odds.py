from telegram import Update
from telegram.ext import CallbackQueryHandler, ContextTypes

sample_odds_text = "🎯 Today's Sample Odds\n\n🏟️ Arsenal vs Chelsea - Over 2.5\n🏟️ Milan vs Napoli - BTTS\nOdds: 2.2"

async def sample_odds(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(sample_odds_text)

odds_handler = CallbackQueryHandler(sample_odds, pattern="^sample_odds$")
