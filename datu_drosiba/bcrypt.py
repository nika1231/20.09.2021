#datu šifrēšana

import bcrypt

parole = b'abols'

salt = bcrypt.gensalt() #generējam salt

savienots = bcrypt.hashpw(parole,salt)

print(parole)
print(salt)
print(savienots)