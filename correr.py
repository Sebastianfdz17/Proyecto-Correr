
"""Constantes"""

SEGUNDOS_POR_MINUTO = 60
SEGUNDOS_POR_HORA = 3600
METROS_POR_KM = 1000
FACTOR_VO2_VELOCIDAD = 0.2
VO2_REPOSO = 3.5
DIVISOR_CALORIAS = 200

"""Funciones de manejo de cadenas de texto"""

def procesar_nombre(nombre):
    nombre = nombre.strip()
    nombre = nombre.title()
    return nombre

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
        return "Recuperacion"
    elif esfuerzo <= 5:
        return "Resistencia aeróbica"
    elif esfuerzo <= 7:
        return "Umbral"
    elif esfuerzo <= 9:
        return "VO2 máximo"
    else:
        return "Velocidad"

"""Devuelve el nivel de condicion fisica segun el VO2 estimado."""

def clasificar_vo2(vo2):
    if vo2 <= 30:
        return "Bajo"
    elif vo2 < 41:
        return "Regular"
    elif vo2 < 51:
        return "Bueno"
    elif vo2 < 61:
        return "Muy bueno"
    else:
        return "Excelente"

"""Devuelve la lista de días según la cantidad de días que entrenará el usuario."""

def obtener_dias_semana(dias_disponibles):
    if dias_disponibles == 1:
        return ["Miércoles"]
    elif dias_disponibles == 2:
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
        return ["Lunes", "Martes", "Miércoles", "Jueves",
                "Viernes", "Sábado", "Domingo"]

"""Devuelve el plan de entrenamiento específico para la zona y días seleccionados."""

def generar_plan_personalizado(dias_disponibles, zona):
    dias = obtener_dias_semana(dias_disponibles)
    entrenamientos = [
        [
            "Piques cortos de aceleración",
            "Carrera de técnica y movilidad",
            "Sprints cortos con descanso completo",
            "Carrera suave + aceleraciones finales",
            "Cuestas cortas",
            "Carrera suave + ejercicios de coordinación",
            "Descanso activo o rodaje muy suave"
        ],
        [
            "Carrera continua a ritmo cómodo (Easy Run)",
            "Rodaje suave en Zona 2",
            "Carrera suave con cambios de ritmo ligeros",
            "Tirada media regenerativa",
            "Rodaje cómodo sostenido",
            "Tirada larga a ritmo suave",
            "Caminata activa o descanso"
        ],
        [
            "Carrera suave + bloques a ritmo umbral",
            "Intervalos de tiempo (Tempo Run 3x10 min)",
            "Rodaje suave de recuperación",
            "Bloques de tempo (2x15 min)",
            "Tirada larga con ritmo controlado",
            "Fartlek (cambios de ritmo de 2 min)",
            "Trote suave de regeneración"
        ],
        [
            "Intervalos de 400 m",
            "Easy Run de recuperación",
            "Repeticiones de 1 km",
            "Intervalos controlados en cuesta",
            "Fartlek (1 min fuerte / 1 min suave)",
            "Tirada larga suave",
            "Descanso activo"
        ],
        [
            "Caminata o trote muy suave",
            "Movilidad y rodaje suave",
            "Descanso total",
            "Caminata al aire libre",
            "Trote regenerativo corto",
            "Movilidad articular y rodaje ligero",
            "Descanso total"
        ]
    ]
    if zona == "Velocidad":
        fila = 0
    elif zona == "Resistencia aeróbica":
        fila = 1
    elif zona == "Umbral":
        fila = 2
    elif zona == "VO2 máximo":
        fila = 3
    else:
        fila = 4
    entrenamientos_dia = []
    
    for i in range(dias_disponibles):
        entrenamientos_dia.append(entrenamientos[fila][i])
    return dias, entrenamientos_dia

"""Guarda los resultados de la carrera en un archivo."""

