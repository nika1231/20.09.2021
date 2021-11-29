print('Sveiks/a')
print('šī programma izdrukās vienkāršun rēķinu koka lādītei ar gravējumu\n\n')



class Rekins:


   def __init__(self,klients,veltijums,izmers,materials):
   
      self.klients = klients
      self.veltijums = veltijums
      self.izmers = izmers
      self.materials = materials
  

      self.teksta_gar = len(self.veltijums)
      self.ladites_izm = self.izmers.split(',')
      self.garums = int(self.ladites_izm[0])
      self.platums = int(self.ladites_izm[1])
      self.augstums = int(self.ladites_izm[2])
      self.materials = int(self.materials)


   def izdrukat(self):
    print(f'Klienta vārds {self.klients}')
    print(f'veltījuma teksts{self.veltijums}')
    print(f'izmērs{self.izmers}')
    print(f'lodītes materiāls{self.materials}')
    print("\n\n")
    print('\033[1m'+"Pasūtītāja dati:"+'\033[0m')
    print("-"*50)
    print(f"\x1B[3mPasūtītāja vārds un uzvārds:\x1B[0m \033[1;32m{self.klients}\033[1;0m")
    print(f"\x1B[3mVeltījuma teksts:\x1B[0m\033[1;32m{self.veltijums}\033[1;0m")
    print(f"\x1B[3mLādītes izmēri:\x1B[0m\033[1;32m{self.izmers}\033[1;0m")
    print(f"\x1B[3mPlatums:\x1B[0m\033[1;32m{self.platums}\033[1;0m")
    print(f"\x1B[3mGarums:\x1B[0m\033[1;32m{self.garums}\033[1;0m")
    print(f"\x1B[3mAugstums:\x1B[0m\033[1;32m{self.augstums}\033[1;0m")
    print(f"\x1B[3mMateriāla cena EUR/m2:\x1B[0m\033[1;32m{self.materials}\033[1;0m")
    print(f"\x1B[3mIzmaksas:\x1B[0m\033[1;32m{self.aprekins()}\033[1;0m")

    self.saglabat()
    print(f'klienta dati saglabāti failā{self.klients}.csv')




   def aprekins(self):
     darba_samaksa = 15
     PVN = 21
     produkta_cena = (self.teksta_gar)* 1.2 + (self.platums/100 * self.garums/100 * self.augstums/100)/ 3 * self.materials
     PVN_summa = (produkta_cena + darba_samaksa)*PVN/100
     rekina_summa = (produkta_cena + darba_samaksa) + PVN_summa
     return rekina_summa

   def saglabat(self): 

     import csv 

     with open(f'{self.klients}.csv', 'w', newline ='') as file:
       writer = csv.writer(file)
       writer.writerow = (['Klienta vārds','Veltījums','Izmēri','Materiāla cena'])
 



klients = input('Pasūtītāja vārds,uzvārds:')
print('-'*50)
veltijums = input('Nepieciešamais veltījums:')
print('-'*50)
izmeri = input('Lādītes izmērs - Garums, platums,augstums- milimetros(raksti veselus skaitļus:')
print('-'*50)
materials = input('Kokmateriāla cena EUR/m2:')

rekins = Rekins(klients,veltijums,izmeri, materials)
print(rekins.izdrukat())






# print(rekins.klients)
# print(rekins.veltijums)
# print(rekins.izmers)
# print(rekins.ladites_izm)

# print(rekins.aprekins())
# print(izmeri)
# print(type(izmeri))  
# print(izmeri.split(','))  
# sadal = izmeri.split(',')
# print(sadal[0])
# print (sadal[1])
# print(sadal[2])

