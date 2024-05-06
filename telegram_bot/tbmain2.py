#Прописать в BotFather /newbot.Затем назвать своего бота,затем прописать название без пробелов
#t.me/InsPekToP_test_bot
#pip install pyTelegramBotAPI

import telebot

bot = telebot.TeleBot('тут должен быть ТОКЕН')

#чтобы онаобрабатывала несколько комманд,пишем несколько команд
#поддерживает кирилицу
@bot.message_handler(commands=['start','main','hello','привет'])
def main(message):
    #bot.send_message(message.chat.id,'Привет!')
    #bot.send_message(message.chat.id,message) #выбивает инфу о польз-ле
    bot.send_message(message.chat.id, f'Привет,{message.from_user.first_name}')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id,'<b>Инфа</b> о <em><u>помощи</u></em>',parse_mode='html')
#parse_mode='html' - теперь можем добавлять стили к 'Инфа о помощи(форматировать строку)

#декоратор bot.message_handler(commands обрабатывает команды.Но если надо текст
@bot.message_handler() #просто не помещать пар-ты
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Хеллоу,{message.from_user.first_name}')
    elif message.text.lower()=='id':
        bot.reply_to(message,f'ID: {message.from_user.id}')
#reply_to в формате ответа на прошлое смс





#прога выполнилась и закрылась
bot.polling(non_stop=True)# Чтобы она постоянно выполнялась
#bot.infinity_polling() #тоже самое