def guardar_historial(nombre, distancia_km, minutos, segundos,
                      velocidad, ritmo_min, ritmo_seg, vo2,
                      nivel_vo2, met, calorias, esfuerzo, zona):
    archivo = open("historial_carreras.txt", "a", encoding="utf-8")
    print("----------------------------------------", file=archivo)
    print("Nombre:", nombre, file=archivo)
    print("Distancia:", distancia_km, "km", file=archivo)
    print("Tiempo:", minutos, "minutos y", segundos, "segundos", file=archivo)
    print("Velocidad:", velocidad, "km/h", file=archivo)
    print("Ritmo:", ritmo_min, "minutos y", ritmo_seg, "segundos por km", file=archivo)
    print("VO2 estimado:", vo2, file=archivo)
    print("Nivel de VO2:", nivel_vo2, file=archivo)
    print("MET:", met, file=archivo)
    print("Calorias:", calorias, file=archivo)
    print("Esfuerzo:", esfuerzo, file=archivo)
    print("Zona:", zona, file=archivo)
    print("----------------------------------------\n", file=archivo)
    archivo.close()

"""Consulta los resultados guardados en el archivo."""

def consultar_historial():
    archivo = open("historial_carreras.txt", "r", encoding="utf-8")
    print("\n--- HISTORIAL DE CARRERAS ---\n")
    contenido = False
    for linea in archivo:
        print(linea, end="")
        contenido = True
    if contenido == False:
        print("Todavía no hay carreras registradas.")
    archivo.close()

"""Programa principal"""

archivo = open("historial_carreras.txt", "a", encoding="utf-8")
archivo.close()
continuar = "si"
while continuar == "si":
    print("\n===== ANALIZADOR DE CARRERA =====")
    print("1. Analizar una carrera")
    print("2. Consultar historial")
    print("3. Salir")
    opcion = input("\nSelecciona una opción: ")
    if opcion == "1":
        nombre = input("\nIngresa tu nombre: ")
        nombre = procesar_nombre(nombre)
        print("\nBienvenido al analizador de carrera, " + nombre)
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

        """Calculos"""

        velocidad = calcular_velocidad_kmh(minutos, segundos, distancia_km)
        ritmo_min, ritmo_seg = calcular_ritmo(minutos, segundos, distancia_km)
        vo2 = calcular_vo2(minutos, segundos, distancia_km)
        nivel_vo2 = clasificar_vo2(vo2)
        met = calcular_met(minutos, segundos, distancia_km)
        calorias = calcular_calorias(peso_kg, minutos, segundos, distancia_km)
        zona_trabajo = obtener_zona_entrenamiento(esfuerzo)

        """Mostrar resultados"""

        print("\n--- ANALISIS DE CARRERA DE " + nombre.upper() + " ---")
        print(f"Tu velocidad es: {velocidad:.2f} km/h")
        print(f"Tu ritmo de carrera es: {ritmo_min}:{ritmo_seg:02d} min/km")
        print(f"Tu VO2 estimado es: {vo2:.2f}")
        print(f"Tu nivel de VO2 es: {nivel_vo2}")
        print(f"Tu MET es: {met:.2f}")
        print(f"Calorias quemadas: {calorias:.2f}")
        print(f"Zona a trabajar: {zona_trabajo}")

        """Generar plan"""
        dias_lista, entrenamientos_lista = generar_plan_personalizado(
            dias_entreno, zona_trabajo
        )

        print("\n--- PLAN DE ENTRENAMIENTO RECOMENDADO ---")
        for i in range(len(dias_lista)):
            print(f"{dias_lista[i]}: {entrenamientos_lista[i]}")
            
        """Guardar resultados"""
        guardar_historial(
            nombre, distancia_km, minutos, segundos,
            velocidad, ritmo_min, ritmo_seg, vo2,
            nivel_vo2, met, calorias, esfuerzo, zona_trabajo
        )
        print("\nTu carrera se guardó correctamente en el historial.")
    elif opcion == "2":
        consultar_historial()
    elif opcion == "3":
        continuar = "no"
        print("\nGracias por utilizar el analizador de carrera.")
    else:
        print("\nOpción no válida. Selecciona 1, 2 o 3.")
print("\nPrograma finalizado.")
