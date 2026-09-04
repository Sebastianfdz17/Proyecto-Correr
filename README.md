# Proyecto-Análisis del corredor
Contexto:
Entrenar por tu cuenta siendo un corredor, puede ser bastante abrumador al principio si no cuentas con una base de entrenamientos dependiendo de tu nivel. Realmente el progreso al momento de correr se empieza notar hasta que reconoces tus carencias y debilidades y entrenas específicamente para mejorar en dichas áreas.

Este proyecto consiste en desarrollar un programa donde se pueda analizar el rendimiento de un corredor a partir de diferente datos obtenidos durante sus entrenamientos. El usuario deberá ingresar información como la distancia corrida, el tiempo realizado, y los días que tiene para entrenar.

A partir de estos datos, el programa realizará diferentes cálculos para determinar el ritmo del corredor y analizar de manera aproximada la intensidad del esfuerzo durante los entrenamiento y estimar tiempos para otras distancia. Además, mediante un conjunto de condiciones, el sistema expondrá que aspecto del rendimiento podría recibir mayor atención, como resistencia aeróbica, velocidad o capacidad para mantener ritmos elevados.

Finalmente, el programa generará recomendaciones de entrenamiento de acuerdo con el análisis realizado. Estas recomendaciones estarán conformadas por diferentes tipos de sesiones, como carreras de baja intensidad, carreras largas, intervalos y entrenamientos de ritmo controlado, y estarán organizadas dependiendo de la cantidad de días disponibles para entrenar y que aspecto de su rendimiento necesita mejorar.

El objetivo principal del proyecto es crear una herramienta sencilla y fácil de usar que permita al corredor principiante interpretar sus propios datos de entrenamiento y obtener recomendaciones básicas de manera automática.

El Algoritmo sería el siguiente:
1. Registrar datos
   Input: distancia, tiempo, días disponibles, nivel de esfuerzo
3. Analizar Rendimiento
   Calcular mediante divisiones y multiplicaciones el ritmo por kilometro
5. Detectar áreas de mejora
   Mediante if y el nivel de esfuerzo
7. Preguntar días disponibles
8. Seleccionar los entrenamientos predeterminados
   Mediante las áreas de mejora y los días disponibles, seleccionar los entrenamientos
10. Generar plan de entrenamiento semanal
11. Finalizar
