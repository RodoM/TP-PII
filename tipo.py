class Tipo:
  id_inicial = 1
  def __init__(self, nombre: str, bonif_ataque: float, bonif_defensa: float, bonif_vida: float) -> None:
    self.__id = Tipo.id_inicial
    Tipo.id_inicial += 1
    self.__nombre = nombre
    self.__bonif_ataque = bonif_ataque
    self.__bonif_defensa = bonif_defensa
    self.__bonif_vida = bonif_vida

  @property
  def id(self) -> int:
    return self.__id
  
  @property
  def nombre(self) -> str:
    return self.__nombre
  
  @property
  def bonif_ataque(self) -> float:
    return self.__bonif_ataque
  
  @property
  def bonif_defensa(self) -> float:
    return self.__bonif_defensa
  
  @property
  def bonif_vida(self) -> float:
    return self.__bonif_vida

  def __str__(self) -> str:
    return f"'{self.nombre}' ataque: x{self.bonif_ataque}, defensa: x{self.bonif_defensa}, vida: x{self.bonif_vida}."