import random
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8079517120:AAHss6Sv-kuDMNSedKkEvZOeIP-XptiuBh0"
users = {}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    users[chat_id] = {"secret_number": random.randint(1, 10), "attempts": 3}
    await update.message.reply_text("Salom! Men 1 dan 10 gacha son o‘yladim. Uni topishga harakat qiling!")


async def guess(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    if chat_id not in users:
        users[chat_id] = {"secret_number": random.randint(1, 10), "attempts": 3}

    try:
        guess = int(update.message.text)
        user_data = users[chat_id]

        if user_data["attempts"] > 0:
            if guess == user_data["secret_number"]:
                await update.message.reply_text("Tabriklayman! Siz to‘g‘ri topdingiz! 😊")
                users.pop(chat_id)
            elif guess < user_data["secret_number"]:
                user_data["attempts"] -= 1
                await update.message.reply_text(f"Kattaroq son kiriting! Qolgan urinishlar: {user_data['attempts']}")
            else:
                user_data["attempts"] -= 1
                await update.message.reply_text(f"Kichikroq son kiriting! Qolgan urinishlar: {user_data['attempts']}")

            if user_data["attempts"] == 0:
                await update.message.reply_text(
                    f"Sen ahmoqsan! 🤦‍♂️ Men {user_data['secret_number']} sonini o‘ylagan edim.")
                users.pop(chat_id)
    except ValueError:
        await update.message.reply_text("Iltimos, faqat son kiriting!")


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, guess))

    print("Bot ishga tushdi...")
    app.run_polling()


if __name__ == "__main__":
    main()
