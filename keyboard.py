from telebot import types
from language.keyboard_lang import *

# def phone_number():
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#     phone_button = types.KeyboardButton(text="Share your phone number", request_contact=True)
#     keyboard.add(phone_button)
#     return keyboard


def generate_main_menu(lang):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # btn_phone = types.KeyboardButton(text=menu_keyboard[lang])
    btn_toy = types.KeyboardButton(text=toy_keyboard[lang])
    # btn_back = types.KeyboardButton(back_to_start[lang])
    keyboard.row(btn_toy)#btn_phone,
    # keyboard.row(btn_back)
    return keyboard


def generate_language():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn_phone = types.KeyboardButton(text="🇬🇧ENG")
    btn_toy = types.KeyboardButton(text="🇷🇺RU")
    keyboard.row(btn_toy, btn_phone)
    return keyboard


def generate_inline_url(url, lang):
    keyboard = types.InlineKeyboardMarkup()
    btn_more = types.InlineKeyboardButton(text=more[lang], url=url)
    btn_more_bay = types.InlineKeyboardButton(text=buy[lang], callback_data="buy")
    keyboard.row(btn_more_bay, btn_more)
    return keyboard



def generate_pagination(lang):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_next = types.KeyboardButton(text=forward[lang])
    btn_prev = types.KeyboardButton(text=back_menu[lang])
    btn_menu = types.KeyboardButton(text=back_to[lang])
    keyboard.row(btn_prev, btn_next)
    keyboard.row(btn_menu)
    return keyboard 