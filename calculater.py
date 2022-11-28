import telebot
bot=telebot.TeleBot("5920503633:AAGh39hYruYHO8B8PPNq-Fkdy7ZBTRewOfI")

@bot.message_handler(commands=["start,calculater"])
def getmessage(messange):
    bot.send_message( message.from_user.id, "Привет! ")

bot.polling(non_stop=False,interval=0)

bot.send_message(messange.from_user.id, "Привет!",reply_markup=keyboard)


