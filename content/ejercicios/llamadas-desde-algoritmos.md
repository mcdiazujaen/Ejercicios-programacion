---
title: "Llamadas desde algoritmos"
date: 2024-01-01
draft: false
languages: ['pseudocódigo']
categories: ['enunciado']
---

# Llamadas desde algoritmos

##  Enunciado 

Dadas las siguientes declaraciones en un algoritmo: 
```text
i, j, k : ENTERO
c : LÓGICO
a : ARRAY [1...10] DE ENTEROS
```

y las siguientes declaraciones de subalgoritmos: 
```text
FUNCIÓN Primera( x: ENTERO, a:ENTERO ): ENTERO
FUNCIÓN Segunda( y: LOGICO, VAR h: ENTERO ): LÓGICO
PROCEDIMIENTO Tercero( c: LÓGICO, VAR y: LÓGICO, a: ENTERO )
```

Di si las siguientes llamadas desde el algoritmo son correctas o no. Justifica la respuesta dada. 
```text
MIENTRAS Segunda(c, k) HACER ...
SI Segunda (VERDAD, 5) ENTONCES ...
Segunda (FALSO, j)
Tercero(c, Segunda(FALSO, k), Primera(5,a(4)))
SI Primera(i,4) > 5 ENTONCES ...
C <-- Segunda(Segunda(VERDAD, k), Primera(i, j))
SI Segunda(c,a(2)) O c ENTONCES ...
Tercero(FALSO, VERDAD, j)
SI j > k ENTONCES Primera(4,5)
ESCRIBIR Segunda(c, k)
```

##  Soluciones 

###  Pseudocódigo 
```text
MIENTRAS Segunda(c, k) HACER ...

 **Correcta** : El valor devuelto por la función es un lógico, necesario para la condición del `MIENTRAS`. El número de parámetros formales y actuales es el mismo, son del mismo tipo y están en el mismo orden. El segundo parámetro formal está pasado por variable (`VAR h:ENTERO`) y el segundo parámetro actual es un variable (`k`). 

SI Segunda(VERDAD, 5) ENTONCES ...

 **Incorrecta** : El segundo parámetro formal está pasado por variable (`VAR h:ENTERO`), sin embargo, el segundo parámetro actual es un valor constante (`5`). 

Segunda(FALSO, j)

 **Incorrecta** : El valor lógico devuelto por la función no es utilizado. 

Tercero(c, Segunda(FALSO, k), Primera(5,a(4)))

 **Incorrecta** : El segundo parámetro formal del procedimiento `Tercero` está pasado por variable (`VAR y:LÓGICO`), sin embargo, el parámetro actual correspondiente es el valor devuelto por una función (`Segunda(FALSO, k)`) en lugar de una variable. 

SI Primera(i, 4) > 5 ENTONCES ...

 **Correcta** : El valor devuelto por la función `Primera` es un entero y es comparado con el valor constante `5`, por lo tanto, tenemos una expresión lógica necesaria para la condición del `SI`. El número de parámetros formales y actuales es el mismo, son del mismo tipo y están en el mismo orden. 

C <-- Segunda(Segunda(VERDAD, k), Primera(i, j))

 **Incorrecta** : El segundo parámetro formal de la función `Segunda` está pasado por variable (`VAR h:ENTERO`), sin embargo, el parámetro actual correspondiente en la primera llamada es el valor devuelto por una función (`Primera(i, j)`) en lugar de una variable. 

SI Segunda(c, a(2)) O c ENTONCES ...

 **Correcta** : El valor devuelto por la función `Segunda` es lógico que junto con la expresión`O c` forman una expresión lógica, necesaria para la condición del `SI`. El número de parámetros formales y actuales de la función es el mismo, son del mismo tipo y están en el mismo orden. El segundo parámetro de la función `Segunda` se pasa por variables y como parámetro actual se utiliza un elemento de un vector (`a(2)`), lo cual es correcto. 

Tercero(FALSO, VERDAD, j)

 **Incorrecta** : El segundo parámetro formal del procedimiento `Tercero` está pasado por variable (`VAR y:LÓGICO`), sin embargo, el parámetro actual correspondiente es un valor constante (`VERDAD`) en lugar de una variable. 

SI j > k ENTONCES Primera(4,5)

 **Incorrecta** : El valor entero devuelto por la función `Primera` no es utilizado. 

ESCRIBIR Segunda(c, k)

 **Incorrecta** : El valor devuelto por la función `Segunda` es lógico y la orden ESCRIBIR no puede mostrar el valor de un lógico.
```