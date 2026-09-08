#Pedir datos a usuario sobre su carrera
tiempo_min= int(input("Ingresa los minutos que realizaste: "))
tiempo_seg =int(input("Ingresa los segundos restantes: "))
distancia =float(input("Ingresa la distancia total recorrida en km: "))
esfuerzo = int(input("Ingresa tu nivel de esfuerzo del 1 al 10: "))
peso = float(input("Ingresa tu peso: "))

#Calcular tiempo total en segundos
def tiempo_total(tiempo_min, tiempo_seg):
    tiempo= tiempo_min * 60 + tiempo_seg
    return tiempo

#Calcular velocidad km/h
def velocidad_hr(tiempo_min, tiempo_seg, distancia):
    velseg = distancia/tiempo_total(tiempo_min, tiempo_seg)
    velkmhr = (velseg*3600)
    return velkmhr

#Calcular velocidad m/min
def velocidad_min (tiempo_min, tiempo_seg, distancia):
    velm_min= (velocidad_hr(tiempo_min, tiempo_seg, distancia)*1000)/60
    return velm_min

#Calcular ritmo de carrera
def ritmo(tiempo_min, tiempo_seg,distancia):
    temp = 60/velocidad_hr(tiempo_min, tiempo_seg, distancia)
    ritmo_m= int(temp)
    ritmo_s= int((temp % 1)*60)
    return print("Tu ritmo de carrera es:",ritmo_m,":",ritmo_s, "min/km")


#Calcular V02 max estimado
def v02_max(tiempo_min, tiempo_seg, distancia):
    v02= (0.2*velocidad_min(tiempo_min, tiempo_seg, distancia))+3.5
    return v02

#Calcular MET
def met(tiempo_min, tiempo_seg, distancia):
    calc_met=(v02_max(tiempo_min, tiempo_seg, distancia)/3.5)
    return calc_met

#Calcular Calorias
def calorias(peso,tiempo_min, tiempo_seg, distancia):
    peso_kcal= peso/200
    kcal= met(tiempo_min, tiempo_seg, distancia)*3.5*peso_kcal* velocidad_min(tiempo_min, tiempo_seg, distancia)
    return kcal

#Prints
print(f"Tu velocidad es: {velocidad_hr(tiempo_min, tiempo_seg, distancia):.2f} km/h")
ritmo(tiempo_min, tiempo_seg, distancia)
print (f"Tu v02 max estimado es: {v02_max(tiempo_min, tiempo_seg, distancia):.2f}")
print (f"Tu met es: {met(tiempo_min, tiempo_seg, distancia):.2f}")
print(f"Las calorias que consumiste fueron: {calorias(peso,tiempo_min, tiempo_seg, distancia):.2f}")

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