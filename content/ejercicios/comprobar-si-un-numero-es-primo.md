---
title: "Comprobar si un número es primo"
date: 2024-01-01
draft: false
languages: ['c', 'matlab']
professors: ['angel']
categories: ['análisis', 'comentario', 'enunciado']
tags: ['Sin Pseudocódigo']
---

# Comprobar si un número es primo

## Enunciado

El siguiente programa comprueba si un número es primo o no. Recuerda que un número primo es aquél que puede dividirse únicamente por sí mismo y por la unidad. Una manera de decidir si un número es primo o no, es dividirlo por todos los números comprendidos entre el 1 y su raíz cuadrada. Si se encuentra que el número es divisible por alguno de ellos, se deduce que ese número no es primo. Vamos a utilizar el operador módulo o resto de la división entera (%) para comprobar si la división es exacta. Este operador da como resultado el resto de la división del primer operando por el segundo. Por ejemplo, 5%2 es 1, puesto que el resto de dividir 5 entre 2 es 1. Guarda el programa con el nombre primos.c.

## Soluciones

### Programa en C por **Angel**

Solución comentada al Ejercicio:

```c
 /* fichero primos.c */
 /* programa para determinar si un número es primo */
 #include <stdio.h>
 #include <math.h>
 void main(void) {
   int numero, divisor;
   printf("Que numero quieres saber si es primo?\n");
   scanf("%d", &numero);
   while(numero<2) {
      printf("Lo siento, no acepto numeros menores que 2.\n");
      printf("Intentalo de nuevo\n");
      scanf("%d", &numero);
   }
   for (divisor=2; divisor<=sqrt(numero); divisor++) {
      if (numero%divisor==0) {
         printf("%d no es primo.\n", numero);
         return;
      }
   }
   printf("%d es primo.\n", numero);
 }
```

#### Comentario

El comentario más apropiado para este ejercicio es el algoritmo para calcular el primo con el bucle for (divisor=2; divisor<=sqrt(numero); divisor++). Observa que este bucle se termina cuando se encuentra un divisor del número, en cuyo caso se escribe el mensaje de que el número no es primo y se termina la ejecución del programa con un return, o cuando divisor llega a su valor límite, en cuyo caso el número es primo porque no se ha encontrado ningún divisor.

### Programa en Matlab

#### Solución con programación básica

```matlab
%Programa NumeroPrimo
%Descripción: Comprueba si un número es primo o no.
%Entradas: valor a comprobar.
%Salidas: mensaje de "Es primo" o "No es primo".
%Variables:
%   num,div: ENTEROS
%   esprimo: LÓGICO
 
num=input('Introduzca un valor: ');
%Obtener el valor absoluto
if num<0
    num=-num;
end
%Comprobar el número introducido
switch num
    case 0
        disp('Se ha introducido un 0');
    case 1
        disp('Es primo');
    otherwise
        esprimo=true;
        for div=2:fix(sqrt(num))
            if rem(num,div)==0,
                esprimo=false;
            end
        end
        if esprimo==true
            disp('Es primo');
        else
            disp('No es primo');
        end
end
```

#### Solución con programación básica mejorada

Se sustituye el bucle **for** por uno de tipo **while** , para que el programa sea más rápido. 

```matlab
%Programa NumeroPrimo
%Descripción: Comprueba si un número es primo o no.
%Entradas: valor a comprobar.
%Salidas: mensaje de "Es primo" o "No es primo".
%Variables:
%   num,div,tope: ENTEROS
%   esprimo: LÓGICO
 
num=input('Introduzca un valor: ');
%Obtener el valor absoluto
if num<0
    num=-num;
end
%Comprobar el número introducido
switch num
    case 0
        disp('Se ha introducido un 0');
    case 1
        disp('Es primo');
    otherwise
        esprimo=true;
        div = 2;
        tope = fix(sqrt(num));
        while div<=tope && esprimo
            if rem(num,div)==0,
                esprimo=false;
            end
            div = div + 1;
        end
        if esprimo==true
            disp('Es primo');
        else
            disp('No es primo');
        end
end
```

#### Solución con programación Matlab avanzada 

```matlab
%Programa NumeroPrimo
%Descripción: Comprueba si un número es primo o no.
%Entradas: valor a comprobar.
%Salidas: mensaje de "Es primo" o "No es primo".
%Variables:
%   num,div: ENTEROS
%   esprimo: LÓGICO
 
num=input('Introduzca un valor: ');
%Obtener el valor absoluto
num = abs(num)
%Comprobar el número introducido
switch num
    case 0
        disp('Se ha introducido un 0');
    case 1
        disp('Es primo');
    otherwise
        esprimo = sum(rem(num,2:num-1)==0)==0
        if esprimo
            disp('Es primo');
        else
            disp('No es primo');
        end
end
```

##### Comentario

Para esta solución se han utilizado las siguientes funciones de Matlab:

* **abs** : devuelve el valor absoluto de un número.
* **rem** : devuelve el resto de dividir un número entre otro. En este ejemplo, se divide un número entre varios existentes en un array. La solución obtenida es un array con los restos.
* **sum** : devuelve la suma de todos los elementos de un array.
