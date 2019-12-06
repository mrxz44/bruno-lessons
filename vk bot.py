
# 0ebcd0735a4f5a2a7577d81f528ca980fa594959ea3633cee5ba13452717af36ca808dab591e6e4a4f47a
import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

bot_mind = float(random.randint(0,10))
print (bot_mind)


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id':random.randint(0, 2048)})

token = "0ebcd0735a4f5a2a7577d81f528ca980fa594959ea3633cee5ba13452717af36ca808dab591e6e4a4f47a"

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

# Основной цикл
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
    
        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:
        
            # Сообщение от пользователя
            request = event.text
            
            # Каменная логика ответа
            if request == "привет":
                write_msg(event.user_id, "Хай")
            elif request == "пока":
                write_msg(event.user_id, "Пока((")
            elif request == "New game":
            	write_msg(event.user_id, 'OK. Lets play')
            	for event in longpoll.listen():
            		if event.type == VkEventType.MESSAGE_NEW:
            			if event.to_me:
            				request = float(event.text)
            				if request > bot_mind:
            					write_msg(event.user_id, 'Too big')

            				if request < bot_mind:
            					write_msg(event.user_id, 'Too small')

            				if request == bot_mind:
            					write_msg(event.user_id, 'Bingo!!!1')
            					break





"""

            				bot_answer = random.choice(l)
            				write_msg(event.user_id, bot_answer)
            				if request == bot_answer:
            					write_msg(event.user_id, 'Draw')

            				elif request == 'stone':
            					if bot_answer == 'paper':
            						write_msg(event.user_id, 'Loose')
            					else:
            						write_msg(event.user_id, 'Win')

            				elif request == 'paper':
            					if bot_answer == 'scissors':
            						write_msg(event.user_id, 'Loose')
            					else:
            						write_msg(event.user_id, 'Win')

            				break




            else:
                write_msg(event.user_id, "Не поняла вашего ответа...")
                """






"""
V:\PY246-1784\Михаил\temp.py
"""
