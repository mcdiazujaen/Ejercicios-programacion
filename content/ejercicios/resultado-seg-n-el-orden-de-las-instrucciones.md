---
title: "Resultado según el orden de las instrucciones"
date: 2024-01-01
draft: false
languages: ['pseudocódigo']
categories: ['enunciado']
---

# Resultado según el orden de las instrucciones

##  Enunciado

¿En cuál de los siguientes pares es importante el orden de los enunciados? En otras palabras, si se modifica el orden de ellos, ¿cambian los resultados finales? (Supóngase que X<>Y<>Z). 
```text
a) X <-- Y
   Y <-- Z

b) X <-- Y
   Z <-- X

c) X <-- Z
   X <-- Y

d) Z <-- Y
   X <-- Y

```
##  Soluciones

Para demostrar las respuestas de este ejercicio daremos valores distintos a X, Y, Z. En nuestro caso le vamos a dar los valores siguientes: 
```text
X = 1	; 	Y = 2	; 	Z = 3

```
**a)** El resultado final **SI** cambia al cambiar el orden. 

Con el orden normal obtenemos las siguientes soluciones: 
```text
X = 2	; Y = 3	; Z = 3

```
Con el orden inverso, como Y ha cambiado tenemos que adjudicarle ese valor a X, por lo tanto nos quedaría: 
```text
X = 3	; Y = 3	; Z = 3

```
En este caso se observa que si variamos el orden del enunciado no obtenemos lo mismo, entonces, _no da igual_

**b)** El resultado final **SI** cambia al cambiar el orden. 

Repitiendo los pasos anteriores, tenemos: En el orden normal, a Z le asignamos un valor que ha variado en el primer cambio: 
```text
X = 2	; Y = 2	; Z = 2

```
Orden inverso: 
```text
X = 2	; Y = 2	; Z = 1

```
En este caso también varía, ya que no obtenemos lo mismo al cambiar el orden. _No da igual_

**c)** El resultado final **SI** cambia al cambiar el orden. En este caso le asignamos a X tanto en el orden normal como en el inverso, así que quedaría: 
```text
Orden normal:  X = 2 ; Y = 2 ; Z = 3
Orden inverso: X = 3 ; Y = 2 ; Z = 3

```
No obtenemos lo mismo, por lo tanto,_no da igual_. 

**d)** El resultado final **NO** cambia al cambiar el orden. 

Volvemos a hacer el mismo procedimiento: 
```text
Orden normal:  X = 2 ; Y = 2 ; Z = 2
Orden inverso: X = 2 ; Y = 2 ; Z = 2

```
En este caso se observa que hemos obtenido el mismo resultado, por lo tanto _sí que da igual el orden del enunciado_.