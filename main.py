import sqlite3
import random
import time
conn = sqlite3.connect('Lina.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS names(
   name TEXT,
   userID INT,
   age TEXT,
   gender TEXT);
""")
conn.commit() #Сохранение в БД
cur.execute("""CREATE TABLE IF NOT EXISTS answer(
   userID INT,
   health INT,
   friend INT,
   work INT);
""")
conn.commit()

userId = random.randint(1, 100)
def Go():
    health = 0
    friend = 0
    work = 0
    print("Принято. Теперь пара вопросов:")
    time.sleep(1)
    print("Вы хорошо себя чувствуете?")
    print("Да(0), Нет(1), Не могу ответить(2)")
    answer = input(" ")
    if answer == "0":
        health = 0
    elif answer == "1":
        health = 1
    else:
        health = 2

    time.sleep(1)
    print("Вы имеете много друзей?")
    print("Да(0), Нет(1), Не могу ответить(2)")
    answer1 = input(" ")
    if answer1 == "0":
        friend = 0
    elif answer1 == "1":
        friend = 1
    else:
        friend = 2
    time.sleep(1)

    print("Вы хорошо учитесь/работаете?")
    print("Да(0), Нет(1), Не могу ответить(2)")
    answer2 = input(" ")
    if answer2 == "0":
        work = 0
    elif answer2 == "1":
        work = 1
    else:
        work = 2
    print("Делаю результат")
    cur.execute("INSERT INTO answer VALUES(?, ?, ?, ?);", (userId, health, friend, work)) # 3 - аргумента
    conn.commit()
    if health == 0 and friend == 0 and work == 0:
        print("У вас всё хорошо")
    elif health == 1 and friend == 0 and work == 0:
        print("У вас всё хорошо, кроме здоровья")
    elif health == 0 and friend == 1 and work == 0:
        print("У вас всё хорошо, кроме количества друзей")
    elif health == 0 and friend == 0 and work == 1:
        print("У вас всё хорошо, кроме учёбы")
    elif health == 1 and friend == 1 and work == 1:
        print("У вас всё плохо")
    else:
        print("Всё плохо")
def regist():
    global userId
    name = input("Ваше имя: ")
    age = int(input("Ваш возраст: "))
    gender = input("Ваш пол: ")
    #Можно таким способом, чтобы всё было в одной переменной.
    #info = (name, age, gender)
    #cur.execute("INSERT INTO names VALUES(?, ?, ?);", info) # 1 - аргумент
    cur.execute("INSERT INTO names VALUES(?, ?, ?, ?);", (name, userId, age, gender)) # 3 - аргумента
    conn.commit()
    Go()


print("Привет! Меня зовут Лина. Я - тестовый ИИ с базой данных. Желаете начать?")
start = input("Д/Н ")
if start == "Д":
    regist()


