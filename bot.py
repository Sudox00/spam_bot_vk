import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from time import sleep
from random import randint
try:
	z = open('token.txt')
except:	
	my_file = open("token.txt", "w")
	my_file.close()
	z = open('token.txt')
	
if z.read() == "":
	access_token = input("Введите ваш access_token: ")
	f = open('token.txt', 'w')
	f.write(str(access_token))
	
else:
	f = open('token.txt')
	access_token=str(f.read())
	

f = open('token.txt')	
session = vk_api.VkApi(token=str(access_token))
vk=session.get_api()
longpoll = VkLongPoll(session)



inp = input("Введите id чатов или бесед через запятую: ")
cc = inp.replace(' ', '')
ids = cc.split(",")

msg = input("Введтие сообщение: ")

timeout = input("Задержка(в сек.): ")

while True:
	for x in ids:
		try:
				
			if int(len(str(x))) <= 3:
				vk.messages.send(chat_id=x,random_id=randint(1,999999999),message=str(msg))
				print("отправленно в беседу!")
			else:
				vk.messages.send(user_id=x,random_id=randint(1,999999999),message=str(msg))
				print("отправленно в чат!")
		except Exception as e:			
			print("Ошибка: " + str(e))

	sleep(int(timeout))
