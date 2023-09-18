from token_1 import TOKEN_VK
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import time

# Создаем базу данных для хранения идентификаторов пользователей
new_users = set()

vk_session = vk_api.VkApi(token=TOKEN_VK)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def send_some_msg(id, text, keyboard=None):
    message = {
        'user_id': id,
        'message': text,
        'random_id': 0
    }
    if keyboard:
        message['keyboard'] = keyboard.get_keyboard()
    vk_session.method('messages.send', message)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg = event.text.lower()
            id = event.user_id
            if id not in new_users:
                new_users.add(id)
                # Создаем клавиатуру с кнопками
                keyboard = VkKeyboard(inline=True)
                keyboard.add_button("Онлайн калькулятор", color=VkKeyboardColor.PRIMARY)
                keyboard.add_button("Записаться на замер", color=VkKeyboardColor.PRIMARY)
                keyboard.add_line()  # Добавляем новую строку для третьей кнопки
                keyboard.add_button("Адрес и контакты", color=VkKeyboardColor.POSITIVE)

                # Отправляем приветственное сообщение с кнопками
                send_some_msg(id, 'Добро пожаловать, новый пользователь!', keyboard)
                time.sleep(1)
            if msg == 'поздоровайся':
                send_some_msg(id, '!!!!!!!!!)))')
                time.sleep(1)
                send_some_msg(id, 'https://kartinkof.club/uploads/posts/2022-06/1655913915_3-kartinkof-club-p-kartinki-s-nadpisyu-ya-rodilsya-luntik-3')

