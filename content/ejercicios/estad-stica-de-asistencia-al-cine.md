---
title: "Estadística de asistencia al cine"
date: 2024-01-01
draft: false
languages: []
categories: ['enunciado']
tags: ['Sin Matlab', 'Sin solución']
---

# Estadística de asistencia al cine

##  Enunciado 

Se ha realizado una encuesta a la población sobre la cantidad de veces que van al cine a lo largo de un año, y se desean obtener estadísticas según el sexo y grupo de edad. 

Implementa un programa que lea para cada persona encuestada: el número de veces que va al cine, su sexo (H o M), su edad (un entero positivo en el rango [2, 100]) y calcule las siguientes estadísticas (sin utilizar estructuras de datos): 

  * Media del número de veces que van al cine según el sexo. 
  * Considerando los siguientes grupos de edad: niños (2-12 años), adolescentes (13-18 años) y adultos (19-100 años), mostrar cuál es el grupo de edad que más va al cine. 

Para el desarrollo del programa se ha de realizar la siguiente descomposición modular: 

  * _**LecturaSexo**_ : Módulo que haga una captura perfecta del sexo. 
  * _**LecturaNumero**_ : Módulo que dados como parámetros de entrada dos enteros, haga una captura perfecta de otro entero comprendido en el rango delimitado por los parámetros de entrada. 
  * **Programa principal** que lea desde teclado el sexo y la edad (utilizando los módulos anteriores) de cada persona y escriba en pantalla los resultados pedidos de la encuesta. El número de personas a los que se le pasa la encuesta se debe pedir también por teclado (el número de encuestados ha de ser un número entre 2 y 500). 

##  Soluciones