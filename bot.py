import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask
from threading import Thread
import os

# --- 1. إعداد السيرفر (للحفاظ على عمل البوت 24/7) ---
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_server():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# تشغيل السيرفر في خلفية منفصلة
thread = Thread(target=run_server)
thread.start()

# --- 2. كود البوت الخاص بك ---
BOT_TOKEN = "8278573609:AAHAXRsqPZZiw7zzvqJ9vFIqG-Fnk3UiCYs"
bot = telebot.TeleBot(BOT_TOKEN)

def main_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("1️⃣ أساسيات الإلكترونيات", callback_data="cat1"),
        InlineKeyboardButton("2️⃣ المحاكاة والتجربة", callback_data="cat2"),
        InlineKeyboardButton("3️⃣ برامج التصميم (PCB)", callback_data="cat3"),
        InlineKeyboardButton("4️⃣ مراجع و داتا شيت", callback_data="cat4")
    )
    return markup

def menu_cat1():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("Arduino Docs", url="https://docs.arduino.cc/learn/"),
        InlineKeyboardButton("Electronics Tutorials", url="https://www.electronics-tutorials.ws/"),
        InlineKeyboardButton("All About Circuits", url="https://www.allaboutcircuits.com/textbook/"),
        InlineKeyboardButton("Instructables", url="https://www.instructables.com/circuits/"),
        InlineKeyboardButton("CircuitDigest", url="https://circuitdigest.com/"),
        InlineKeyboardButton("🔙 العودة", callback_data="back_to_main")
    )
    return markup

def menu_cat2():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("Wokwi", url="https://wokwi.com/"),
        InlineKeyboardButton("LabEx", url="https://labex.io/projects"),
        InlineKeyboardButton("EDA Playground", url="https://www.edaplayground.com/x/A4"),
        InlineKeyboardButton("Tinkercad", url="https://www.tinkercad.com/circuits"),
        InlineKeyboardButton("Falstad", url="https://www.falstad.com/circuit/"),
        InlineKeyboardButton("🔙 العودة", callback_data="back_to_main")
    )
    return markup

def menu_cat3():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("EasyEDA", url="https://easyeda.com/editor-mobile/"),
        InlineKeyboardButton("KiCad", url="https://www.kicad.org/"),
        InlineKeyboardButton("Altium", url="https://www.altium.com/"),
        InlineKeyboardButton("PCBWay", url="https://www.pcbway.com/"),
        InlineKeyboardButton("JLCPCB", url="https://jlcpcb.com/"),
        InlineKeyboardButton("🔙 العودة", callback_data="back_to_main")
    )
    return markup

def menu_cat4():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("Electronics Lab", url="https://www.electronics-lab.com/"),
        InlineKeyboardButton("AllDataSheet", url="https://www.alldatasheet.com/"),
        InlineKeyboardButton("Octopart", url="https://octopart.com/"),
        InlineKeyboardButton("DigiKey", url="https://www.digikey.com/en/resources"),
        InlineKeyboardButton("Mouser", url="https://www.mouser.com/"),
        InlineKeyboardButton("🔙 العودة", callback_data="back_to_main")
    )
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_listener(call):
    bot.answer_callback_query(call.id)
    if call.data == "cat1": bot.edit_message_text("📘 الأساسيات:", call.message.chat.id, call.message.message_id, reply_markup=menu_cat1())
    elif call.data == "cat2": bot.edit_message_text("🚀 المحاكاة:", call.message.chat.id, call.message.message_id, reply_markup=menu_cat2())
    elif call.data == "cat3": bot.edit_message_text("🖥️ التصميم:", call.message.chat.id, call.message.message_id, reply_markup=menu_cat3())
    elif call.data == "cat4": bot.edit_message_text("🔍 المراجع:", call.message.chat.id, call.message.message_id, reply_markup=menu_cat4())
    elif call.data == "back_to_main": bot.edit_message_text("مرحباً بك! اختر فئة:", call.message.chat.id, call.message.message_id, reply_markup=main_menu())

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "مرحباً بك في منصة الهندسة الإلكترونية الدراسية! ⚡\nاختر فئة للبدء:", reply_markup=main_menu())

if __name__ == "__main__":
    bot.infinity_polling()
