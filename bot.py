import telebot
import time
import sys
from telebot import types
sys.setrecursionlimit(1500)

# bot token number generated via BotFather can be changed accordingly
bot_token = '707051309:AAEjGCQL94X3dEDs5krKPns6DxndJJCwM1Q'
bot = telebot.TeleBot(token=bot_token)


def find_at(msg):  # function to loop through msg and and add in '+'
    searc = ''
    for text in msg:
        if searc == '':
            searc = str(text)
        else:
            searc = searc + "+" + text
    return searc


@bot.message_handler(commands=['start'])  # Bot will send out this message when user uses the start command
def send_welcome(message):
    bot.reply_to(message, 'Welcome i can help you to search on either Google, Google Scholar or Yahoo while in telegram, Please type in either Google, Google Scholar or Yahoo and then what you want me to search and i will give you the results (eg. Google Goodgle)')


@bot.message_handler(func=lambda msg: msg.text is not None) #Based on users preffered platfrom and query, approporiate search results will be provided. 
def at_answer(message1):
    texts = message1.text.split()
    at_text = find_at(texts)
    if len(texts) > 1:
        if texts[1] == 'Scholar' or texts[1] == 'scholar' or texts[1] == 'SCHOLAR':
            bot.reply_to(
                message1, 'https://scholar.google.com.sg/scholar?hl=en&as_sdt=0%2C5&q={}'.format(at_text[15:]))
            bot.reply_to(
                message1, 'If you wish to search again, just send me another query. If you wish stop searching just type and send Stop')
        elif texts[0] == 'Google' or texts[0] == 'google' or texts[0] == 'GOOGLE':
            bot.reply_to(
                message1, 'https://www.google.com/search?q={}'.format(at_text[7:]))
            bot.reply_to(
                message1, 'If you wish to search again, just send me another query. If you wish stop searching just type and send Stop')
        elif texts[0] == 'Yahoo' or texts[0] == 'yahoo' or texts[0] == 'YAHOOO':
            bot.reply_to(
                message1, 'https://search.yahoo.com/search?p={}'.format(at_text[6:]))
            bot.reply_to(
                message1, 'If you wish to search again, just send me another query. If you wish stop searching just type and send Stop')
        else:
            bot.reply_to(
                message1, 'Please type in either Google, Google Scholar or Yahoo before your query to indicate which platfrom to use to search, If you wish stop searching just type and send Stop')
    elif texts[0] == 'stop' or texts[0] == 'STOP' or texts[0] == 'Stop':
        bot.reply_to(
                message1, 'Thanks for using goodgle!')
        return None   
        bot.reply_to(
            message1, 'Please type in either Google, Google Scholar or Yahoo before your query to indicate which platfrom to use to search, If you wish stop searching just type and send Stop')


    

while True: #Exception handling due to unusual behavior by Telegram that stops Bot after few hours
    try:
        bot.polling()
    except Exception:
        time.sleep(15)