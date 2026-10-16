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
    vo2 = FACTOR_VO2_VELOCIDAD * velocidad + VO2_REPOSO
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
    if esfuerzo <= 3:
        return "Velocidad"
    if esfuerzo >= 4 and esfuerzo <= 5:
        return "Resistencia aeróbica"
    if esfuerzo >= 6 and esfuerzo <= 7:
        return "Umbral"
    if esfuerzo >= 8 and esfuerzo <= 9:
        return "VO2 máximo"
    if esfuerzo == 10:
        return "Recuperacion"

"""Devuelve el nivel de condicion fisica segun el VO2 estimado."""
def clasificar_vo2(vo2):
    if vo2 <= 30:
        return "Bajo"
    if vo2 >= 31 and vo2 <= 40:
        return "Regular"
    if vo2 >= 41 and vo2 <= 50:
        return "Bueno"
    if vo2 >= 51 and vo2 <= 60:
        return "Muy bueno"
    if vo2 > 60:
        return "Excelente"

"""Devuelve la lista de días según la cantidad de días que entrenará el usuario."""
def obtener_dias_semana(dias_disponibles):
    if dias_disponibles == 2:
        return ["Martes", "Jueves"]
    elif dias_disponibles == 3:
        return ["Lunes", "Miércoles", "Viernes"]
    elif dias_disponibles == 4:
        return ["Lunes", "Miércoles", "Viernes", "Sábado"]
    elif dias_disponibles == 5:
        return ["Lunes", "Martes", "Jueves", "Viernes", "Sábado"]
    elif dias_disponibles == 6:
        return ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
    else:
        return ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

"""Devuelve el plan de entrenamiento específico para la zona y días seleccionados."""
def generar_plan_personalizado(dias_disponibles, zona):
    dias = obtener_dias_semana(dias_disponibles)
    entrenamientos = []

    # Selección de entrenamientos según la zona recomendada
    if zona == "Velocidad":
        opciones = [
            "Piques cortos de aceleración (Sprint 50m)",
            "Carrera de técnica y multisaltos",
            "Sprints cortos con descanso completo",
            "Easy run + 4 aceleraciones finales",
            "Cuestas cortas a máxima intensidad",
            "Carrera suave + ejercicios de reactividad",
            "Descanso activo o rodaje muy suave"
        ]
    elif zona == "Resistencia aeróbica":
        opciones = [
            "Carrera continua a ritmo cómodo (Easy Run)",
            "Rodaje suave en Zona 2",
            "Carrera suave con cambios de ritmo ligeros",
            "Tirada media regenerativa",
            "Rodaje cómodo sostenido",
            "Tirada larga a ritmo suave",
            "Caminata activa o trote regenerativo"
        ]
    elif zona == "Umbral":
        opciones = [
            "Easy Run de calentamiento + 20 min a ritmo Umbral",
            "Intervalos de tiempo (Tempo Run 3x10 min)",
            "Rodaje suave de recuperación",
            "Bloques de tempo (2x15 min en Zona 3)",
            "Tirada larga con bloques a ritmo de competencia",
            "Fartlek (cambios de ritmo de 2 min)",
            "Trote muy suave de regeneración"
        ]
    elif zona == "VO2 máximo":
        opciones = [
            "Intervalos cortos (10x400m a máxima intensidad)",
            "Easy Run de recuperación",
            "Repeticiones de 1km a ritmo de VO2 máx",
            "Intervalos en cuesta de 1 minuto",
            "Fartlek intensivo (1 min fuerte / 1 min suave)",
            "Tirada larga suave de descarga",
            "Descanso activo"
        ]
    else: 
        opciones = [
            "Caminata o trote muy suave (20 min)",
            "Estiramientos dinámicos y rodaje suave",
            "Descanso total",
            "Caminata al aire libre",
            "Trote regenerativo muy corto",
            "Movilidad articular y rodaje ligero",
            "Descanso total"
        ]

    for i in range(dias_disponibles):
        entrenamientos.append(opciones[i])

    return dias, entrenamientos


