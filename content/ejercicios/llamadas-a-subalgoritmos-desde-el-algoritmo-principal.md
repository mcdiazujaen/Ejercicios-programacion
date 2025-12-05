---
title: "Llamadas a subalgoritmos desde el algoritmo principal"
date: 2024-01-01
draft: false
languages: ['pseudocódigo']
categories: ['enunciado']
---

# Llamadas a subalgoritmos desde el algoritmo principal

##  Enunciado 

Dadas las siguientes declaraciones en un determinado algoritmo: 
```text
a, b, c : ENTERO
si: LÓGICO

```
y las siguientes declaraciones de subalgoritmos: 
```text
FUNCIÓN uno(x: ENTERO, y: ENTERO): LÓGICO
PROCEDIMIENTO dos(VAR x:ENTERO, VAR y: ENTERO)
FUNCIÓN tres(x: ENTERO): ENTERO

```
¿Cuáles de las siguientes llamadas a los subalgoritmos desde el cuerpo del algoritmo principal, son válidas y por qué? 
```text
a) SI uno(a, b) ENTONCES ...
b) si <-- dos(c,5)
c) SI tres(a) ENTONCES ...
d) dos(a, b+3)
e) dos(a, tres(a))
f) b <-- tres(dos(a,5))
g) si <-- uno(c, 5)
h) dos(tres(b), c)
i) dos(4, c)

```
##  Soluciones 
```text
a) SI uno(a, b) ENTONCES ...

```
La llamada está bien, porque está llamando a una función y además lo está utilizando como lógico. Las variables coinciden con el tipo que son, es decir, tanto `a` como `b` son enteros. Por lo tanto la llamada es **CORRECTA**. 
```text
b) si <-- dos(c,5)

```
En este caso la variable `si` es lógica. La asignación que le está haciendo es un procedimiento, pero a los procedimientos se les llama solos no con asignación, por lo tanto la llamada es **INCORRECTA**. 
```text
c) SI tres(a) ENTONCES ...

```
La función `tres` devuelve un valor entero, pero la condición `SI` necesita un valor lógico, por lo tanto la llamada es **INCORRECTA**. 
```text
d) dos(a, b+3)

```
Tanto `a` como `b+3` son enteros, así que se corresponden con el tipo de variables definidas en la cabecera del procedimiento. No obstante, ambos parámetros se pasan por variable, por lo que el uso de `b+3` es **INCORRECTO**. 
```text
e) dos(a, tres(a))

```
El parámetro actual `a` está bien y se corresponde con el parámetro formal `x`. `tres(a)` es la llamada a una función que devuelve un entero, luego el tipo se corresponde con el parámetro formal `y` que también es un entero. Pero no se puede utilizar la llamada a una función cuando el parámetro se pasa por variable, por lo tanto, la llamada es **INCORRECTA**. 
```text
f) b <-- tres(dos(a,5))

```
Dentro de la función hay una llamada a un procedimiento, lo cual está mal. Por lo tanto, en este caso, la llamada es **INCORRECTA**. 
```text
g) si <-- uno(c, 5)

```
La función `uno` devuelve el un tipo lógico, que es asignado a la variable `si` que también es de tipo lógico. Además tanto `c` como 5 son enteros, tal y como se indica en los parámetros formales. Por todo esto la llamada es **CORRECTA**. 
```text
h) dos(tres(b), c)

```
Está mal porque en el primer parámetro actual es una llamada a una función y se debe corresponder con una sola variable, ya que el parámetro formal se pasa por variable. En este caso la llamada es **INCORRECTA**. 
```text
i) dos(4, c)

```
Es una llamada a un procedimiento, pero está mal porque el primer parámetro sólo se puede corresponder con una variable (ya que se pasa por variable) y no con un valor constante como en este caso, por lo tanto la llamada es **INCORRECTA**.