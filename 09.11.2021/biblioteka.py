#klases nosaukums

class Robots:
  """Klase reprezentā robotu ar specifisko vārdu"""

  #klases konstruktoru. inicializēšana
  def __init__(self, vards):
    """Datu inicializācija"""

    #īpašību definēšana
    self.vards = vards

    print(f'Inicializējam {self.vards}')
  
  def sasveicinaties(self):
    print(f'Sveiks! Mani sauc {self.vards}')


#klases pārbaudīšanās

#1. robota izveide
rob1 = Robots('R1')

#1.robota metodes pārbaude
rob1.sasveicinaties()

#2.robota izveide

rob2 = Robots('R2')

rob2.sasveicinaties()
