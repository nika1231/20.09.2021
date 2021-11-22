class Rekins:

   def __init__(self,klients,veltijums,izmers,materials):
   
      self.klients = klients
      self.veltijums = veltijums
      self.izmers = izmers
      self.materials = materials
  

      self.teksta_gar = len(self.veltijums)
      self.ladites_izm = self.izmeri.split(',')
      self.garums = self.ladites_izm[0]
      self.platums = self.ladites_izm[1]
      self.augstums = self.ladites_izm[2]


   def izdrukat(self):
    print(f'Klienta vārds {self.klients}')
    print(f'veltjuma teksts{self.veltijums}')
    print(f'izmērs{self.izmers}')
    print(f'lodītes materials{self.materials}')

   def aprekins(self):
     darba_samaksa = 15
     PVN = 21
       produkta_cena = (self.teksta_gar)* 1.2 + (self.platums/100 * self.garums/100 * self.augstums/100)/ 3 * self.materialas
       PVN_summa = (produkta_cena + darba_samaksa)*PVN/100
       rekina_summa = (produkta_cena + darba_samaksa) + PVN_summa
     pass
klients = input('Uzraksti savu vārdu un uzvārdu')
veltijums = input('Uzraksti veltījumu:')
izmeri = input('Ievadi lādītes izmēru\n Garums, platums,augstums(raksti veselus skaitļus, atdalot tos ar komatiem\n')
materials = input('materiala cena EUR/m2:')

rekins = Rekins(klients,veltijums,izmeri, materials)
print(rekins.klients)
print(rekins.veltijums)
print(rekins.izmeri)
print(rekins.ladites_izm)

print(rekins.aprekins())
# print(izmeri)
# print(type(izmeri))  
# print(izmeri.split(','))  
# sadal = izmeri.split(',')
# print(sadal[0])
# print (sadal[1])
# print(sadal[2])

