import telebot
import time
from telebot import types
bot_token='6839796095:AAH2rCz2oXiwrgifSFRxKLLvkwRiRe9Pe0c'
bot=telebot.TeleBot(token=bot_token)

aruzhan_id="805798099"
miras_id="894349873"
def is_aruzhan(user_id):
    return str(user_id) == aruzhan_id

@bot.message_handler(commands=["start"])
def hello(message):
    if is_aruzhan(message.chat.id):
        message_text = (
            "Привет, Аружан! 🌹✨ Я написал этого бота, чтобы <b>поздравить</b> тебя с <i>14 февраля</i> 💖. "
            "Пусть этот день будет наполнен любовью, теплом и вниманием! 💌"
        )

        bot.send_message(message.chat.id, message_text, parse_mode='HTML')

        time.sleep(1)
        item1 = types.InlineKeyboardButton("😊 Эмодзи", callback_data="1")
        item2 = types.InlineKeyboardButton("💌 Сообщение", callback_data="2")
        item3 = types.InlineKeyboardButton("🎤 Голосовое сообщение", callback_data="3")
        item4 = types.InlineKeyboardButton("📸 Фоточки", callback_data="4")
        item5 = types.InlineKeyboardButton("💖 Комплименты", callback_data="5")
        markup = types.InlineKeyboardMarkup()
        markup.add(item1, item2, item3, item4, item5)
        bot.send_message(message.chat.id, "Нажми на одну из пяти кнопок!", reply_markup=markup)
    else:
        bot.send_message(message.chat.id,"Сорри но вы не Аружан")
        print(message.chat.id)

@bot.callback_query_handler(func=lambda call: True)
def check(call):
    if call.data =="1":
        send_emoji(call)

    elif call.data =="2":
        send_messages(call)

    elif call.data =="3":
        send_voice(call)
    elif call.data =="4":
        send_photo(call)
    elif call.data =="5":
        send_compliments(call)
def send_voice(call):
    with open("media/Эщкере.mp3", 'rb') as audio:
        bot.send_audio(call.message.chat.id, audio, caption="Для крутышки записал")

def send_messages(call):
    message_text = (
        "<b>Валентинка для Тажибаевой Аружан из 11А класса 💌</b>\n\n"
        "По моему скромному мнению, ты - <i>самая крутая, самая вайбовая, самая-самая</i> одноклассница, с которой весело проводить время. 🌟✨\n"
        "Твоя улыбка освещает день лучше солнца, а твой смех заражает всех вокруг позитивом. Ты не просто одноклассница, ты - истинный свет в нашем классе, делающий каждый день ярче. 🌈🎉\n\n"
        "P.S. От неизвестного писателя,точно не от 'крутышки-мартышки'"
    )
    bot.send_message(call.message.chat.id, message_text, parse_mode="HTML")

def send_compliments(call):
    bot.send_message(call.message.chat.id, "Лови парочку комплиментов:")
    messages = [
        "Твоя улыбка освещает весь мир вокруг.",
        "Ты обладаешь невероятной энергетикой.",
        "В твоих глазах столько глубины и тепла.",
        "Ты воплощение элегантности.",
        "Ты очень талантлива во всем, чем занимаешься.",
        "Твой стиль просто безупречен.",
        "Твой смех заражает позитивом.",
        "Ты невероятно умная и остроумная.",
        "В тебе столько силы и вдохновения.",
        "Ты особенная, как звезда на небе.",
        "Твое присутствие делает день лучше.",
        "Ты обладаешь потрясающей интуицией.",
        "Ты истинный источник вдохновения.",
        "Твоя доброта безгранична.",
        "Ты умеешь видеть красоту в мелочах.",
        "Ты как солнечный луч в пасмурный день.",
        "Твоя уверенность в себе вдохновляет.",
        "Ты просто ослепительна.",
        "Твоя искренность ценна и редка.",
        "Ты неповторима в каждом смысле этого слова.",
        "Ты просто ЭЩКЕРЕЕЕЕЕЕ.",
        "Ты КРУТО ЙОУ ЙОУ",
        "Скидываем розочки лайк басамыз",
    ]
    for i in messages:
        bot.send_message(call.message.chat.id, i)
        time.sleep(2)

def send_emoji(call):
    bot.send_message(call.message.chat.id, "Лови стикеры для настроения")
    for i in range(1, 6):
        with open(f"media/sticker ({i}).tgs", 'rb') as sticker:
            bot.send_sticker(call.message.chat.id, sticker)
    for i in range(6, 10):
        with open(f"media/sticker ({i}).webp", 'rb') as sticker:
            bot.send_sticker(call.message.chat.id, sticker)

def send_photo(call):
    messages=["Эщкере","Круто","Йоу","Сисі","Ты че вытыкаешь?","Че зыришь глаза пузыришь","МЕГА КРУТО"]
    bot.send_message(call.message.chat.id, "Лови лютые фоточки")
    for i in range(1, 7):
        with open(f"media/pic ({i}).jpg", 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo,caption=messages[i-1])



bot.infinity_polling()
