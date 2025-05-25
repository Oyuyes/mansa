import os
from telegram.ext import ApplicationBuilder
from handlers.start_handler import start_handler
from handlers.button_handler import button_handler
from handlers.member_handler import member_join_handler
from handlers.admin_handler import broadcast_handler
from utils.sheets import check_subscriptions

TOKEN = "7704949627:AAF5loja9V9sdORNClkIDPhkfwMPmJ8PyOs"

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(start_handler)
app.add_handler(button_handler)
app.add_handler(member_join_handler)
app.add_handler(broadcast_handler)

# Schedule daily subscription check
app.job_queue.run_daily(check_subscriptions, time=datetime.time(hour=9, minute=0))

print("🤖 TIPS MANSA bot is running.")
app.run_polling()
