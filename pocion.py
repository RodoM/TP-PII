class Pocion:
  id_inicial = 1
  def __init__(self, nombre, curacion) -> None:
    self.id = Pocion.id_inicial
    Pocion.id_inicial += 1
    self.nombre = nombre
    self.curacion = curacion

  def __str__(self) -> str:
    return f"'{self.nombre}' curación: {self.curacion}."