import math
import random
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

  def mostrar_atributos(self):
    return f"Ataque: {self.ataque}, Defensa: {self.defensa}, Vida: {self.vida}, Suerte: {self.suerte}"
  
  # Ver de hacer setter de vida
  def recibir_ataque(self, cantidad):
    self.vida -= cantidad - self.defensa  # El daño recibido se reduce por la defensa
    if self.vida < 0:
      self.vida = 0
  
  def combate(self, defensor):
    daño = self.ataque + self.arma.daño

    if (random.random() < self.arma.probabilidad_critico + self.suerte):
      daño *= 2
      print(f"\n{self.nombre} realizó un golpe crítico a {defensor.nombre} con {self.arma.nombre} causando {daño} puntos de daño.")
    else:
      print(f"\n{self.nombre} atacó a {defensor.nombre} con {self.arma.nombre} causando {daño} de daño.")
    
    defensor.recibir_ataque(daño)
    print(f"{defensor.nombre} tiene {defensor.vida} de vida restante.")

    if defensor.vida <= 0:
      print(f"{defensor.nombre} ha sido derrotado.")

  def beber_pocion(self, pocion):
    if random.random() > 0.20 - self.suerte:
      self.vida += self.pociones[pocion - 1].curacion
      if self.vida > 100:
        self.vida = 100
    del self.pociones[pocion - 1]

  # getters de tipo, arma y pociones.

  def __str__(self) -> str:
    return f"ID: {self.id}, Nombre: {self.nombre}, Género: {self.genero}, Tipo: {self.tipo.nombre}"