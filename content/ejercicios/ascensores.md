---
title: "Ascensores"
date: 2024-01-01
draft: false
languages: []
categories: ['enunciado']
tags: ['Sin Matlab', 'Sin solución']
---

# Ascensores

##  Enunciado 

En un hotel desean mejorar el sistema de control de sus ascensores que funcionan de forma independiente (supongamos que hay **N** ascensores). Para ello necesitan instalar una centralita que calcule que ascensor debe acudir a la llamada de un cliente desde una planta. Para ello la centralita dispone de la siguiente información: 

  * En qué planta se encuentra cada ascensor. 
  * Cuál el estado de cada ascensor (1: subiendo, 0: parado, -1: bajando). 
  * Desde que planta ha solicitado el cliente el ascensor. 
  * Hacia dónde quiere ir el cliente (1: subir, -1: bajar) 

Para programar la centralita necesitamos realizar los siguiente subalgoritmos: 

###  Apartado a) 

Un subalgoritmo que dada la posición de un ascensor, su estado, la planta desde donde se solicita y la dirección de la solicitud, devuelva la cercanía de dicho ascensor dependiendo si el ascensor debe acudir a la llamada o no. Si debe acudir a la llamada el subalgoritmo devolverá la diferencia de plantas en valor absoluto. Si no debe acudir a la llamada devolverá una cercanía de 10000. Un ascensor debe acudir a la llamada si: 

  * Se encuentra parado, o 
  * Si el usuario solicita subir y el ascensor está en una planta inferior y subiendo, o 
  * Si el usuario solicita bajar y el ascensor está en una planta superior y bajando. 

###  Apartado b) 

Un subalgoritmo que dado un array de enteros devuelva en qué posición se encuentra el mínimo valor. Si el mínimo está varias veces debe devolver el primer valor encontrado. 

###  Apartado c) 

Un subalgoritmo que dada las posiciones de todos los ascensores, los estados de todos los ascensores, la planta desde donde se solicita y la dirección de la solicitud, calcule cual es el ascensor más cercano utilizando los subalgoritmos de los apartados a) y b). Si ningún ascensor puede acudir a la llamada devolverá un valor de -1. 

##  Soluciones