---
title: "Evaluar condiciones"
date: 2024-01-01
draft: false
languages: ['pseudocódigo']
categories: ['enunciado']
---

# Evaluar condiciones

##  Enunciado 

Suponed que I y J son variables enteras cuyos valores son 6 y 12 respectivamente. ¿Cuáles de las siguientes condiciones son verdaderas? 
```text
a) 2*I <= J
b) 2*I-1 < J
c) I>0 AND I<=10
d) I>25 OR (I<50 AND J<50)
e) I<4 OR J>5
f) NOT I>6
```

##  Soluciones 

a) Como nos dice que el valor obtenido tiene que ser menor o igual que el valor de J, en este caso la condición es VERDADERA, porque 12=12. Demostración: 
```text
 2 * I <= J
 2 * 6 <= 12
   12  <= 12   (**VERDADERO**) 
```

b) 2*6-1=11,como nos dice que el valor obtenido en la operación tiene que ser estrictamente menor que el valor de J, aquí la condición es VERDADERA,porque 11<12\. Demostración: 
```text
2 * I - 1 < J
2 * 6 - 1 < 12
  12  - 1 < 12
     11   < 12  (**VERDADERO**)
```

c) Tenemos dos condiciones unidas por la unión AND, como se cumple que 6>0 y también que 6<10, la condición es VERDADERA, por la unión de dos condiciones verdaderas. Demostración: 
```text
I > 0  AND  I <= 10
6 > 0  AND  6 <= 10
Verdad AND  Verdad   (**VERDADERO**)
```

d) Primero miramos la condición indicada entre paréntesis: 6<50 es verdadera y 12<50 es falsa, por lo tanto, la condición entre paréntesis es falsa. Después evaluamos la primera condición: I>25 es falsa ya que 6<25, por lo tanto tenemos Falso OR Falso. Según la condición que las une (OR) el resultado es FALSO. Demostración: 
```text
I > 25  OR  ( I < 50  AND  J < 50 )
6 > 25  OR  ( 6 < 50  AND 12 < 50 )
Falso   OR  ( Verdad  AND  Falso  )
Falso   OR           Falso               (**FALSO**)
```

e) En este caso tenemos que la primera condicón es falsa porque 6 no es menor que 4 y la segunda condición es verdadera porque 12 si es mayor que 5. La condición final sería Falso OR Verdad, por lo tanto, la condición es VERDADERA. Demostración: 
```text
I < 4  OR   J > 5
6 < 4  OR  12 > 5
Falso  OR  Verdad  (**VERDADERO**)
```

f) La condición 6>6 es falsa (sería válida si fuese `I**> =**6`). En consecuencia, tenemos una condición falsa negada (NOT Falso). Por lo tanto, la condición es VERDADERA. Demostración: 
```text
NOT I > 6
NOT 6 > 6
NOT Falso    (**VERDADERO**)
```