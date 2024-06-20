class Arma:
  id_inicial = 1
  def __init__(self, nombre, daño, probabilidad_critico) -> None:
    self.id = Arma.id_inicial
    Arma.id_inicial += 1
    self.nombre = nombre
    self.daño = daño
    self.probabilidad_critico = probabilidad_critico

  def __str__(self) -> str:
    return f"'{self.nombre}' daño: {self.daño}, probabilidad de crítico: {self.probabilidad_critico}."