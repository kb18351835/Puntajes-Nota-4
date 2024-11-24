from functions import *
from helpers import *
registered = False
print("Bienvenido a tu contador de puntajes, aqui podras registrar tus puntajes de paes y promedio, minimo y maximo!")
delay(5)

print("Entrando a base de datos ...")
delay(2)
cl()
TextList=OpenText()
while not registered:
  print("""
  Haz estado aqui antes? :
  a) si
  b) no""")
  choice= input(":")
  if choice.lower() == "a":
    delay(2)
    print("Loging in ...")
    cl()
    nombre , ID , N_puntajes = login(TextList)
          
    registered = True
    
  elif choice.lower() == "b":
    delay(2)
    print("Registrando ...")
    cl()
    
    nombre , ID , N_puntajes = registrando()
    registered = True
    TextList=OpenText()
  else:
    print("Responde a o b")
cl()

print(f"Bienvenido al menu principal {nombre}! Tu ID es: {ID} Tienes {N_puntajes} puntajes.")
menu(TextList,ID,N_puntajes)

