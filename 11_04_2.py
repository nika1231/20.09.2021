import sqlite3

db = sqlite3.connect('test.db')

db.execute("""CREATE TABLE IF NOT EXISTS sastavdalas
    (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,pirma 
    CHAR(50) NOT NULL,
    otra CHAR (50),
    tresa CHAR(50)
    )""")
pirma = input("Ievadi pirmo sastāvdaļu:")
print(pirma)
otra = input ("Ievadi otro sastāvdaļu:")
print(otra)
tresa = input("Ievadi trešo sastāvdaļu:")
print(tresa)
db.execute("""INSERT INTO sastavdalas 
            (pirma,otra,tresa)
            VALUES (:pirma,:otra,:tresa)
""",{'pirma':pirma,'otra':otra,'tresa':tresa})

db.commit()

dati = db.execute("SELECT * FROM sastavdalas")


rezultats = dati.fetchall()

for rinda in rezultats:
  print("ID",rinda[0])
  print("1 sastāvdaļa",rinda[1])
  print("2 sastāvdaļa",rinda[2])