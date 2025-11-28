---
title: "Calculo de números primos"
date: 2024-01-01
draft: false
languages: ['c', 'matlab', 'pseudocódigo']
professors: ['angel']
categories: ['enunciado', 'comentario', 'análisis']
---


# Calculo de números primos

  

##  Enunciado 

Basándote en el ejercicio [Comprobar si un número es primo](/ejercicios/comprobar-si-un-número-es-primo/), realiza un programa que imprima todos los números primos comprendidos entre el 2 y un valor límite que se preguntará al ejecutar el programa. 

##  Soluciones 

###  Programa en C por **Angel**

Solución comentada del Ejercicio: 
```c


 /* fichero primos1.c */
 #include <stdio.h>
 void main(void) {
   int numero, divisor;
   int n;
   printf("¿Hasta qué número desea conocer los primos?\n");
   printf("Introduzca el valor: ");
   scanf("%d", &n);
   for (numero=2; numero<=n; numero++) {
      esPrimo=1; /* numero es primo */
      for (divisor=2; divisor<=sqrt(numero); divisor++){
         if (numero%divisor==0){
            esPrimo=0;
            break;
         }
      }
      if(esPrimo==1) printf("%d\n", numero);
   }
 }

```
####  Comentario 

Para poder escribir todos los números primos hasta un límite, basta introducir un nuevo bucle for al programa anterior que vaya recorriendo todos los números enteros desde el 2 hasta dicho límite inclusive. En cada ejecución del bucle se comprueba si el número considerado es primo aprovechando las sentencias del programa anterior. En este caso se calcula si un número es primo mediante el bucle for (divisor=2; divisor<=sqrt(numero); divisor++). Observa que se ha definido una variable esPrimo que indica si el número es primo o no. Al principio se supone que el número es primo, y esta condición se cambia si se encuentra un divisor exacto. En esta caso, la sentencia break hace que se termine el bucle for más interno. 

###  Solucion en Pseudocódigo
```text


 ALGORITMO primos1
 ENTRADAS:
    n: ENTERO (* Valor límite *)
 SALIDAS:
    numero: ENTERO
 VARIABLES
    divisor: ENTERO
 INICIO
 
   ESCRIBIR "¿Hasta qué número desea conocer los primos?"
   ESCRIBIR SaltoDeLinea
   ESCRIBIR "Introduzca el valor: "
   LEER n
   PARA numero<--2 HASTA n HACER
      esPrimo<--1 (* numero es primo *)
      divisor<--2
      MIENTRAS divisor<=RAIZ(numero) Y esPrimo=1 HACER
        SI (numero MOD divisor) = 0 ENTONCES
           esPrimo<--0;
        FIN_SI
      FIN_MIENTRAS
      SI esPrimo=1 ENTONCES
          ESCRIBIR numero
          ESCRIBIR SaltoDeLinea
      FIN_SI
   FIN_PARA 
 FIN

```
####  Comentario 

En la creación del pseudocódigo a partir del código en C mostrado en el apartado anterior hemos realizado algunas sustituciones para que el pseudocódigo fuera correcto. El bucle `for` más interno ha sido sustituido por una sentecia `MIENTRAS`, ya que en el código C dicho bucle estaba siendo utilizado como una sentencia `MIENTRAS`. Además en el diseño en pseudocódigo no es recomendable incluir sentencias de ruptura de flujo como `break`, por lo que se ha simulado su comportamiento incluyendo en la condición del `MIENTRAS` la comparación `esPrimo=1`. Por último, se ha utilizado la función ficticia `RAIZ(numero)` como si ya estubiera declarada anteriormente. 

###  Programa en Matlab 
```matlab


%Programa Primos1
%Descripción: Nos localiza los números primos entre el 2 y el número que queramos.
%Entradas: El valor límite hasta el que queremos analizar.
%Salidas: Los números primos.
%Variables:
%   n, numero, divisor: ENTEROS;
 
n=input('Introduzca hasta que número desea buscar: ');
disp('Primos contenidos:');
for numero=2:n,
    divisor=2;
    while rem(numero,divisor)~=0,
        divisor = divisor + 1;
    end
    if numero==divisor,
        disp(numero);
    end
end
```