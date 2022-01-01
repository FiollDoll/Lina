import sqlite3
conn = sqlite3.connect('Lina.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS names(
   name TEXT,
   age TEXT,
   gender TEXT);
""")
conn.commit() #Сохранение в БД

def Go():
    print("Принято")

def regist():
    name = input("Ваше имя: ")
    age = int(input("Ваш возраст: "))
    gender = input("Ваш пол: ")
    #Можно таким способом, чтобы всё было в одной переменной.
    #info = (name, age, gender)
    #cur.execute("INSERT INTO names VALUES(?, ?, ?);", info) # 1 - аргумент
    cur.execute("INSERT INTO names VALUES(?, ?, ?);", (name, age, gender)) # 3 - аргумента
    conn.commit()


print("Привет! Меня зовут Лина. Я - тестовый ИИ с базой данных. Желаете начать?")
start = input("Д/Н ")
if start == "Д":
    regist()


