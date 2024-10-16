import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
    )
''')

# Удалял ранее внесенные записи, чтобы не загромождать БД при экспериментах
# cursor.execute("DELETE FROM Users")

for count in range(1, 11):
    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f'User{count}', f'example{count}@gmail.com', f'{10 * count}', 1000))
for count in range(1, 11, 2):
    cursor.execute('UPDATE Users SET balance = ? WHERE username = ?', (500, f'User{count}'))

for count in range(1, 11, 3):
    cursor.execute('DELETE FROM Users WHERE Username = ?', (f'User{count}',))

cursor.execute('SELECT Username, email, age, balance FROM Users WHERE age != ?', (60,))

user_list = cursor.fetchall()
for user in user_list:
    print(user)

connection.commit()
connection.close()
