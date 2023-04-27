from main import bot, dp

from random import choice
import subprocess
import pyautogui
from aiogram_broadcaster import TextBroadcaster
import time
from PIL import Image, ImageDraw
import sqlite3
from datetime import datetime

from aiogram.types import Message
from config import admin_id, users_id
user_id = users_id[:]
us = set()

async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text="Бот таки работает")

async def notify_admins(dp):
    save('Start bot')
    await TextBroadcaster(users_id, 'Бот таки работает').run()
    for i in users_id:
        await bot.send_photo(i, open('C:\\Users\\Admin\\Desktop\\start.jpg', 'rb'))


async def gg():
    print(1)
    for i in users_id:
        await bot.send_message(i, text="Доброе утро, Славяне")

@dp.message_handler(commands='id')
async def idy(message: Message):
    save('id')
    await message.answer(f'Ваш ID: {message.from_user.id}')
    us.add(message.from_user.id)

@dp.message_handler(commands='allid')
async def allidy(message: Message):
    save('allid')
    await message.answer(f'Все ID: {us}')

@dp.message_handler(commands='start')
async def star(message: Message):
    me = await bot.get_me()
    save('start')
    await message.answer(f'{message.from_user.first_name}, тебе здесь не рады')

@dp.message_handler(commands='maincraft')
async def mainc(message: Message):
    if message.from_user.id == admin_id:
        subprocess.Popen('C:\\Users\\Admin\\AppData\\Roaming\\.minecraft\\TLauncher.exe')
        time.sleep(15)
        pyautogui.moveTo(1080, 830)
        pyautogui.click()
        time.sleep(15)
        pyautogui.screenshot(r"C:\Users\Admin\Desktop\screenshot.png")
        photo = open('C:\\Users\\Admin\\Desktop\\screenshot.png', 'rb')
        save('maincraft')
        await bot.send_photo(chat_id=message.chat.id, photo=photo)
        await bot.send_message(message.from_user.id, text=f'Майн запущен')
    else:
        print('Error')

@dp.message_handler(commands='starcraft')
async def starcraft(message: Message):
    if message.from_user.id == admin_id:
        subprocess.Popen('D:\\Games\\StarCraft II\\StarCraft II.exe')
        time.sleep(15)
        pyautogui.moveTo(360, 900)
        pyautogui.click()
        time.sleep(15)
        pyautogui.screenshot(r'C:\Users\Admin\Desktop\screenshot.png')
        photo = open('C:\\Users\\Admin\\Desktop\\screenshot.png', 'rb')
        save('starcraft')
        await bot.send_photo(chat_id=message.chat.id, photo=photo)
        await bot.send_message(message.from_user.id, text=f'Старкрафт запущен')
    else:
        print('Error')

@dp.message_handler(commands='warthunder')
async def warthunder(message: Message):
    if message.from_user.id == admin_id:
        subprocess.Popen('D:\\games steam\\steamapps\\common\\War Thunder\\launcher.exe')
        time.sleep(30)
        pyautogui.moveTo(1320, 850)
        pyautogui.click()
        time.sleep(30)
        pyautogui.screenshot(r'C:\Users\Admin\Desktop\scrinshot.png')
        photo = open('C:\\Users\\Admin\\Desktop\\scrinshot.png', 'rb')
        save('warthunder')
        await bot.send_photo(chat_id=message.chat.id, photo=photo)
        await bot.send_message(message.from_user.id, text=f'Тундра запущена')
    else:
        print('Error')

@dp.message_handler(commands='closegame')
async def closegame(message: Message):
    if message.from_user.id == admin_id:
        pyautogui.hotkey('alt', 'f4')
        time.sleep(2)
        pyautogui.screenshot(r'C:\Users\Admin\Desktop\screenshot.png')
        photo = open('C:\\Users\\Admin\\Desktop\\screenshot.png', 'rb')
        save('close game')
        await bot.send_photo(chat_id=message.chat.id, photo=photo)
        await bot.send_message(message.from_user.id, text=f'Игра закрыта')

