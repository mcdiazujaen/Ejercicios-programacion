---
title: "Análisis de llamadas a procedimientos"
date: 2024-01-01
draft: false
languages: ['pseudocódigo']
categories: ['enunciado']
---


# Análisis de llamadas a procedimientos

  

##  Enunciado 

Considera el siguiente procedimiento: 
```text


 PROCEDIMIENTO Escr(ch: CARÁCTER, long: ENTERO)
 INICIO
   MIENTRAS long>0 HACER
     ESCRIBIR ch
     long <-- long - 1
   FIN_MIENTRAS
 FIN


```
###  Enunciado a) 

Si `ch` tiene el valor 'X' y `numero` el valor 5, ¿cuál sería el efecto de ejecutar cada una de las siguientes llamadas al procedimiento? 
```text


 Escr(ch,4*numero-12)
 Escr(ch,6)
 Escr(5,numero)
 Escr('/',numero)
 Escr('.',6)
 Escr('p',-10)


```
###  Enunciado b) 

Escribe llamadas al procedimiento `Escr` para que cuando se ejecuten produzcan las siguientes salidas: 

1) 35 guiones sucesivos. 

2) 6 veces tantos espacios en blanco como el valor de `numero`

3) El valor actual de `ch` 14 veces 

##  Soluciones 

Para dar la solución del ejercicio hay que tener en cuenta que el procedimiento `Escr` muestra en el dispositivo de salida el contenido de `ch` tantas veces como indique el parámetro `long`. 

###  Solución de a) 

`Escr(ch,4*numero-12)` |  Muestra el carácter 'x' 8 veces (4*numero-12) 
```text


xxxxxxxx 
  
  
```
---|---  
`Escr(ch,6)` |  Muestra el carácter 'x' 6 veces 
```text


xxxxxx
  
  
```
`Escr(5,numero)` |  La llamada _no es correcta_ , porque para ser un carácter tiene que ir entre comillas, por lo tanto tomará _5_ como un entero.   
`Escr('/',numero)` |  Muestra el carácter '/' 5 veces 
```text


/////
  
  
```
`Escr('.',6)` |  Muestra el carácter '.' 6 veces 
```text


......
  
  
```
`Escr('p',-10)` |  No muestra nada ya que -10 es menor que 0 y no entrará dentro del bucle MIENTRAS del procecimiento.   
  
  

###  Solucion de b) 

1) 35 guiones sucesivos 
```text


Escr('-',35)


```
2) 6 veces tantos espacios en blanco como el valor de `numero`
```text


Escr(' ',6*numero)


```
3) El valor actual de `ch` 14 veces 
```text


 Escr(ch,14)
```