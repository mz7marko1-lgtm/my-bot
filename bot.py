import os
from threading import Thread
from flask import Flask
from telebot import types
import telebot

# ------------------ 1. تهيئة خادم Flask لخدمة Render ------------------
app = Flask("")


@app.route("/")
def home():
  return "Bot is alive and running!"


def run():
  port = int(os.environ.get("PORT", 8080))
  app.run(host="0.0.0.0", port=port)


def keep_alive():
  t = Thread(target=run)
  t.start()


# ------------------ 2. تهيئة التوكن والبوت ------------------
TOKEN = os.environ.get(
    "BOT_TOKEN", "8278573609:AAHTK3-kghgQtVB7JAKjLyZtl_LU_3dQPzc"
)
bot = telebot.TeleBot(TOKEN)

# ------------------ 3. القوائم والأزرار التفاعلية ------------------


@bot.message_handler(commands=["start"])
def send_welcome(message):
  markup = types.InlineKeyboardMarkup(row_width=2)

  btn_sim = types.InlineKeyboardButton(
      "🌐 مواقع المحاكاة", callback_data="simulation"
  )
  btn_books = types.InlineKeyboardButton(
      "📚 المراجع والكتب", callback_data="books"
  )
  btn_explain = types.InlineKeyboardButton(
      "🔧 شروحات المكونات", callback_data="components"
  )
  btn_control = types.InlineKeyboardButton(
      "⚙️ أنظمة التحكم", callback_data="control"
  )

  markup.add(btn_sim, btn_books, btn_explain, btn_control)

  welcome_text = (
      "مرحباً بك في منصة الهندسة الإلكترونية الدراسية! ⚡\n\n"
      "هذا البوت مصمم خصيصاً لطلاب ومحبي تكنولوجيا وهندسة الإلكترونيات، "
      "ليجمع لك كل ما تحتاجه في مكان واحد:\n"
      "🌐 أفضل مواقع محاكاة الدوائر (Simulation)\n"
      "📚 المراجع والكتب الدراسية المعتمدة\n"
      "🔧 شروحات تفصيلية للمكونات الإلكترونية وأنظمة التحكم.\n\n"
      "اختر من القائمة أدناه للبدء:"
  )

  bot.reply_to(message, welcome_text, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_listener(call):
  if call.data == "simulation":
    bot.answer_callback_query(call.id)
    bot.send_message(
        call.message.chat.id,
        "🌐 **أبرز مواقع المحاكاة:**\n- EasyEDA\n- EDA Playground\n- Falstad Circuit Simulator",
    )
  elif call.data == "books":
    bot.answer_callback_query(call.id)
    bot.send_message(
        call.message.chat.id,
        "📚 **قسم المراجع:**\nستجد هنا الكتب المعتمدة والحلول.",
    )
  elif call.data == "components":
    bot.answer_callback_query(call.id)
    bot.send_message(
        call.message.chat.id,
        "🔧 **شروحات المكونات:**\n- Transistors (BJT / MOSFET)\n- Operational Amplifiers\n- Voltage Regulators",
    )
  elif call.data == "control":
    bot.answer_callback_query(call.id)
    bot.send_message(
        call.message.chat.id,
        "⚙️ **أنظمة التحكم:**\nشروحات الـ Block Diagrams وحسابات Transfer Functions و Routh-Hurwitz Criterion.",
    )


# ------------------ 4. التشغيل النهائي ------------------
if __name__ == "__main__":
  keep_alive()
  bot.infinity_polling(non_stop=True)
