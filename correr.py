#Pedir datos a usuario sobre su carrera
tiempo_min= int(input("Ingresa los minutos que realizaste: "))
tiempo_seg =int(input("Ingresa los segundos restantes: "))
distancia =float(input("Ingresa la distancia total recorrida en km: "))
esfuerzo = int(input("Ingresa tu nivel de esfuerzo del 1 al 10: "))

#Calcular tiempo total en segundos
tiempo_total= tiempo_min * 60 + tiempo_seg

#Calcular ritmo de carrera
ritmo= tiempo_total/distancia
minutos=int(ritmo/60)
segundos=int(ritmo % 60)
print ("Tu ritmo de carrera es:",minutos,":", segundos, "min/km")

#Calculo de esfuerzo
if esfuerzo <=3:
    print ("Zona a trabajar: Velocidad")
if esfuerzo >= 4 and esfuerzo <=5:
    print("Zona a trabajar: Resistencia aeróbica")
if esfuerzo >=6 and esfuerzo <= 7:
    print("Zona a trabajar: Umbral")

if esfuerzo >=8 and esfuerzo <=9:
    print("Zona a trabajar: V02 máximo")
if esfuerzo == 10:
    print("Zona a trabajar: Recuperacion")


