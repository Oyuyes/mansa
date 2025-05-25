from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CommandHandler, CallbackQueryHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📥 Subscribe to VIP", callback_data="subscribe")],
        [InlineKeyboardButton("🔥 View Our VIP Wins", callback_data="view_wins")],
        [InlineKeyboardButton("🎯 Sample Odds", callback_data="sample_odds")],
        [InlineKeyboardButton("📢 Share Our Link", switch_inline_query="🔥 Get Daily 2+ Odds - @tipsmansabot")],
        [InlineKeyboardButton("🗣️ Chat with Admin", url="https://t.me/calvo")],
        [InlineKeyboardButton("💬 WhatsApp", url="https://wa.me/254726376277")]
    ]
    await update.message.reply_text(
        "🎉 Welcome to TIPS MANSA!\n\n💰 Get daily 2+ odds to double your money. Subscribe to start winning today!",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "subscribe":
        keyboard = [
            [InlineKeyboardButton("1 Week - Ksh 1000", callback_data="pay_1w")],
            [InlineKeyboardButton("2 Weeks - Ksh 2000", callback_data="pay_2w")],
            [InlineKeyboardButton("1 Month - Ksh 3000", callback_data="pay_1m")]
        ]
        await query.edit_message_text("Choose your subscription period:", reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif data == "view_wins":
        await query.edit_message_text("📊 VIP Winning Record (Last 10 Days)\n\n✅ Day 1: 2.4 odds\n✅ Day 2: 2.1 odds...\n\n🔥 Want to join? Click Subscribe!")

menu_handler = CommandHandler("start", start)
callback_handler = CallbackQueryHandler(button_callback, pattern="^(subscribe|view_wins)$")
