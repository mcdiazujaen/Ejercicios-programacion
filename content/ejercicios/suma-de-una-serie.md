---
title: "Suma de una serie"
date: 2024-01-01
draft: false
languages: ['c', 'pseudocódigo']
professors: ['angel']
categories: ['enunciado', 'comentario', 'análisis']
tags: ['sin_matlab']
---

# Suma de una serie

##  Enunciado 

Diseñar un algoritmo para calcular la suma de los siguientes 100 primeros términos de la serie: 
```text
  1 - 1/2 + 1/4 - 1/6 + 1/8 - 1/10 + 1/12 - ...

```
##  Soluciones

###  Diseño en pseudocódigo 
```text
 ALGORITMO Suma_serie
 ENTRADAS:
   _(No hay)_
 SALIDAS: 
   suma: REAL    _(La suma de los 100 primeros términos de la serie)_
 VARIABLES: 
   i: ENTERO
   signo: ENTERO
 INICIO
   suma <- 1
   signo <-- -1
   PARA i <-- 1 HASTA 99 CON INCREMENTO DE 1 HACER
     suma <-- signo * (suma/(2*i))
     signo <-- signo * (-1)
   FIN PARA
   ESCRIBIR("La suma vale:", suma)
 FIN
```