"""Programa principal"""
continuar = "si"

while continuar == "si":

    minutos = int(input("Ingresa los minutos que realizaste: "))

    while minutos < 0:
        print("Error: los minutos no pueden ser negativos.")
        minutos = int(input("Ingresa los minutos que realizaste: "))

    segundos = int(input("Ingresa los segundos restantes: "))

    while segundos < 0 or segundos > 59:
        print("Error: los segundos deben estar entre 0 y 59.")
        segundos = int(input("Ingresa los segundos restantes: "))

    while minutos == 0 and segundos == 0:
        print("Error: el tiempo debe ser mayor que cero.")
        minutos = int(input("Ingresa los minutos que realizaste: "))
        segundos = int(input("Ingresa los segundos restantes: "))

        while minutos < 0:
            print("Error: los minutos no pueden ser negativos.")
            minutos = int(input("Ingresa los minutos que realizaste: "))

        while segundos < 0 or segundos > 59:
            print("Error: los segundos deben estar entre 0 y 59.")
            segundos = int(input("Ingresa los segundos restantes: "))

    distancia_km = float(input("Ingresa la distancia total en km: "))

    while distancia_km <= 0:
        print("Error: la distancia debe ser mayor que cero.")
        distancia_km = float(input("Ingresa la distancia total en km: "))

    peso_kg = float(input("Ingresa tu peso en kg: "))

    while peso_kg <= 0:
        print("Error: el peso debe ser mayor que cero.")
        peso_kg = float(input("Ingresa tu peso en kg: "))

    esfuerzo = int(input("Ingresa tu nivel de esfuerzo del 1 al 10: "))

    while esfuerzo < 1 or esfuerzo > 10:
        print("Error: el esfuerzo debe estar entre 1 y 10.")
        esfuerzo = int(input("Ingresa tu nivel de esfuerzo del 1 al 10: "))

    dias_entreno = int(input("¿Cuántos días a la semana puedes entrenar (1 a 7)?: "))

    while dias_entreno < 1 or dias_entreno > 7:
        print("Error: ingresa un número de días válido entre 1 y 7.")
        dias_entreno = int(input("¿Cuántos días a la semana puedes entrenar (1 a 7)?: "))

    velocidad = calcular_velocidad_kmh(minutos, segundos, distancia_km)
    ritmo_min, ritmo_seg = calcular_ritmo(minutos, segundos, distancia_km)
    vo2 = calcular_vo2(minutos, segundos, distancia_km)
    nivel_vo2 = clasificar_vo2(vo2)
    met = calcular_met(minutos, segundos, distancia_km)
    calorias = calcular_calorias(peso_kg, minutos, segundos, distancia_km)
    zona_trabajo = obtener_zona_entrenamiento(esfuerzo)

    print("\n--- ANALISIS DE CARRERA ---")
    print(f"Tu velocidad es: {velocidad:.2f} km/h")
    print(f"Tu ritmo de carrera es: {ritmo_min}:{ritmo_seg:02d} min/km")
    print(f"Tu VO2 estimado es: {vo2:.2f}")
    print(f"Tu nivel de VO2 es: {nivel_vo2}")
    print(f"Tu MET es: {met:.2f}")
    print(f"Calorias quemadas: {calorias:.2f}")
    print(f"Zona a trabajar: {zona_trabajo}")

    # Generación y despliegue del plan personalizado con for y listas
    dias_lista, entrenamientos_lista = generar_plan_personalizado(dias_entreno, zona_trabajo)
    
    print("\n--- PLAN DE ENTRENAMIENTO RECOMENDADO ---")
    for i in range(len(dias_lista)):
        print(f"{dias_lista[i]}: {entrenamientos_lista[i]}")

    continuar = input("\n¿Quieres analizar otra carrera? (si/no): ")

    while continuar != "si" and continuar != "no":
        print("Respuesta no válida. Escribe si o no.")
        continuar = input("¿Quieres analizar otra carrera? (si/no): ")

print("\nGracias por utilizar el programa de análisis de carrera.")