import telebot

bot=telebot.TeleBot("5920503633:AAGh39hYruYHO8B8PPNq-Fkdy7ZBTRewOfI")

@bot.message_handler(commands=["start, calculater"])
def getMessage(message):
    bot.send_message(message.from_user.id,"Привет")

bot.polling(none_stop=False,interval=0)