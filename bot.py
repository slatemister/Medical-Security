#!/usr/bin/python3
# -*- coding: utf-8 -*-
from aiogram import Bot, Dispatcher,executor,types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.markdown import hlink
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from answers import ans2,ans3_1,ans3_3_1,ans3_3_2,ans3_3_3,ans3_3_4,ans4_1,ans4_2,ans4_3,ans4_4,ans3_3_5,\
    ans3_3_6,ans4_5,ans4_6,ans3_3_7,ans3_3_8,ans3_3_9,ans5
from link import link4_1,link4_4,link3_3_2,link4_3_1,link4_2,link3_3_3,link3_3_4,link4_3_2, \
    link2,link3_3_5,link3_3_6,link3_3_7,link3_3_8,link3_3_9,link4_5_1,link4_5_2,link4_6
import os

PATH = os.path.split(os.path.abspath(__file__))[0]
token_file = PATH + '/token.txt'

token = open(token_file).read().strip('\n\t ')
bot=Bot(token=token,parse_mode=types.ParseMode.HTML)
dp=Dispatcher(bot, storage=MemoryStorage())

available_categories = ['врачебная тайна']
available_variants = ['что такое врачебная тайна','защита врачебной тайны',
                      'контроль деятельности по защите врачебной тайны','назад']
available_variants_safety = ['субъекты, отвечающие за защиту врачебной тайны','действия субъектов по защите врачебной тайны',
                              'документы, регулирующие действия по защите вт','назад']
available_variants_control = ['росздравнадзор','роструд','роскомнадзор','фсб','роспотребнадзор','фстэк','назад']
available_documents = ['ст. 13 фз № 323 «об основах охраны здоровья граждан в рф»','ст. 10 фз № 152 «о персональных данных»','фз «об информации, информационных технологиях и о защите информации» от 02.07.2021 № 149-фз',
                       'постановление правительства рф «о федеральном государственном надзоре в сфере обращения лекарственных средств» от 29.06.2021 № 1049',
                       'постановление правительства рф «об утверждении перечня мер, направленных на обеспечение выполнения обязанностей, предусмотренных фз о персональных данных» от 21.03.2012 № 211',
                       'постановление правительства рф «об утверждении положения об особенностях обработки персональных данных, осуществляемой без использования средств автоматизации» от 15.09.2008 № 687',
                       'приказ фстэк россии «об утверждении состава и содержания организационных и технических мер по обеспечению безопасности персональных данных при их обработке в испдн»  от 18 февраля 2013 г. № 21',
                       'постановление правительства рф «об утверждении требований к защите персональных данных при их обработке в испдн» от 01.11.2012 № 1119',
                       'федеральный закон  «о государственном контроле(надзоре) и муниципальном контроле в рф» от 06.12.2021 № 248-фз', 'назад']
                                                                  
class Medical_security(StatesGroup):
    waiting_for_choosing_1 = State()
    waiting_for_choosing_2 = State()
    waiting_for_choosing_3 = State()
    waiting_for_choosing_4 = State()
    waiting_for_choosing_5 = State()

