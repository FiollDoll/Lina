import sqlite3
import random
conn = sqlite3.connect('Lina.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS names(
   name TEXT,
   userID INT,
   age TEXT,
   gender TEXT);
""")
conn.commit() #Сохранение в БД
cur.execute("""CREATE TABLE IF NOT EXISTS info(
   userID INT,
   location TEXT,
   money TEXT);
""")
conn.commit()

userId = random.randint(1, 100)
def Go():
    print("Принято. Теперь пара вопросов:")
    location = input("Где вы живёте:")
    money = input("Сколько у вас денег:")
    cur.execute("INSERT INTO info VALUES(?, ?, ?);", ( userId, location, money)) # 3 - аргумента
    conn.commit()
    print("Спасибо! Наши специалисты уже выезжают :)")
    input("Нажмите ENTER")

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


