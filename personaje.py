import math
import random
from tipo import Tipo
from arma import Arma
from pocion import Pocion
from typing import List
class Personaje:
  id_inicial = 1
  def __init__(self, nombre: str, genero: str, ataque: int, defensa: int, suerte: int, tipo: Tipo, arma: Arma, pociones: List[Pocion]) -> None:
    self.__id = Personaje.id_inicial
    Personaje.id_inicial += 1
    self.__nombre = nombre
    self.__genero = genero
    self.__ataque = ataque
    self.__defensa = defensa
    self.__vida = 100
    self.__suerte = suerte
    self.__tipo = tipo
    self.__arma = arma
    self.__pociones = pociones

  @property
  def id(self) -> int:
    return self.__id

  @property
  def nombre(self) -> str:
    return self.__nombre
  
  @property
  def genero(self) -> str:
    return self.__genero
  
  @property
  def ataque(self) -> int:
    return self.__ataque
  
  @ataque.setter
  def ataque(self, nuevo_ataque: int):
    self.__ataque = nuevo_ataque
  
  @property
  def defensa(self) -> int:
    return self.__defensa
  
  @defensa.setter
  def defensa(self, nueva_def: int):
    self.__def = nueva_def
  
  @property
  def vida(self) -> int:
    return self.__vida
  
  @vida.setter
  def vida(self, nueva_vida: int):
    self.__vida = nueva_vida
  
  @property
  def suerte(self) -> int:
    return self.__suerte
  
  @suerte.setter
  def suerte(self, nueva_suerte: int):
    self.__suerte = nueva_suerte
  
  @property
  def tipo(self) -> Tipo:
    return self.__tipo
  
  @property
  def arma(self) -> Arma:
    return self.__arma
  
  @property
  def pociones(self) -> list[Pocion]:
    return self.__pociones

  def aplicar_bonificaciones(self):
    self.ataque = math.ceil(self.ataque * self.tipo.bonif_ataque)
    self.defensa = math.ceil(self.defensa * self.tipo.bonif_defensa)
    self.vida = math.ceil(self.vida * self.tipo.bonif_vida)
    self.suerte = math.ceil(self.suerte * self.tipo.bonif_suerte)

  def mostrar_atributos(self):
    return f"Ataque: {self.ataque}, Defensa: {self.defensa}, Vida: {self.vida}, Suerte: {self.suerte}"

  def recibir_ataque(self, cantidad):
    self.vida -= cantidad - self.defensa  # El daño recibido se reduce por la defensa
    if self.vida < 0:
      self.vida = 0
  
  def combate(self, defensor):
    daño = self.ataque + self.arma.daño

    if (random.random() > self.arma.probabilidad_critico + (self.suerte / 100)):
      daño *= 2
      print(f"\n{self.nombre} realizó un golpe crítico a {defensor.nombre} con {self.arma.nombre} causando {daño} puntos de daño.")
    else:
      print(f"\n{self.nombre} atacó a {defensor.nombre} con {self.arma.nombre} causando {daño} de daño.")
    
    defensor.recibir_ataque(daño)
    print(f"{defensor.nombre} tiene {defensor.vida} de vida restante.")

    if defensor.vida <= 0:
      print(f"{defensor.nombre} ha sido derrotado.")

  def beber_pocion(self, pocion):
    if random.random() > 0.20 - (self.suerte / 100):
      self.vida += self.pociones[pocion - 1].curacion
      if self.vida > 100:
        self.vida = 100
    del self.pociones[pocion - 1]

  def __str__(self) -> str:
    return f"ID: {self.id}, Nombre: {self.nombre}, Género: {self.genero}, Tipo: {self.tipo.nombre}"