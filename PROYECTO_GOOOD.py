import random
from ahorcado import *
from funcionesproyecto import lista_pal
from Tateti import *
diccionario=lista_pal
opc='0'
while True:
    print('Hola, bienvenido a un humilde algorimo de juegos.'
          '          Elige opcion:'
          '          1. Tateti'
          '          2. Ahorcado futbolero'
          '          3. Salir')
    opc=input('---> ')
    if opc == '1':
        TATETI.start()
    elif opc == '2':
        jugar_al_ahorcado(diccionario)
    elif opc == '3':
        print('¡¡¡Chau, volve luego!!!')
        break
    else:
        print('No es una opción valida')