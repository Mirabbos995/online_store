import telebot
from keyboard import *
from language.bot_lang import *
from language.keyboard_lang import *
from telebot.types import LabeledPrice
# from repository.smartphone_db import Smartphone
from repository.toy_db import Postgres_toy
import os
user_langs = {}



token = os.getenv("TOKEN")
click_token = os.getenv("CLICK_TOKEN")
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.chat.id
    lang = bot.send_message(chat_id, "🇬🇧Choose language!\n\n🇷🇺Выберите язык!", reply_markup=generate_language())
    bot.register_next_step_handler(lang, menu)



def menu(message):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, "eng")
    if message.text == '🇬🇧ENG':
        lang = 'eng'
        photo = open('photo/img.png', 'rb')
        bot.send_photo(chat_id, photo, caption=caption[lang])

    if message.text == '🇷🇺RU':
        lang = 'ru'
        photo = open('photo/img.png', 'rb')
        bot.send_photo(chat_id, photo, caption=caption[lang])
    catalog = bot.send_message(chat_id, select_catalog[lang], reply_markup=generate_main_menu(lang))
    bot.register_next_step_handler(catalog, main_catalogs)
    user_langs[chat_id] = lang

def main_catalogs(message, product_id=0, products=None):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id)
    if message.text == back_to[lang]:
        return start(message)

    # if message.text == menu_keyboard:
    #     products = Smartphone().select_data()

    if message.text == toy_keyboard[lang]:
        products = Postgres_toy().select_data()

    if message.text == back_to[lang]:
        return start(message)

    if message.text == forward[lang] and product_id < len(products):
        product_id += 1

    elif message.text == back_menu[lang] and product_id > 0:
        product_id -= 1

    product = products[product_id]
    product_title = product[0]
    photo = product[1]
    product_price = product[2]
    product_url = product[3]
    bot.send_photo(chat_id, photo, caption=name[lang] + f': {product_title}\n\n'
                                               f'Product cost: {product_price}',
                       reply_markup=generate_inline_url(product_url, lang))

    user_message = bot.send_message(chat_id, we_have[lang] + f": {len(products) - (product_id + 1)}", reply_markup=generate_pagination(lang))

    if message.text == forward[lang] and len(products) - (product_id + 1) == 0:
        bot.send_message(chat_id, no_goods[lang])
        product_id = product_id - len(products)

    bot.register_next_step_handler(user_message, main_catalogs, product_id, products)

@bot.callback_query_handler(func=lambda call: True)
def payments(call):
    chat_id = call.message.chat.id
    product_price_data = ''
    if call.data == "buy":
        product_info = call.message.caption
        product = product_info.split(':')
        product_name = product[1].replace("Product characteristics", "")
        description = product[2]
        product_price = product[-1].replace('сум', "") # " 2 700 00" -> "270000"
        for x in product_price:
            if x.isdigit():
                product_price_data += x

        INVOICE = {
            "title": product_name,
            "description": description,
            "invoice_payload": "bot-defined invoice payload",
            "provider_token": click_token,
            "start_parameter": "pay",
            "currency": "UZS",
            "prices": [LabeledPrice(label=product_name, amount=int(product_price_data + '00'))]
        }

        bot.send_invoice(chat_id, **INVOICE)
        bot.register_next_step_handler(call.message, successful_payment)

@bot.pre_checkout_query_handler(func=lambda query: True)
def invoice_checkout(query):
    bot.answer_pre_checkout_query(query.id, ok=True, error_message="Payment error")


def successful_payment(message):
    bot.send_message(message.chat.id, "The payment was made successfully!")
    return menu(message)

bot.polling(non_stop=True)
