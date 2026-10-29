---
title: "Día de la semana"
date: 2024-01-01
draft: false
languages: []
categories: ['enunciado']
tags: ['Sin Matlab', 'Sin Pseudocódigo', 'Sin solución']
---

# Día de la semana

##  Enunciado 

La gente que trata con fechas históricas utiliza un nombre llamado **Día Juliano** para calcular el número de días entre dos sucesos. El Día Juliano es el número de días que han pasado desde el 1 de enero del año 413 a. C. Por ejemplo, el Día Juliano para el 16 de Octubre de 1956 es 2435763. Existen fórmulas para calcular el Día Juliano dada una fecha y viceversa. 

También existen fórmulas que utilizan el Día Juliano. Una fórmula muy sencilla que calcula el día de la semana de un Día Juliano dado es: 
```text
Día de la semana = (Día Juliano+1) MOD 7
```

Esta fórmula dará un resultado de 0 para el domingo, 1 para el lunes, y así sucesivamente hasta 6 para sábado. Para el Día Juliano 2435763, el resultado de esta fórmula debe ser un 2 (un martes). Escribir un algoritmo que dado un Día Juliano, escriba el día de la semana (lunes, martes, ...) que corresponde a dicho número. 

##  Soluciones