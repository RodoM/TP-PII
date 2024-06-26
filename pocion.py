import random

class Pocion:
  id_inicial = 1
  def __init__(self, nombre: str, curacion: int) -> None:
    self.__id = Pocion.id_inicial
    Pocion.id_inicial += 1
    self.__nombre = nombre
    self.__curacion = curacion

  @property
  def id(self) -> int:
    return self.__id
  
  @property
  def nombre(self) -> str:
    return self.__nombre
  
  @property
  def curacion(self) -> int:
    return self.__curacion
  
  # función que simula utilizar una poción, tiene una probabilidad de 20% de no tener efecto.
  def utilizar(self) -> int:
    if random.random() < 0.80:
      return self.curacion
    else:
       return 0

  def __str__(self) -> str:
    return f"'{self.nombre}' curación: {self.curacion}."