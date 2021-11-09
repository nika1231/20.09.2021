#uzdevumā nepieciešams definēt divus for ciklus, izmantot if apgalvojumu, lietotāja ievadi un izvadi.

saraksts = sk

saraksts = [int(sk) for sk in input('Ievadi skaitļus, atdalot tos ar atstarpi:')]

saraksts = [int(sk) for sk in input('Ievadi skaitļus, atdalot tos ar atstarpi:').split()]

for i in range(len(saraksts)):
  print(i)
  
if saraksts[i] == saraksts[i+1]
  print(saraksts[i],saraksts[i+1])