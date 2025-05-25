from telegram import Update
from telegram.ext import CallbackQueryHandler, ContextTypes
from utils.constants import PAYMENT_MENU, get_latest_odds

async def button_handler_func(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "subscribe":
        await query.edit_message_text(
            "🎯 Choose your subscription period:",
            reply_markup=PAYMENT_MENU
        )
    elif query.data == "sample_odds":
        odds = get_latest_odds()
        await query.edit_message_text(odds, parse_mode="Markdown")
    elif query.data == "pay_mpesa":
        await query.edit_message_text(
            "✅ Pay via M-PESA Till Number:\n\n"
            "*Till Number:* 5455121\n"
            "*Business Name:* RNS\n"
            "*Amount:* As per your chosen plan\n\n"
            "_After payment, reply 'I have paid' and we will confirm ASAP._",
            parse_mode="Markdown"
        )
    elif query.data == "pay_binance":
        await query.edit_message_text("💰 Binance Payment:\n\nSend to Binance ID: `BINANCE-ID-12345`")
    elif query.data == "pay_paypal":
        await query.edit_message_text("💳 PayPal:\n\nSend to: `oyuyocalvin@gmail.com`")
    else:
        await query.edit_message_text("❗ Unknown option.")

button_handler = CallbackQueryHandler(button_handler_func)
