import sqlite3

# اتصال به پایگاه داده
connection = sqlite3.connect('train_ticket.db')
cursor = connection.cursor()

# ایجاد جدول trains
cursor.execute('''
CREATE TABLE IF NOT EXISTS trains (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    train_number TEXT NOT NULL,
    destination TEXT NOT NULL,
    departure_time TEXT NOT NULL,
    available_seats INTEGER NOT NULL
);
''')

# ایجاد جدول passengers
cursor.execute('''
CREATE TABLE IF NOT EXISTS passengers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    contact TEXT NOT NULL
);
''')

# ایجاد جدول reservations
cursor.execute('''
CREATE TABLE IF NOT EXISTS reservations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    train_id INTEGER,
    passenger_id INTEGER,
    seat_number INTEGER,
    booking_date TEXT NOT NULL,
    FOREIGN KEY (train_id) REFERENCES trains(id),
    FOREIGN KEY (passenger_id) REFERENCES passengers(id)
);
''')

# تغییرات را ذخیره کنید و اتصال را ببندید
connection.commit()
connection.close()
