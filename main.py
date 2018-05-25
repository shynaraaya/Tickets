from constants import TOKEN
from messages import HELLO, HELP, ALMATYTOASTANA, ALMATYTOAKTAU, ALMATYTOAKTOBE, ALMATYTOATYRAU, ALMATYTOPAVLODAR, ALMATYTOURALSK, ALMATYTOUST, ALMATYTOKRG, ALMATYTOKOST, ALMATYTOSHYMKENT
from telebot import types
import messages
import database
import random
import telebot
import requests



bot = telebot.TeleBot(TOKEN)
current_shown_dates={}


markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn2 = types.KeyboardButton('Astana')
itembtn3 = types.KeyboardButton('Aktau')
itembtn4 = types.KeyboardButton('Aktobe')
itembtn5 = types.KeyboardButton('Atyrau')
itembtn6 = types.KeyboardButton('Pavlodar')
itembtn7 = types.KeyboardButton('Uralsk')
itembtn8 = types.KeyboardButton('Ust-Kamenogorsk')
itembtn9 = types.KeyboardButton('Karaganda')
itembtn10 = types.KeyboardButton('Kostanai')
itembtn11 = types.KeyboardButton('Shymkent')
markup.row(itembtn2, itembtn7)
markup.row(itembtn3, itembtn8)
markup.row(itembtn4, itembtn9)
markup.row(itembtn5, itembtn10)
markup.row(itembtn6, itembtn11)



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, messages.HELLO)

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(message.chat.id, messages.HELP)


@bot.message_handler(commands=['inAlmaty'])
def location(message):

    print('inserted')
    bot.send_message(message.chat.id, "Choose the city you are going to fly to:", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): 
    
    if message.text=="Astana":
        bot.send_message(message.chat.id,random.choice([ALMATYTOASTANA]))
    if message.text=="Aktau":
        bot.send_message(message.chat.id,random.choice([ALMATYTOAKTAU]))
    if message.text=="Aktobe":
        bot.send_message(message.chat.id,random.choice([ALMATYTOAKTOBE]))
    if message.text=="Atyrau":
        bot.send_message(message.chat.id,random.choice([ALMATYTOATYRAU]))
    if message.text=="Pavlodar":
        bot.send_message(message.chat.id,random.choice([ALMATYTOPAVLODAR]))
    if message.text=="Uralsk":
        bot.send_message(message.chat.id,random.choice([ALMATYTOURALSK]))
    if message.text=="Ust-Kamenogorsk":
        bot.send_message(message.chat.id,random.choice([ALMATYTOUST]))
    if message.text=="Karaganda":
        bot.send_message(message.chat.id,random.choice([ALMATYTOKRG]))
    if message.text=="Kostanai":
        bot.send_message(message.chat.id,random.choice([ALMATYTOKOST]))
    if message.text=="Shymkent":
        bot.send_message(message.chat.id,random.choice([ALMATYTOSHYMKENT]))
     
     

if __name__ == '__main__':
    
    print('Starting AirTickets')
    bot.polling()