@dp.message_handler(commands='move')
async def movemouse(message: Message):
    if message.from_user.id == admin_id:
        text = message.text[6:]
        text = text.split()
        if int(text[0]) > 1919:
            text[0] = 1919
        if int(text[1]) > 1079:
            text[1] = 1079
        pyautogui.moveTo(int(text[0]), int(text[1]))
        pyautogui.screenshot(r'C:\Users\Admin\Desktop\screenshot.png')
        photo = Image.open('C:\\Users\\Admin\\Desktop\\screenshot.png')
        draw = ImageDraw.Draw(photo)
        if int(text[0]) < 1909 and int(text[1]) < 1069:
            draw.ellipse((int(text[0]) - 5, int(text[1]) - 5, int(text[0]) + 5, int(text[1]) + 5), fill='red', outline=(0, 0, 0))
            photo.save(r'C:\Users\Admin\Desktop\screenshot.png', quality=95)
        photo = open('C:\\Users\\Admin\\Desktop\\screenshot.png', 'rb')
        save('move')
        await bot.send_photo(chat_id=message.chat.id, photo=photo)

@dp.message_handler(commands='click')
async def dclicking(message: Message):
    if message.from_user.id == admin_id:
        pyautogui.click()
        pyautogui.screenshot(r'C:\Users\Admin\Desktop\screenshot.png')
        photo = open('C:\\Users\\Admin\\Desktop\\screenshot.png', 'rb')
        save('click')
        await bot.send_photo(chat_id=message.chat.id, photo=photo)

@dp.message_handler(commands='dclick')
async def clicking(message: Message):
    if message.from_user.id == admin_id:
        pyautogui.doubleClick()
        pyautogui.screenshot(r'C:\Users\Admin\Desktop\screenshot.png')
        photo = open('C:\\Users\\Admin\\Desktop\\screenshot.png', 'rb')
        save('double click')
        await bot.send_photo(chat_id=message.chat.id, photo=photo)

@dp.message_handler(commands='write')
async def keyboard(message: Message):
    if message.from_user.id == admin_id:
        text = message.text[7:]
        pyautogui.write(text, interval=0.25)
        time.sleep(3)
        pyautogui.screenshot(r'C:\Users\Admin\Desktop\screenshot.png')
        photo = open('C:\\Users\\Admin\\Desktop\\screenshot.png', 'rb')
        save('write')
        await bot.send_photo(chat_id=message.chat.id, photo=photo)

@dp.message_handler(commands='enter')
async def keyboarde(message: Message):
    if message.from_user.id == admin_id:
        text = message.text[7:]
        pyautogui.press('Enter')
        time.sleep(3)
        pyautogui.screenshot(r'C:\Users\Admin\Desktop\screenshot.png')
        photo = open('C:\\Users\\Admin\\Desktop\\screenshot.png', 'rb')
        save('enter')
        await bot.send_photo(chat_id=message.chat.id, photo=photo)

@dp.message_handler(commands='screen')
async def screenshot(message: Message):
    if message.from_user.id == admin_id:
        x, y = pyautogui.position()
        pyautogui.screenshot(r'C:\Users\Admin\Desktop\screenshot.png')
        photo = Image.open('C:\\Users\\Admin\\Desktop\\screenshot.png')
        draw = ImageDraw.Draw(photo)
        if int(x) < 1909 and int(y) < 1069:
            draw.ellipse((int(x) - 5, int(y) - 5, int(x) + 5, int(y) + 5), fill='red',
                         outline=(0, 0, 0))
            photo.save(r'C:\Users\Admin\Desktop\screenshot.png', quality=95)
        photo = open('C:\\Users\\Admin\\Desktop\\screenshot.png', 'rb')
        save('screen')
        await bot.send_photo(chat_id=message.chat.id, photo=photo)

def save(command):
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    res = cur.execute("SELECT Command FROM Commands")
    res = res.fetchall()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    cur.execute('''INSERT INTO Commands(Command, Time)
            VALUES (?, ?)''', [command, current_time])
    con.commit()