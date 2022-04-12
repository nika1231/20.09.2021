import sqlite3
db = sqlite3.connect('test.db')
db.execute("""CREATE TABLE IF NOT EXISTS edienkarte
    (id INT PRIMARY KEY NOT NULL,
    nosaukums TEXT NOT NULL,
    cena REAL NOT NULL,
   alergeni CHAR(50)
   )""")
db.execute("""INSERT INTO edienkarte
          (id,nosaukums,cena,alergeni)
          VALUES (2,'Pīrāgs',1.5,'glutēns')
          """)
db.commit()
dati = db.execute("SELECT * FROM edienkarte WHERE cena > 0.5")
print(dati)

rezultats = dati.fetchall()
print(rezultats)