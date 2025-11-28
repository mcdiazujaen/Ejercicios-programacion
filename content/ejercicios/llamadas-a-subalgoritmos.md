---
title: "Llamadas a subalgoritmos"
date: 2024-01-01
draft: false
languages: ['pseudocódigo']
categories: ['enunciado']
---


# Llamadas a subalgoritmos

##  Enunciado 

Dada las siguientes declaraciones en un determinado algoritmo: 
```text


a, b, c : ENTERO
k: LÓGICO
d,e : REAL


```
Y las siguientes declaraciones de subalgoritmos: 
```text


FUNCIÓN Uno (x:REAL, y:ENTERO): LÓGICO
PROCEDIMIENTO Dos (VAR x: REAL, y: ENTERO)
FUNCIÓN Tres (x:ENTERO, VAR z: LÓGICO):ENTERO


```
Decir si las siguientes llamadas a los subalgoritmos desde el cuerpo del algoritmo principal son validas o no. Justificar la respuesta: 
```text


Dos(1.4, 5)
Dos(e+2, b+3)
a <-- Dos(e,b)
Dos(a, Tres(a,k))
b <-- Tres(Dos(a,5),k)
c <-- Uno(d,5)
Dos(Tres(b,k),c)
Dos(4,c)
SI Tres(a,k) ENTONCES ...
SI Uno(d, Tres(c,k)) ENTONCES ...
a <-- Tres(c, Uno(e,b))
Tres(a,k)


```
##  Soluciones 

###  Pseudocódigo 
```text


Dos(1.4, 5)


 **Incorrecta** : el primer parámetro formal de `Dos` se pasa por variable (`VAR x:REAL`), sin embargo, el primer parámetro actual es un valor constante (`1.4`) que se pasa por copia. 


Dos(e+2, b+3)


 **Incorrecta** : el primer parámetro formal de `Dos` se pasa por variable (`VAR x:REAL`), sin embargo, el primer parámetro actual es una expresión aritmética (`e+2`) que se pasa por copia. 


a <-- Dos(e,b)


 **Incorrecta** : un procedimiento no devuelve nada asociado a su nombre, por lo tanto, la asignación es incorrecta. 


Dos(a, Tres(a,k))


 **Correcta** : El número de parámetros formales y actuales es el mismo. El tipo y orden de los parámetros es el mismo, aunque en `Dos` el parámetro formal `x` sea real y el parámetro actual `a` sea entero. El paso por variable de los parámetros se respeta. 


b <-- Tres( Dos(a,5),k)


 **Incorrecta** : el procedimiento `Dos` no devuelve nada asociado a su nombre, por lo que está mal hecha la llamada. Es decir, el primer parámetro formal de `Tres` es de tipo entero, sin embargo, el procedimiento `Dos` no devuelve un entero. 


c <-- Uno(d,5)


 **Incorrecta** : la función `Uno` devuelve un valor lógico y se pretende asignar a una variable de tipo entero. 


Dos(Tres(b,k),c)


 **Incorrecta** : el primer parámetro formal de `Dos` se pasa por variable (`VAR x:REAL`), sin embargo, el primer parámetro actual es una llamada a una función (`Tres(b,k)`) que se pasa por copia. Además la función `Tres` devuelve un entero y el primer parámetro formal de `Dos` es de tipo real. 


Dos(4,c)


 **Incorrecta** : el primer parámetro formal de `Dos` se pasa por variable (`VAR x:REAL`), sin embargo, el primer parámetro actual es un valor constante (`4`) que se pasa por copia. 


SI Tres(a,k) ENTONCES ...


 **Incorrecta** : la función `Tres` devuelve un valor entero y la condición del `SI` debe ser un valor lógico. 


SI Uno(d, Tres(c,k)) ENTONCES ...


 **Correcto** : En ambas funciones el número de parámetros formales y actuales es el mismo. El tipo y orden de los parámetros es el mismo. El paso por variable de los parámetros se respeta. Y la función `Uno` devuelve un lógico, que es el tipo que necesita la condición del `SI`. 


a <-- Tres(c, Uno(e,b))


 **Incorrecta** : el segundo parámetro formal de `Tres` se pasa por variable (`VAR z: LÓGICO`), sin embargo, el segundo parámetro actual es una llamada a una función (`Uno(e,b)`) que se pasa por copia. Además la función `Tres` devuelve un entero y el primer parámetro formal de `Dos` es de tipo real. 


Tres(a,k)  


 **Incorrecta** : la llamada a la función es correcta, pero el valor que la función devuelve no se está utilizando.
```