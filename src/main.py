import telebot
import base
from singer import Singer

bot = telebot.TeleBot(base.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    msg = bot.send_message(chat_id=message.chat.id, text='لطفا نام خواننده را وارد کنید:')
    bot.register_next_step_handler(message=msg, callback=get_singer_musics)


def get_singer_musics(message):
    singer = Singer(message.text)
    musics = singer.musics()
    for music in musics:
        bot.send_audio(chat_id=message.chat.id, audio=music.get('Music_320'))


if __name__ == '__main__':
    bot.infinity_polling()
