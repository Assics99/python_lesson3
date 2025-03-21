import os
from dotenv import load_dotenv
load_dotenv()
import smtplib

f = """Ass1cs88@yandex.ru"""
t = """Ass1cs88@yandex.ru"""
sub = """Приглашение!"""
сontect_type = """text/plain; charset="UTF-8"; """

send_to = 'Ass1cs88@yandex.ru'
send_from = 'Ass1cs88@yandex.ru'

letter = """From: {f}
To: {t}
Subject: {sub}
сontect_type: {сontect_type}

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""".format(f=f, t=t, sub=sub, сontect_type=сontect_type)

letter = letter.replace("%website%", "https://dvmn.org/profession-ref-program/brat_luki/QfXMV/")
letter = letter.replace("%friend_name%", "Кирилл")
letter = letter.replace("%my_name%", "Иван")
letter = letter.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(os.environ['LOGIN'], os.environ['PASSWORD'])
server.sendmail(send_to, send_from, letter)
server.quit