import telegram.ext.filters
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def bb(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'goodbye {update.effective_user.first_name}')


async def msg(update, context):
    file_to_download = await update.message.document.get_file()
    file_path = await file_to_download.download_to_drive()

    print(type(file_path))
    print(file_path)
    await update.message.reply_text(str(file_path))


app = ApplicationBuilder().token("5909752196:AAH1HBAfHTMvSIZNdDY0Qlzw4aqCjDCpOjU").build()

app.add_handler(CommandHandler("hello", hello))

app.add_handler(CommandHandler("goodbye", bb))

app.add_handler(MessageHandler(filters.Document.FileExtension("txt"), msg))

app.run_polling()