@dp.message_handler(commands="start")
async def start_choosing (message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for category in available_categories:
        keyboard.add(category)
    await message.answer('О какой тайне вы бы хотели узнать?', reply_markup=keyboard)
    await Medical_security.waiting_for_choosing_1.set()

@dp.message_handler(state=Medical_security.waiting_for_choosing_1)
async def category_1_choosed (message: types.Message):
    if message.text.lower() == '/start':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for category in available_categories:
            keyboard.add(category)
        await message.answer('О какой тайне вы бы хотели узнать?', reply_markup=keyboard)
        await Medical_security.waiting_for_choosing_1.set()
    if message.text.lower() not in available_categories:
        await message.answer("Пожалуйста, выберете тайну с помощью клавиатуры")
        return
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for variant in available_variants:
        keyboard.add(variant)
    await message.answer('Что бы вы хотели узнать о данной тайне?', reply_markup=keyboard)
    await Medical_security.waiting_for_choosing_2.set()

@dp.message_handler(state=Medical_security.waiting_for_choosing_2)
async def category_2_choosed (message: types.Message):
    if message.text.lower() == '/start':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for category in available_categories:
            keyboard.add(category)
        await message.answer('О какой тайне вы бы хотели узнать?', reply_markup=keyboard)
        await Medical_security.waiting_for_choosing_1.set()
    if message.text.lower() not in available_variants:
        await message.answer("Пожалуйста, выберете категорию с помощью клавиатуры")
        return
    if message.text.lower()=='назад':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for category in available_categories:
            keyboard.add(category)
        await message.answer('О какой тайне вы бы хотели узнать?', reply_markup=keyboard)
        await Medical_security.waiting_for_choosing_1.set()
    if message.text.lower()=='что такое врачебная тайна':
        await message.answer(ans2)
        await message.answer(hlink('статья 13ФЗ №323 «Соблюдение врачебной тайны»', link2))
    if message.text.lower()=='защита врачебной тайны':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for variant_safety in available_variants_safety:
            keyboard.add(variant_safety)
        await message.answer('Выберете дальнейшую категорию', reply_markup=keyboard)
        await Medical_security.waiting_for_choosing_3.set()
    if message.text.lower() == 'контроль деятельности по защите врачебной тайны':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for variant_control in available_variants_control:
            keyboard.add(variant_control)
        await message.answer('Выберите орган, действия которого по контролю деятельности субъектов защищающих ВТ и документы, регулирующие данные действия,будут показаны', reply_markup=keyboard)
        await Medical_security.waiting_for_choosing_4.set()

@dp.message_handler(state=Medical_security.waiting_for_choosing_3)
async def category_3_choosed (message: types.Message):
    if message.text.lower() == '/start':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for category in available_categories:
            keyboard.add(category)
        await message.answer('О какой тайне вы бы хотели узнать?', reply_markup=keyboard)
        await Medical_security.waiting_for_choosing_1.set()
    if message.text.lower() not in available_variants_safety:
        await message.answer("Пожалуйста, выберете категорию с помощью клавиатуры")
        return
    if message.text.lower()=='субъекты, отвечающие за защиту врачебной тайны':
        await message.answer(ans3_1)
    if message.text.lower()=='документы, регулирующие действия по защите вт':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for variant_document in available_documents:
            keyboard.add(variant_document)
        await message.answer('Выберете интересующий вас документ',reply_markup=keyboard)
        await Medical_security.waiting_for_choosing_5.set()
    if message.text.lower()=='действия субъектов по защите врачебной тайны':
        await message.answer(ans5)
    if message.text.lower()=='назад':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for variant in available_variants:
            keyboard.add(variant)
        await message.answer('Что бы вы хотели узнать о данной тайне?', reply_markup=keyboard)
        await Medical_security.waiting_for_choosing_2.set()

@dp.message_handler(state=Medical_security.waiting_for_choosing_4)
async def category_4_choosed (message: types.Message):
    if message.text.lower() == '/start':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for category in available_categories:
            keyboard.add(category)
        await message.answer('О какой тайне вы бы хотели узнать?', reply_markup=keyboard)
        await Medical_security.waiting_for_choosing_1.set()
    if message.text.lower() not in available_variants_control:
        await message.answer("Пожалуйста, выберете категорию с помощью клавиатуры")
        return
    if message.text.lower()=='росздравнадзор':
        await message.answer(ans4_1)
        await message.answer(hlink('Федеральный закон «Об основах охраны здоровья граждан в Российской Федерации»', link4_1))
    if message.text.lower()=='роструд':
        await message.answer(ans4_2)
        await message.answer(hlink('Постановление Правительства РФ от 30.06.2004 N 324 (ред. от 15.12.2021) «Об утверждении Положения о Федеральной службе по труду и занятости»', link4_2))
    if message.text.lower()=='фстэк':
        await message.answer(ans4_3)
        await message.answer(hlink('Приказ ФСТЭК России от 11 февраля 2013 г. № 17', link4_3_1))
        await message.answer(hlink('Приказ ФСТЭК России от 25 декабря 2017 г. № 239', link4_3_2))
    if message.text.lower()=='роспотребнадзор':
        await message.answer(ans4_4)
        await message.answer(hlink('Постановление Правительства РФ  30 июня 2004 г. N 322 «О федеральной службе по надзору в сфере защиты прав потребителей и благополучия человека»', link4_4))
    if message.text.lower()=='роскомнадзор':
        await message.answer(ans4_5)
        await message.answer(hlink('Федеральный закон от 27.07.2006 N 152-ФЗ (ред. от 02.07.2021) «О персональных данных«', link4_5_1))
        await message.answer(hlink('Постановление Правительства РФ от 01.11.2012 N 1119 «Об утверждении требований к защите персональных данных при их обработке в информационных системах персональных данных»', link4_5_2))
    if message.text.lower()=='фсб':
        await message.answer(ans4_6)
        await message.answer(hlink('Федеральный закон от 21.11.2011 N 323-ФЗ (ред. от 13.07.2022) «Об основах охраны здоровья граждан в Российской Федерации»', link4_6))
    if message.text.lower()=='назад':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for variant in available_variants:
            keyboard.add(variant)
        await message.answer('Что бы вы хотели узнать о данной тайне?', reply_markup=keyboard)
        await Medical_security.waiting_for_choosing_2.set()

@dp.message_handler(state=Medical_security.waiting_for_choosing_5)
async def category_5_choosed (message: types.Message):
    if message.text.lower() == '/start':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for category in available_categories:
            keyboard.add(category)
        await message.answer('О какой тайне вы бы хотели узнать?', reply_markup=keyboard)
        await Medical_security.waiting_for_choosing_1.set()
    if message.text.lower() not in available_documents:
        await message.answer("Пожалуйста выберете категорию с помощью клавиатуры")
        return
    if message.text.lower() == 'ст. 13 фз № 323 «об основах охраны здоровья граждан в рф»':
        await message.answer(ans3_3_1)
        await message.answer(hlink('ст. 13 фз № 323 «об основах охраны здоровья граждан в рф»',link4_1))
    if message.text.lower() == 'ст. 10 фз № 152 «о персональных данных»':
        await message.answer(ans3_3_2)
        await message.answer(hlink('ст. 10 фз № 152 «о персональных данных»',link3_3_2))
    if message.text.lower() == 'фз «об информации, информационных технологиях и о защите информации» от 02.07.2021 № 149-фз':
        await message.answer(ans3_3_3)
        await message.answer(hlink('фз «об информации, информационных технологиях и о защите информации» от 02.07.2021 № 149-фз',link3_3_3))
    if message.text.lower() == 'постановление правительства рф «о федеральном государственном надзоре в сфере обращения лекарственных средств» от 29.06.2021 № 1049':
        await message.answer(ans3_3_4)
        await message.answer(hlink('постановление правительства рф «о федеральном государственном надзоре в сфере обращения лекарственных средств» от 29.06.2021 № 1049',link3_3_4))
    if message.text.lower() == 'постановление правительства рф «об утверждении перечня мер, направленных на обеспечение выполнения обязанностей, предусмотренных фз о персональных данных» от 21.03.2012 № 211':
        await message.answer(ans3_3_5)
        await message.answer(hlink('постановление правительства рф «об утверждении перечня мер, направленных на обеспечение выполнения обязанностей, '
                                   'предусмотренных фз о персональных данных» от 21.03.2012 № 211',link3_3_5))
    if message.text.lower() == 'постановление правительства рф «об утверждении положения об особенностях обработки персональных данных, осуществляемой без использования средств автоматизации» от 15.09.2008 № 687':
        await message.answer(ans3_3_6)
        await message.answer(hlink('постановление правительства рф «об утверждении положения об особенностях обработки персональных данных, осуществляемой '
                                   'без использования средств автоматизации» от 15.09.2008 № 687',link3_3_6))
    if message.text.lower() == 'приказ фстэк россии «об утверждении состава и содержания организационных и технических мер по обеспечению безопасности персональных данных при их обработке в испдн»  от 18 февраля 2013 г. № 21':
        await message.answer(ans3_3_7)
        await message.answer(hlink('приказ фстэк россии «об утверждении состава и содержания организационных и технических мер по обеспечению безопасности '
                                   'персональных данных при их обработке в испдн»  от 18 февраля 2013 г. № 21',link3_3_7))
    if message.text.lower() == 'постановление правительства рф «об утверждении требований к защите персональных данных при их обработке в испдн» от 01.11.2012 № 1119':
        await message.answer(ans3_3_8)
        await message.answer(hlink('постановление правительства рф «об утверждении требований к защите персональных данных'
                                   'при их обработке в испдн» от 01.11.2012 № 1119',link3_3_8))
    if message.text.lower() == 'федеральный закон  «о государственном контроле(надзоре) и муниципальном контроле в рф» от 06.12.2021 № 248-фз':
        await message.answer(ans3_3_9)
        await message.answer(hlink('федеральный закон  «о государственном контроле(надзоре) и муниципальном контроле в рф» от 06.12.2021 № 248-фз',link3_3_9))
    if message.text.lower()=='назад':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for variant in available_variants_safety:
            keyboard.add(variant)
        await message.answer('Что бы вы хотели узнать о данной тайне?', reply_markup=keyboard)
        await Medical_security.waiting_for_choosing_3.set()
def main():
    executor.start_polling(dp)

if __name__ == "__main__":
    main()
