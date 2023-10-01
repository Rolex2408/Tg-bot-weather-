import telebot
import requests

TOKEN = "6473289822:AAFG_6amBEANJ0uqOwJP6cSOt0noJsijXaU"
API_KEY = "385a320e478aab07130c188843a29657"


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Доброго дня! Введіть назву міста на будь-якій мові")

@bot.message_handler(commands=['developer'])
def send_welcome(message):
    bot.reply_to(message, "Рамус Ілля, іпс-22")

@bot.message_handler(func=lambda message: True)
def get_weather(message):
    city = message.text
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url).json()
        temp = response['main']['temp']
        description = response['weather'][0]['description']
        weather_info = f"Погода в {city}: {temp}°C, {description}"
        bot.reply_to(message, weather_info)
    except:
        bot.reply_to(message,
                     "Не вдалось отримати прогноз погоди. Будь ласка, переконайтеся, що ви написали коректну назву міста.")

