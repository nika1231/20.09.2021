#Divu tabulu savienošana

import sqlite3


db = sqlite3.connect('test.db')



# dati = db.execute("""SELECT * FROM edienkarte
#                   JOIN sastavdalas
#                   ON edienkarte.id = sastavdalas.id
#                  """)

# rezultats = dati.fetchall()

# print(rezultats)
#TITANIKA DATU BĀZE
import datetime

start = datetime.datetime.now()


db = sqlite3.connect('titanic DB.db')

# dati = db.execute("SELECT Name FROM titanic ORDER BY Name")
# dati = db.execute("SELECT PassengerId, Name FROM titanic ORDER BY Name")
# dati = db.execute("SELECT PassengerId, Name FROM titanic  WHERE Survived = 1")
dati = db.execute("SELECT SUM(Survived) FROM titanic  WHERE Survived = 1")
rezultati = dati.fetchall()
end = datetime.datetime.now()

# print(rezultati)

for rinda in rezultati:
  print(rinda)

laiks = end-start
print(laiks)
