"""Constantes"""
SEGUNDOS_POR_MINUTO = 60
SEGUNDOS_POR_HORA = 3600
METROS_POR_KM = 1000
FACTOR_VO2_VELOCIDAD = 0.2
VO2_REPOSO = 3.5
DIVISOR_CALORIAS = 200

"""Devuelve el tiempo total en segundos."""
def calcular_tiempo_total(minutos, segundos):
    tiempo = minutos * SEGUNDOS_POR_MINUTO + segundos
    return tiempo

"""Devuelve la velocidad promedio en km/h."""
def calcular_velocidad_kmh(minutos, segundos, distancia_km):
    tiempo_total = calcular_tiempo_total(minutos, segundos)
    velocidad = distancia_km / tiempo_total * SEGUNDOS_POR_HORA
    return velocidad

"""Devuelve la velocidad promedio en m/min."""
def calcular_velocidad_m_min(minutos, segundos, distancia_km):
    velocidad_kmh = calcular_velocidad_kmh(minutos, segundos, distancia_km)
    velocidad_m_min = velocidad_kmh * METROS_POR_KM / SEGUNDOS_POR_MINUTO
    return velocidad_m_min

"""Devuelve el ritmo de carrera como (minutos, segundos) por km."""
def calcular_ritmo(minutos, segundos, distancia_km):
    tiempo_total = calcular_tiempo_total(minutos, segundos)
    segundos_por_km = int(tiempo_total / distancia_km)
    ritmo_minutos = segundos_por_km // SEGUNDOS_POR_MINUTO
    ritmo_segundos = segundos_por_km % SEGUNDOS_POR_MINUTO
    return ritmo_minutos, ritmo_segundos

"""Devuelve el consumo de oxigeno estimado (ml/kg/min)."""
def calcular_vo2(minutos, segundos, distancia_km):
    velocidad = calcular_velocidad_m_min(minutos, segundos, distancia_km)
    vo2 =FACTOR_VO2_VELOCIDAD * velocidad + VO2_REPOSO
    return vo2

"""Devuelve el equivalente metabolico (MET) de la carrera."""
def calcular_met(minutos, segundos, distancia_km):
    met_total = calcular_vo2(minutos, segundos, distancia_km) / VO2_REPOSO
    return met_total

"""Devuelve las calorias totales quemadas durante la carrera."""
def calcular_calorias(peso_kg, minutos, segundos, distancia_km):
    met = calcular_met(minutos, segundos, distancia_km)
    duracion_min = calcular_tiempo_total(minutos, segundos)
    duracion_min /= SEGUNDOS_POR_MINUTO
    kcal_por_min = met * VO2_REPOSO * peso_kg / DIVISOR_CALORIAS
    calorias = kcal_por_min * duracion_min
    return calorias

"""Devuelve la zona de entrenamiento segun el esfuerzo (1 a 10)."""
def obtener_zona_entrenamiento(esfuerzo):
    if esfuerzo <=3:
        return "Zona a trabajar: Velocidad"
    if esfuerzo >= 4 and esfuerzo <=5:
        return "Zona a trabajar: Resistencia aeróbica"
    if esfuerzo >=6 and esfuerzo <= 7:
        return "Zona a trabajar: Umbral"
    if esfuerzo >=8 and esfuerzo <=9:
        return "Zona a trabajar: V02 máximo"
    if esfuerzo == 10:
        return "Zona a trabajar: Recuperacion"
    
"""Devuelve el nivel de condicion fisica segun el VO2 estimado."""
def clasificar_vo2(vo2):
    if vo2 <= 30:
        return "Bajo"
    if vo2 >= 31 and vo2 <= 40:
        return "Regular"
    if vo2 >= 41 and vo2 <= 50:
        return "Bueno"
    if vo2 >= 51 and vo2 <= 60 :
        return "Muy bueno"
    if vo2 > 60:
        return "Excelente"
    

"""Pide los datos al usuario e imprime el analisis."""
minutos = int(input("Ingresa los minutos que realizaste: "))
segundos = int(input("Ingresa los segundos restantes: "))
distancia_km = float(input("Ingresa la distancia total en km: "))
peso_kg = float(input("Ingresa tu peso en kg: "))
esfuerzo = int(input("Ingresa tu nivel de esfuerzo del 1 al 10: "))

velocidad = calcular_velocidad_kmh(minutos, segundos, distancia_km)
ritmo_min, ritmo_seg = calcular_ritmo(minutos, segundos, distancia_km)
vo2 = calcular_vo2(minutos, segundos, distancia_km)
nivel_vo2 = clasificar_vo2(vo2)
met = calcular_met(minutos, segundos, distancia_km)
calorias = calcular_calorias(peso_kg, minutos, segundos, distancia_km)

print(f"Tu velocidad es: {velocidad:.2f} km/h")
print(f"Tu ritmo de carrera es: {ritmo_min}:{ritmo_seg:02d} min/km")
print(f"Tu VO2 estimado es: {vo2:.2f}")
print(f"Tu nivel de VO2 es: {nivel_vo2}")
print(f"Tu MET es: {met:.2f}")
print(f"Calorias quemadas: {calorias:.2f}")
print(f"Zona a trabajar: {obtener_zona_entrenamiento(esfuerzo)}")
