import telebot
import json
import requests

API_Token = '6453065800:AAE8ao9Vtr8KEQaOpyq0M4TaqQZ0yrndsVg'

#bot = telebot.Telebot(API_Token)
bot = telebot.TeleBot(API_Token)

 
sp = {'дядя коля': {'номер телефона': ['8-800-555-35-35', '8-900-536-35-35'], 'город': 'Сыктыфкар', 'Статус': 'дядя'}, 'нюрка': {'номер телефона': ['8-555-549-34-35'], 'город': 'Сыктыфкар', 'Статус': 'тетя'}}

while True:
    command = input('Введите команду: ')
    if command == '/all':
        print('Вот текущий список номеров') 
        for k, v in sp.items():
            print(k, v)


    elif command == '/add.contact':
        name = input('Введите имя нового контакта: ')
        if name in sp:
            print('Контакт существует!')
        else:
            coll = int(input('Сколько номеров вы хотите ввести: '))
            numbers = []
            for i in range(coll):
                number = input(f'Введите {i+1} номер: ')
                numbers.append(number)
            city = input('Введите название города: ')
            status = input('Введите статус: ')
            sp[name] = {'номер телефона': numbers, 'город': city, 'Статус': status}
    if command == '/add.number':  
        name = input('Введите имя контакта: ')
        if name not in sp:
            print('Контакта не существует!')
        else: 
            phone = input('Введите номер: ')
            if phone in sp[name]['номер телефона']:
                print('Номер существует')
            else:
                sp[name]['номер телефона'].append(phone)



bot.polling(non_stop = True)
