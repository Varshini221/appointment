import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS services (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(30) UNIQUE NOT NULL,
    category VARCHAR(20) NOT NULL,
    frequency INT NOT NULL DEFAULT '1'
);
""")

conn.commit()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_id INT NOT NULL,
    cost DECIMAL(3, 2) DEFAULT '0',
    date DATE NOT NULL,
    notes VARCHAR(30),
    FOREIGN KEY (service_id) REFERENCES services(id)
);
""")

conn.commit()


# cursor.execute("""
# UPDATE services 
# SET category = 'Hair Stuff' 
# WHERE category = 'Haircare';
# """)

# cursor.execute("""
# DELETE FROM services
# WHERE category = 'Hair Stuff';
# """)

# conn.commit()



flag = True
while flag:
    choice = int(input("1: add a new service, 2: delete a serivce, 3: add an appointment, update an appointment   choose a number: "))

    if choice == 1:
        service_name = input("Add a service name: ")
        service_cat = input("Add the service category: ")
        service_freq = int(input("How many times a month do you do this: "))

        cursor.execute("""
            INSERT INTO services(name, category, frequency) VALUES(?, ?, ?);
        """, (service_name, service_cat, service_freq))
        conn.commit()

    elif choice == 2:
        cursor.execute("SELECT * FROM services")
        print(cursor.fetchall())
        cat = int(input("which service do you want to delete tell me the id: "))

        cursor.execute("""
        DELETE FROM services
        WHERE id = ?
        """, (cat,))
        conn.commit()
        cursor.execute("SELECT * FROM services")
        print(cursor.fetchall())

    elif choice == 3:
        cursor.execute("SELECT * FROM services")
        print(cursor.fetchall())
        service = int(input("What service is it: "))
        cost = float(input("how much did it cost: $"))
        date = input("put the date in format yyyy-mm-dd: ")
        notes = input("do you have any notes about the app: ")
        cursor.execute("""
            INSERT INTO appointments(service_id, cost, date, notes) VALUES(?,  ?, ?, ?);

        """, (service, cost, date, notes))
        conn.commit()
        cursor.execute("SELECT * FROM appointments")
        print(cursor.fetchall())

    elif choice == 4:
        cursor.execute("SELECT * FROM appointments")
        print(cursor.fetchall())
        app = int(input("which appointment do you wanna update give me the id: "))
        up = int(input("1: cost, 2: date, 3: notes what do you wanna update: "))
        if up == 1:
            cost = float(input("whats the new cost: "))
            cursor.execute("""
                UPDATE appointments
                SET cost = ?
                WHERE id = ?
""", (cost, app))
            
        elif up == 2:
            date = input("tell me the new date: ")
            cursor.execute("""
                UPDATE appointments
                SET date = ?
                WHERE id = ?
""", (date, app))
        elif up == 3:
            notes = input("whast the new notes: ")
            cursor.execute("""
                UPDATE appointments
                SET notes = ?
                WHERE id = ?
        """, (notes, app))
        conn.commit()
    else:
        flag = False

cursor.execute("SELECT * FROM services")
print(cursor.fetchall())
