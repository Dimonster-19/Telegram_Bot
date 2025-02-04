import telebot
from extensions import APIException, Converter
from Config import money, TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ["help", "start"])
def helper (message: telebot.types.Message):
    text = "Добрый день, дамы и господа! Этот бот может помочь Вам узнать стоимость определенных валют. Чтобы начать пользоваться ботом, введите команды в следующем порядке:\n валюты>\
            <во что перевести>\
            <количество>\
            Чтобы посмотреть список валют - введите команду '/values'"
    bot.reply_to(message, text)

@bot.message_handler(commands = ['values'])
def cash(message: telebot.types.Message):
    text = "Доступные валюты"
    for coin in money.keys():
        text = "\n".join((text, coin, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types= ["text", ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(" ")

        if len(values) !=3:
            raise APIException("Введенных параметров должно быть три. Попробуйте еще раз!")

        base, quote, amount = values
        result = Converter.get_price(base, quote, amount)

    except Exception as e:
        bot.reply_to (message, f"Недопустимая ошибка пользователя \n {e}")
    except Exception as e:
        bot.reply_to(message, f"Не удалось обработать команду: \n{e}")

    else:
        answer = f"Цена {amount} {base} в {quote} - {result}"
        bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True)
