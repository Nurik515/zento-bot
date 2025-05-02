from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "7651020708:AAE55lbMYpgBvNe82XLUnheBgWf1wleqchI"

main_menu = [["🇪🇺 Работа в Европе", "📄 Помощь с документами"]]
job_menu = [
    ["🚚 Водитель", "🔧 Сварщик"],
    ["🧱 Подсобный рабочий", "🧹 Домработница"],
    ["🚜 Спецтехника", "📋 Общие вакансии"],
    ["🔙 Назад"]
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Ассаламу алейкум! 🧑‍🦱👩‍🦰\n\nЧем можем помочь?\nВыберите интересующий раздел:",
        reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True)
    )

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🇪🇺 Работа в Европе":
        await update.message.reply_text("Выберите профессию:", reply_markup=ReplyKeyboardMarkup(job_menu, resize_keyboard=True))

    elif text == "📄 Помощь с документами":
        await update.message.reply_text("Здесь будет информация о документах. Мы добавим подробности вручную.")

    elif text in ["🚚 Водитель", "🔧 Сварщик", "🧱 Подсобный рабочий", "🧹 Домработница", "🚜 Спецтехника", "📋 Общие вакансии"]:
        await update.message.reply_text(f"Пока нет вакансий по категории: {text}.\n\nНажмите 🔙 Назад.")

    elif text == "🔙 Назад":
        await update.message.reply_text(
            "Чем можем помочь?\nВыберите интересующий раздел:",
            reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True)
        )

    else:
        await update.message.reply_text("Пожалуйста, выберите кнопку из меню.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, message_handler))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()












