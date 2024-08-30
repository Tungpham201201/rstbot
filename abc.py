import telebot
import random

TOKEN = '7264904413:AAGraTZ4isP4qY_OQBTEXmeAh6-5aGPk5Og'
bot = telebot.TeleBot(TOKEN)

user_counts = {}
random_words = ['Xin chào', 'Hello', 'Ok', 'Huhu', 'Hihi']
emojis = ['❤️', '😊', '👍', '🎉', '🌟', '🔥', '💯', '🙌', '😎', '🤩']

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_id = message.from_user.id
    if user_id in user_counts:
        user_counts[user_id] += 1
    else:
        user_counts[user_id] = 1
    random_word = random.choice(random_words)
    random_emoji = random.choice(emojis)
    response = f"{user_counts[user_id]}. {random_word} {random_emoji}"
    bot.reply_to(message, response)
bot.polling()