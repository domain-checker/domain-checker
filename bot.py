import os

import telebot
import whois

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    try:
        user_first_name = message.from_user.first_name
    except AttributeError:
        user_first_name = "User"

    reply = f"Hello {user_first_name}! This is a simple telegram bot to check the registrar for a given domain via WHOIS data😃. Just enter your domain name🔍"

    bot.reply_to(message, reply)


@bot.message_handler(func=lambda message: True)
def checkDomain(message):
    w = whois.whois(str(message.text))
    registrar = w.registrar
    if registrar is None:
        bot.reply_to(message, "Domain does not exist")
    else:
        reply = f"Registrar is {registrar}"
        bot.reply_to(message, reply)


def main():
    bot.infinity_polling()


if __name__ == "__main__":
    main()
