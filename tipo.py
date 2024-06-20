class Tipo:
  id_inicial = 1
  def __init__(self, nombre, bonif_ataque, bonif_defensa, bonif_vida, bonif_suerte) -> None:
    self.id = Tipo.id_inicial
    Tipo.id_inicial += 1
    self.nombre = nombre
    self.bonif_ataque = bonif_ataque
    self.bonif_defensa = bonif_defensa
    self.bonif_vida = bonif_vida
    self.bonif_suerte = bonif_suerte

  def __str__(self) -> str:
    return f"'{self.nombre}' ataque: x{self.bonif_ataque}, defensa: x{self.bonif_defensa}, vida: x{self.bonif_vida}, suerte: x{self.bonif_suerte}."