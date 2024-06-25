from datos import *
from typing import List

def menu():
  print("\n1. Mostrar personajes\n2. Crear nuevo personaje\n3. Seleccionar personaje\n4. Eliminar personaje\n5. Salir")

def mostrar_personajes(id: int = 0) -> None:
  print("\n--- Listado de personajes ---")
  for personaje in personajes:
    if personaje.id != id and personaje.vida > 0:
      print(personaje)

def asignar_puntos(puntos: int, atributo: str) -> None:
  while puntos > 0:
    print(f"Puntos disponibles: {puntos}")
    puntos_a_asignar = int(input(f"Ingrese la cantidad de puntos a asignar a {atributo}: "))
    if 0 <= puntos_a_asignar <= puntos:
      return puntos_a_asignar
    else:
      print("Cantidad de puntos no válida. Intente de nuevo.")
  return

def seleccionar_tipo() -> Tipo:
  print("\n--- Listado de tipos ---")
  for i, tipo in enumerate(tipos, 1):
    print(f"{i}. {tipo}")

  while True:
    opt = int(input("Seleccione un tipo para el personaje: ")) - 1

    if 0 <= opt <= len(tipos) - 1:
      return tipos[opt]
    else:
      print("Opción inválida.")

def seleccionar_arma() -> Arma:
  print("\n--- Listado de armas ---")
  for i, arma in enumerate(armas, 1):
    print(f"{i}. {arma}")

  while True:
    opt = int(input("Seleccione un arma para el personaje: ")) - 1

    if 0 <= opt <= len(armas) - 1:
      return armas[opt]
    else:
      print("Opción inválida.")

def seleccionar_pociones() -> List[Pocion]:
  print("\n--- Listado de pociones ---")
  for i, pocion in enumerate(pociones, 1):
    print(f"{i}. {pocion}")

  pociones_seleccionadas = []
  while True:
    opt = int(input("Seleccione un/unas pociones para el personaje (0 para continuar): ")) - 1
    
    if opt == -1:
      return pociones_seleccionadas
    if 0 <= opt <= len(pociones) - 1:
      pociones_seleccionadas.append(pociones[opt])
    else:
      print("Opción inválida.")

def crear_personaje() -> None:
  nombre = input("Ingrese el nombre del personaje: ")
  genero = input("Ingrese el genero del personaje: ")
  puntos = 10
  atributos = ["Ataque", "Defensa", "Suerte"]
  valores_atributos = {}

  for atributo in atributos:
    if puntos > 0:
      puntos_asignados = asignar_puntos(puntos, atributo)
      valores_atributos[atributo.lower()] = puntos_asignados
      puntos -= puntos_asignados
    else:
      valores_atributos[atributo.lower()] = 0

  tipo = seleccionar_tipo()
  arma = seleccionar_arma()
  pociones_seleccionadas = seleccionar_pociones()
  
  nuevo_personaje = Personaje(nombre=nombre, genero=genero, ataque=valores_atributos["ataque"], defensa=valores_atributos["defensa"], suerte=valores_atributos["suerte"], tipo=tipo, arma=arma, pociones=pociones_seleccionadas)
  nuevo_personaje.aplicar_bonificaciones()
  personajes.append(nuevo_personaje)
  print(f"Personaje {nombre} creado con éxito.")

def menu_personaje() -> None:
  print("\n1. Mostrar atributos\n2. Mostrar arma.\n3. Mostrar pociones.\n4. Pelear.\n5. Beber poción.\n6. Salir")

def seleccionar_personaje(id = 0) -> Personaje:
  opt = int(input("Ingrese el ID del personaje: "))
  for personaje in personajes:
    if personaje.id == opt and personaje.vida > 0 and personaje.id != id:
      print(f"Personaje seleccionado: {personaje.nombre}")
      return personaje
  print("No existe o esta disponible el personaje con ese ID.")

def eliminar_personaje() -> None:
  opt = int(input("Ingrese el ID del personaje que desea eliminar: "))
  for personaje in personajes:
    if personaje.id == opt:
      del personajes[opt - 1]
      print("Se eliminó con éxito el personaje.")
      return
  print("No existe ningún personaje con ese ID.")


while True:
  menu()
  opt = input("Seleccione una opción: ")

  if opt == "1":
    mostrar_personajes()

  elif opt == "2":
    crear_personaje()

  elif opt == "3":
    personaje_seleccionado = seleccionar_personaje()

    while personaje_seleccionado:
      menu_personaje()
      opt2 = input("Seleccione una opción: ")

      if opt2 == "1":
        print(personaje_seleccionado.mostrar_atributos())

      elif opt2 == "2":
        print(personaje_seleccionado.arma)

      elif opt2 == "3":
        if len(personaje_seleccionado.pociones) > 0:
          for i, pocion in enumerate(personaje_seleccionado.pociones, 1):
            print(f"{i}. {pocion}")
        else:
          print("No tiene pociones.")

      elif opt2 == "4":
        mostrar_personajes(personaje_seleccionado.id)
        defensor = seleccionar_personaje(personaje_seleccionado.id)
        if defensor:
          personaje_seleccionado.combate(defensor)
          if defensor.vida > 0:
            defensor.combate(personaje_seleccionado)

      elif opt2 == "5":
        pocion = int(input("Ingrese el ID de la poción que desea beber: "))
        vida_inicial = personaje_seleccionado.vida
        personaje_seleccionado.beber_pocion(pocion)
        if vida_inicial == personaje_seleccionado.vida:
          print("¡La poción no tuvo efecto!")
        else:
          print(f"{personaje_seleccionado.nombre} ha bebido una poción y su vida paso a {personaje_seleccionado.vida}")

      elif opt2 == "6":
        personaje_seleccionado = None

      else:
        print("Opción inválida.")

  elif opt == "4":
    eliminar_personaje()

  elif opt == "5":
    print("Hasta luego!")
    break

  else:
    print("Opción inválida.")