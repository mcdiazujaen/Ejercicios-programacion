---
title: "Paso de segundos a hora-min-seg"
date: 2024-01-01
draft: false
languages: ['pseudocódigo']
categories: ['enunciado']
---


# Paso de segundos a hora-min-seg

##  Enunciado 

Diseñar un algoritmo para convertir un tiempo expresado en segundos a un formato que lo represente en horas, minutos y segundos. 

##  Soluciones 

###  Pseudocódigo 
```text


ALGORITMO ConvertirSegundos
ENTRADAS:
   tiempo: ENTERO    _(Número de segundos que queremos convertir)_
SALIDAS:
   horas: ENTERO     _(Las horas que hay en de la variable tiempo)_
   minutos: ENTERO   _(Los minutos restantes de convertir la variable tiempo)_
   segundos: ENTERO  _(Los segundos restantes de convertir la variable tiempo)_
VARIABLES:
INICIO
   _(Leer el tiempo en segundos)_
   ESCRIBIR "Introduzca hora en segundos: "
   LEER tiempo

   _(Convertir tiempo en horas, minutos y segundos)_
   horas <-- tiempo DIV 3600
   minutos <-- (tiempo MOD 3600) DIV 60
   segundos <-- (tiempo MOD 3600) MOD 60

   _(Mostrar el resultado)_
   ESCRIBIR "La hora es:", hora, ":", minutos, ":", segundos
FIN
```