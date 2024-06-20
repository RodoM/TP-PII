from tipo import Tipo
from arma import Arma
from pocion import Pocion
from personaje import Personaje

# Tipos
tipo1 = Tipo(nombre="Guerrero", bonif_ataque=1.2, bonif_defensa=1.1, bonif_vida=0.9, bonif_suerte=1.0)
tipo2 = Tipo(nombre="Arquero", bonif_ataque=1.3, bonif_defensa=0.8, bonif_vida=0.9, bonif_suerte=1.1)
tipo3 = Tipo(nombre="Mago", bonif_ataque=1.0, bonif_defensa=0.9, bonif_vida=1.0, bonif_suerte=1.2)
tipo4 = Tipo(nombre="Tanque", bonif_ataque=0.8, bonif_defensa=1.4, bonif_vida=1.2, bonif_suerte=0.9)
tipo5 = Tipo(nombre="Asesino", bonif_ataque=1.5, bonif_defensa=0.7, bonif_vida=0.8, bonif_suerte=1.0)

tipos = [tipo1, tipo2, tipo3, tipo4, tipo5]

# Armas
arma1 = Arma(nombre="Espada Larga", daño=15, probabilidad_critico=0.2)
arma2 = Arma(nombre="Arco Compuesto", daño=12, probabilidad_critico=0.25)
arma3 = Arma(nombre="Báculo Mágico", daño=14, probabilidad_critico=0.3)
arma4 = Arma(nombre="Hacha de Batalla", daño=18, probabilidad_critico=0.15)
arma5 = Arma(nombre="Daga Envenenada", daño=10, probabilidad_critico=0.35)

armas = [arma1, arma2, arma3, arma4, arma5]

# Pociones
pocion1 = Pocion("Poción de Curación Menor", 20)
pocion2 = Pocion("Poción de Curación Mayor", 50)
pocion3 = Pocion("Poción de Maná", 30)
pocion4 = Pocion("Poción de Resistencia", 15)
pocion5 = Pocion("Poción de Vitalidad", 40)

pociones = [pocion1, pocion2, pocion3, pocion4, pocion5]

# Personajes
personaje1 = Personaje(nombre="Aragorn", genero="Masculino", ataque=3, defensa=2, vida=3, suerte=2, tipo=tipo1, arma=arma1, pociones=[pocion1])
personaje2 = Personaje(nombre="Legolas", genero="Masculino", ataque=4, defensa=2, vida=3, suerte=1, tipo=tipo2, arma=arma2, pociones=[pocion1, pocion3])
personaje3 = Personaje(nombre="Gimli", genero="Masculino", ataque=3, defensa=3, vida=2, suerte=2, tipo=tipo3, arma=arma3, pociones=[])
personaje4 = Personaje(nombre="Eowyn", genero="Femenino", ataque=2, defensa=2, vida=3, suerte=3, tipo=tipo4, arma=arma4, pociones=[pocion3, pocion5])
personaje5 = Personaje(nombre="Gandalf", genero="Masculino", ataque=1, defensa=3, vida=4, suerte=2, tipo=tipo5, arma=arma5, pociones=[pocion2, pocion4, pocion5])

personajes = [personaje1, personaje2, personaje3, personaje4, personaje5]

for personaje in personajes:
  personaje.aplicar_bonificaciones()