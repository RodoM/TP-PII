class Arma:
  id_inicial = 1
  def __init__(self, nombre: str, daño: int, probabilidad_critico: float) -> None:
    self.__id = Arma.id_inicial
    Arma.id_inicial += 1
    self.__nombre = nombre
    self.__daño = daño
    self.__probabilidad_critico = probabilidad_critico

  @property
  def id(self) -> int:
    return self.__id

  @property
  def nombre(self) -> str:
    return self.__nombre
  
  @property
  def daño(self) -> int:
    return self.__daño
  
  @property
  def probabilidad_critico(self) -> float:
    return self.__probabilidad_critico

  def __str__(self) -> str:
    return f"'{self.nombre}' daño: {self.daño}, probabilidad de crítico: {self.probabilidad_critico}."