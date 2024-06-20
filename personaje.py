import math
class Personaje:
  id_inicial = 1
  def __init__(self, nombre, genero, ataque, defensa, vida, suerte, tipo, arma, pociones) -> None:
    self.id = Personaje.id_inicial
    Personaje.id_inicial += 1
    self.nombre = nombre
    self.genero = genero
    self.ataque = ataque
    self.defensa = defensa
    self.vida = vida
    self.suerte = suerte
    self.tipo = tipo
    self.arma = arma
    self.pociones = pociones

  def aplicar_bonificaciones(self):
    self.ataque = math.ceil(self.ataque * self.tipo.bonif_ataque)
    self.defensa = math.ceil(self.defensa * self.tipo.bonif_defensa)
    self.vida = math.ceil(self.vida * self.tipo.bonif_vida)
    self.suerte = math.ceil(self.suerte * self.tipo.bonif_suerte)

  # getters de tipo, arma y pociones.

  def __str__(self) -> str:
    return f"ID: {self.id}, Nombre: {self.nombre}, Género: {self.genero}, Tipo: {self.tipo.nombre}"