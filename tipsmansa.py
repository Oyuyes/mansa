# ---------------------------------------------
# tipsmansabot.py — TIPS MANSA Telegram Bot
# Author: Calvin Oyuyo
# Features:
# - VIP Subscription Flow
# - Auto Menu Interaction
# - Payment Options (M-PESA, Binance, PayPal)
# ---------------------------------------------

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from telegram.error import BadRequest
import logging

# Enable logging
logging.basicConfig(level=logging.INFO)

# /start command – shows minimal sequential menu
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🚀 Subscribe to VIP", callback_data="subscribe")],
        [InlineKeyboardButton("📈 View VIP Wins (Last 10 Days)", callback_data="vip_results")],
        [InlineKeyboardButton("📢 Share Our Link", url="https://t.me/tipsmansabot")],
        [InlineKeyboardButton("💬 Chat with Admin", url="https://t.me/oyuyes")],
        [InlineKeyboardButton("📱 WhatsApp", url="https://wa.me/254726376277")]
    ]
    await update.message.reply_text(
        "*Welcome to TIPS MANSA!*\n\nYour gateway to reliable football tips. Choose an option below:",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

# Button interaction handler
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    try:
        await query.answer()
    except BadRequest as e:
        if "Query is too old" in str(e):
            print("⏱️ Ignored expired query.")
            return
        else:
            raise e

    data = query.data

    if data == "subscribe":
        keyboard = [
            [InlineKeyboardButton("📅 1 Week - KES 1,000", callback_data="sub_week")],
            [InlineKeyboardButton("📅 2 Weeks - KES 2,000", callback_data="sub_2weeks")],
            [InlineKeyboardButton("📅 1 Month - KES 3,000", callback_data="sub_month")]
        ]
        await query.edit_message_text(
            "📝 *Choose a VIP subscription plan:*",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown"
        )

    elif data in ["sub_week", "sub_2weeks", "sub_month"]:
        amount = {
            "sub_week": "KES 1,000",
            "sub_2weeks": "KES 2,000",
            "sub_month": "KES 3,000"
        }[data]

        keyboard = [
            [InlineKeyboardButton("📲 M-PESA", callback_data=f"mpesa_{data}")],
            [InlineKeyboardButton("💎 Binance", callback_data=f"binance_{data}")],
            [InlineKeyboardButton("💰 PayPal", callback_data=f"paypal_{data}")]
        ]
        await query.edit_message_text(
            f"💵 *{amount} Payment Options*\nChoose your preferred method:",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown"
        )

    elif data.startswith("mpesa_"):
        await query.edit_message_text(
            "📲 *M-PESA Payment (STK Push)*\n\n"
            "Send to:\n`0726376277` - *TIPS MANSA*\n\n"
            "🧾 Tap below to confirm after payment.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📩 Confirm Payment", callback_data="confirm_payment")]
            ]),
            parse_mode="Markdown"
        )

    elif data.startswith("binance_"):
        await query.edit_message_text(
            "💎 *Binance Payment*\n\nSend to Binance ID:\n"
            "`binance_uid_12345678`\nName: *Calvin Oyuyo*\n\n"
            "🧾 Tap below to confirm after payment.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📩 Confirm Payment", callback_data="confirm_payment")]
            ]),
            parse_mode="Markdown"
        )

    elif data.startswith("paypal_"):
        await query.edit_message_text(
            "💰 *PayPal Payment*\n\nSend to:\n"
            "`oyuyocalvin@gmail.com`\n\nUse *Friends & Family* option.\n"
            "🧾 Tap below to confirm.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📩 Confirm Payment", callback_data="confirm_payment")]
            ]),
            parse_mode="Markdown"
        )

    elif data == "confirm_payment":
        await query.edit_message_text(
            "✅ *Thank you!*\n\nPlease send a screenshot or confirmation message. Admin will activate your VIP access shortly.",
            parse_mode="Markdown"
        )

    elif data == "vip_results":
        await query.edit_message_text(
            "📈 *VIP Wins - Last 10 Days*\n\n"
            "✅ 8 Wins\n❌ 2 Losses\n🔥 +315 Pips Total!\n\n"
            "Start your winning journey with us!",
            parse_mode="Markdown"
        )

# Main function to run the bot
if __name__ == '__main__':
    import os
    TOKEN = os.getenv("7704949627:AAF5loja9V9sdORNClkIDPhkfwMPmJ8PyOs") or "7704949627:AAF5loja9V9sdORNClkIDPhkfwMPmJ8PyOs"  # Replace with your token
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("🤖 TIPS MANSA bot is running...")
    app.run_polling()
