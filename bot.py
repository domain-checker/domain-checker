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

    reply = f"Hello {user_first_name}! 👋 Enter a domain name to check its registrar via WHOIS data 🔍 and whether it belongs to HSBC:"

    bot.reply_to(message, reply)


@bot.message_handler(func=lambda message: True)
def check_domain(message):
    try:
        w = whois.whois(str(message.text))
        registrar = w.registrar
    except:
        bot.reply_to(message, "Domain does not exist ⚠️")
        return

    if registrar is None:
        bot.reply_to(message, "Domain does not exist ⚠️")
        return

    if not is_hsbc(registrar):
        reply = f"Domain\'s registrar is <b>{registrar}</b> and does <b>not</b> belong to HSBC ❌"
        bot.reply_to(message, reply, parse_mode="HTML")
        return

    reply = f"Domain\'s registrar is <b>{registrar}</b>"
    bot.reply_to(message, reply, parse_mode="HTML")


def is_hsbc(registrar: str):
    return "markmonitor" in registrar.lower()


def main():
    bot.infinity_polling()


if __name__ == "__main__":
    main()
