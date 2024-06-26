from datos import *
from typing import List

def menu():
  print("\n1. Mostrar personajes\n2. Crear nuevo personaje\n3. Seleccionar personaje\n4. Eliminar personaje\n5. Salir")

# función para mostrar el listado de personajes.
def mostrar_personajes(id: int = 0) -> None:
  if len(personajes) > 0:
    print("\n--- Listado de personajes ---")
    for personaje in personajes:
      if personaje.id != id and personaje.vida > 0:
        print(personaje)
  else:
    print("No hay personajes disponibles.")

# función que asigna 10 puntos a los atributos del personaje. 
def asignar_puntos(puntos: int, atributo: str) -> None:
  while puntos > 0:
    print(f"Puntos disponibles: {puntos}")
    try:
      puntos_a_asignar = int(input(f"Ingrese la cantidad de puntos a asignar a {atributo}: "))
      if 0 <= puntos_a_asignar <= puntos:
        return puntos_a_asignar
      else:
        print("Cantidad de puntos no válida. Intente de nuevo.")
    except:
      print("Cantidad de puntos no válida. Ingrese un número entero.")
  return

# función que permite seleccionar el tipo del personaje.
def seleccionar_tipo() -> Tipo:
  print("\n--- Listado de tipos ---")
  for i, tipo in enumerate(tipos, 1):
    print(f"{i}. {tipo}")

  while True:
    try:
      opt = int(input("Seleccione un tipo para el personaje: ")) - 1

      if 0 <= opt <= len(tipos) - 1:
        return tipos[opt]
      else:
        print("Opción inválida.")
    except:
      print("Opción inválida. Ingrese un número entero.")

# función que permite seleccionar el arma del personaje.
def seleccionar_arma() -> Arma:
  print("\n--- Listado de armas ---")
  for i, arma in enumerate(armas, 1):
    print(f"{i}. {arma}")

  while True:
    try:
      opt = int(input("Seleccione un arma para el personaje: ")) - 1

      if 0 <= opt <= len(armas) - 1:
        return armas[opt]
      else:
        print("Opción inválida.")
    except:
      print("Opción inválida. Ingrese un número entero.")

# función que permite seleccionar las pociones del personaje.
def seleccionar_pociones() -> List[Pocion]:
  print("\n--- Listado de pociones ---")
  for i, pocion in enumerate(pociones, 1):
    print(f"{i}. {pocion}")

  pociones_seleccionadas = []
  while True:
    try:
      opt = int(input("Seleccione un/unas pociones para el personaje (0 para continuar): ")) - 1
      
      if opt == -1:
        return pociones_seleccionadas
      if 0 <= opt <= len(pociones) - 1:
        pociones_seleccionadas.append(pociones[opt])
      else:
        print("Opción inválida.")
    except:
      print("Opción inválida. Ingrese un número entero.")

# funcion para crear un nuevo personaje.
def crear_personaje() -> None:
  nombre = input("Ingrese el nombre del personaje: ")
  genero = input("Ingrese el género del personaje: ")
  puntos = 10
  atributos = ["Ataque", "Defensa"]
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
  
  nuevo_personaje = Personaje(nombre=nombre, genero=genero, ataque=valores_atributos["ataque"], defensa=valores_atributos["defensa"], tipo=tipo, arma=arma, pociones=pociones_seleccionadas)
  nuevo_personaje.aplicar_bonificaciones()
  personajes.append(nuevo_personaje)
  print(f"Personaje {nombre} creado con éxito.")

def menu_personaje() -> None:
  print("\n1. Mostrar atributos\n2. Mostrar arma.\n3. Mostrar pociones.\n4. Pelear.\n5. Beber poción.\n6. Salir")

# función para seleccionar un personaje basado en su ID.
def seleccionar_personaje(id = 0) -> Personaje:
  try:
    opt = int(input("Ingrese el ID del personaje: "))
    for personaje in personajes:
      if personaje.id == opt and personaje.vida > 0 and personaje.id != id:
        print(f"Personaje seleccionado: {personaje.nombre}")
        return personaje
    print("No existe o esta disponible el personaje con ese ID.")
  except:
    print("ID inválido. Ingrese un número entero.")
def combate(personaje1: Personaje, personaje2: Personaje) -> None:
  daño_base = personaje1.ataque + personaje1.arma.daño
  daño = personaje1.ataque + personaje1.arma.utilizar()
  if daño > daño_base:
    print(f"\n{personaje1.nombre} realizó un golpe crítico a {personaje2.nombre} con {personaje1.arma.nombre} causando {daño} puntos de daño.")
  else:
      print(f"\n{personaje1.nombre} atacó a {personaje2.nombre} con {personaje1.arma.nombre} causando {daño} puntos de daño.")
  personaje2.recibir_ataque(daño)
  print(f"{personaje2.nombre} tiene {personaje2.vida} puntos de vida restante.")

# función para eliminar un personaje basado en su ID.
def eliminar_personaje() -> None:
  try:
    opt = int(input("Ingrese el ID del personaje que desea eliminar: "))
    for personaje in personajes:
      if personaje.id == opt:
        personajes.remove(personaje)
        print("Se eliminó con éxito el personaje.")
        return
    print("No existe ningún personaje con ese ID.")
  except:
    print("ID inválido. Ingrese un número entero.")


while True:
  menu()
  opt = input("Seleccione una opción: ")

  if opt == "1":
    mostrar_personajes()

  elif opt == "2":
    crear_personaje()

  elif opt == "3":
    if len(personajes) > 0:
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
          if len(personajes) > 1:
            mostrar_personajes(personaje_seleccionado.id)
            defensor = seleccionar_personaje(personaje_seleccionado.id)
            if defensor:
              combate(personaje_seleccionado, defensor)
              if defensor.vida > 0:
                combate(defensor, personaje_seleccionado)
              else:
                print(f"{defensor.nombre} ha sido derrotado.")
          else:
            print("Debe haber al menos 2 personajes disponibles para realizar un combate.")


        elif opt2 == "5":
          try:
            pocion = int(input("Ingrese la poción que desea beber: "))
            curacion = personaje_seleccionado.pociones[pocion - 1].utilizar()
            if curacion == 0:
              print("¡La poción no tuvo efecto!")
            else:
              personaje_seleccionado.vida = curacion
              print(f"{personaje_seleccionado.nombre} ha bebido una poción y su vida paso a {personaje_seleccionado.vida}")
            del personaje_seleccionado.pociones[pocion - 1]
          except:
            print("Opción inválida.")

        elif opt2 == "6":
          personaje_seleccionado = None

        else:
          print("Opción inválida.")
    else:
      print("No hay personajes disponibles. Primero debe crear uno")

  elif opt == "4":
    eliminar_personaje()

  elif opt == "5":
    print("Hasta luego!")
    break

  else:
    print("Opción inválida.")