from helpers import *
def verificar_numero_puntajes():
  while True:
    try:
        N_puntajes = int(input("Cuantos puntajes tienes: "))

        if N_puntajes < 6:
            print(f" tienes {N_puntajes}")
            break
        else:
            print("El maximo puntaje es de 5. Trata denuevo")
    except ValueError:
        print("Tienes que poner un integer")
  return N_puntajes

def login(list):
  AccountFound=False
  while not AccountFound:
    print("Cual es tu nombre?")
    NameSearch=input(": ")
    for i in range(len(list)):
      if list[i][0] == NameSearch.lower():
        nombre=NameSearch
        ID= i+1
        AccountFound=True
    if not AccountFound:
      print("Nombre no encontrado. intenta denuevo")
      delay(1)
      cl()
  N_puntajes=len(list[ID-1])-1
  delay(1)
  advance()
  cl()
  return nombre,ID,N_puntajes
  
        
       
def OpenText():
  f=open("data.txt","r").read().splitlines()
  
  list = []  
  for line in f:
    l = line.split(", ")
    list.append(l)
  return list


def registrando():
  print("Cual es tu nombre ")
  nametotext=input(":").strip()
  N_puntajes=verificar_numero_puntajes()
  f=open("data.txt","a")
  f.write("\n"+nametotext)
  f.close()
  for i in range(N_puntajes):
    while True:
      try:
        puntaje = int(input("Cual es tu puntaje: "))
        if puntaje < 1001:
          f=open("data.txt","a")
          f.write( ", " + str(puntaje))
          f.close()
          break
        else:
          print("El maximo puntaje es de 1000. Trata denuevo")
      except ValueError:
        print("Tienes que poner un integer")
  print("Tus puntajes han sido guardados")
  ID=len(OpenText())
  nombre=nametotext
  delay(0)
  advance()
  cl()
  return nombre,ID,N_puntajes
  
  



def ver_puntajes(list,ID,N_puntajes):
  print("Tus puntajes son: ")
  total=0
  for i in range(N_puntajes):
    print(list[ID-1][i+1]) 
    total += int(list[ID-1][i+1])
  print("Promedio: "+str(total/N_puntajes))
  advance()
  cl()

def ver_puntajes_generales(list):
  total = 0
  n_puntajes = 0
  for jugador in list:
    for i in range(1, len(jugador)):
      total += int(jugador[i])
      n_puntajes += 1
  print("Promedio general: ", total/n_puntajes)
  advance()
  cl()

def menu(TextList,ID,N_puntajes):
  while True:
    print("""
    Que quieres hacer: 
    a) Ver mis puntajes y promedio
    b) Ver promedio general
    c) Cerrar

    """)
    while True:
      choice = input(": ")
      if choice.lower() == "a":
        ver_puntajes(TextList,ID,N_puntajes)
        break


      elif choice.lower() == "b":
        ver_puntajes_generales(TextList)
        break

      elif choice.lower() == "c":
        print("Ojala vuelvas pronto!")
        exit()


      else:
        print("Responde a, b o c")
  
  