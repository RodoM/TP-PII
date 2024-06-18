from personaje import Personaje

class Personajes:
  def __init__(self):
    self.lista_personajes = []

  def mostrar_personajes(self):
    for personaje in self.lista_personajes:
      print(f"ID: {personaje.id}, Nombre: {personaje.nombre}, Vida: {personaje.vida}")

  def agregar_personaje(self):
    # pedir por input los datos de personaje, crearlo y agregarlo a la lista de personajes
    nombre = input("Ingrese el nombre del personaje: ")
    genero = input("Ingrese el genero del personaje: ")
    puntos = 10
    # pj = Persanaje(nombre, genero)
    # self.lista_personajes.append(pj)
    # Pregunte secuencialmente cuantos puntos asignar a cada atributo, al ultimo asignarle los puntos disponibles restantes
    
  def usar_personaje(self, id):
    personaje = self.buscar_personaje_por_id(id)
    if personaje:
      return personaje
    else:
      print(f"Personaje con ID {id} no encontrado")
      return None

  def eliminar_personaje(self, id):
    personaje = self.buscar_personaje_por_id(id)
    if personaje:
      self.lista_personajes.remove(personaje)
      print(f"Personaje con ID {id} eliminado")
    else:
      print(f"Personaje con ID {id} no encontrado")

  def buscar_personaje_por_id(self, id):
    for personaje in self.lista_personajes:
      if personaje.id == id:
        return personaje
    return None