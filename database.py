import sqlite3
import random

def create_name(dlzka: int) -> str:
    samo = "aeiouy"
    spolu = "bcdfghjklmnpqrstvwxz"
    temp = ""
    for i in range(dlzka):
        if i % 2 == 0:
            temp += random.choice(spolu)
        else:
            temp += random.choice(samo)
    return temp.capitalize()

oci = ["hnede", "modre", "zelene", "sive"]

connection = sqlite3.connect("C:/Users/lomni/pokusna.db")
cursor = connection.cursor()

for i in range(10):
    cursor.execute(
        "INSERT INTO studenti (meno, priezvisko, vek, oci, velkost_nohy) "
        "VALUES (?, ?, ?, ?, ?)",
        (
            create_name(8),
            create_name(10),
            random.randint(12, 22),
            random.choice(oci),
            random.randint(34, 48),
        ),
    )

connection.commit()

cursor.execute("SELECT * FROM studenti")
for riadok in cursor.fetchall():
    print(riadok)

connection.close()
