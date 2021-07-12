menu = ["grafico contagios ultimas 7 fechas:","mostrar rango etario con mayor tasa de contagios:","mostrar sexo con mayor tasa de contagios:","mostrar rango etario y sexo con mayor tasa de contagios:","mostrar cantidad de contagiados por rango etarioque no pasaron por etapa clinica, aquellos que estan en etapa clinica y aquellos que probablemente pasaron por etapa clinica:","mostrar metrica de comparacion:"]
menu2 = ["elija sexo o  rango etario","grafico rango etario","grafico sexo","grafico rango etario y sexo","cantidad de contagiados en etapa clinica, no etapa clinica, probablemente etapa clinica","metrica de comparacion"]
salir=False
def menu1():
  print("\n") 
  print("      ingrese una opción: ") 
  j = 0 
  for i in range(6): 
    j = j + 1 
    print(j,end=')')
    print(menu[i])
  print("7) Salir")
  print("\n")
def opciones(a):  
    print("---",menu2[a],"---")
def respuesta():
    verdadero = False 
    opc = 0 
    while (not verdadero): 
        try:
            opc = int(input("ingrese una opción: >"))
            verdadero = True
        except ValueError: 
            print('ingrese una opción valida: >')
        if opc == 7:
            break
    return opc
while True:
    menu1()
    opc = respuesta()
    if opc < 7:
        opciones(opc)
    if opc == 7:
        break
    if opc > 7:
        print("\n Pon un numero entre el 1 y el 7")
        break
print("TERMINÓ")