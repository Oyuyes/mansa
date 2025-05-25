from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from utils.sheets import fetch_latest_odds

MAIN_MENU = InlineKeyboardMarkup([
    [InlineKeyboardButton("✅ Subscribe to VIP", callback_data="subscribe")],
    [InlineKeyboardButton("📊 View Sample Odds", callback_data="sample_odds")],
    [InlineKeyboardButton("📣 Share Our Bot", url="https://t.me/share/url?url=https://t.me/tipsmansabot")],
    [InlineKeyboardButton("💬 Chat with Admin", url="https://t.me/calvo")],
    [InlineKeyboardButton("📱 WhatsApp", url="https://wa.me/254726376277")]
])

PAYMENT_MENU = InlineKeyboardMarkup([
    [InlineKeyboardButton("1 Week - KES 1000", callback_data="pay_mpesa")],
    [InlineKeyboardButton("2 Weeks - KES 2000", callback_data="pay_mpesa")],
    [InlineKeyboardButton("1 Month - KES 3000", callback_data="pay_mpesa")],
    [InlineKeyboardButton("💰 Pay with Binance", callback_data="pay_binance")],
    [InlineKeyboardButton("💳 Pay with PayPal", callback_data="pay_paypal")]
])

def get_latest_odds():
    odds = fetch_latest_odds()
    if odds:
        return (
            f"*Today's Sample Odds:*\n\n"
            f"🏟 {odds['match']}\n"
            f"💡 Tip: {odds['tip']}\n"
            f"✅ Odds: {odds['odds']}\n\n"
            "_Updated daily by the TIPS MANSA team._"
        )
    else:
        return "No odds available at the moment. Please check back later."
