---
title: "Analisis de Seno entre 2 valores"
date: 2024-01-01
draft: false
languages: ['matlab']
categories: ['enunciado']
---

# Analisis de Seno entre 2 valores

##  Enunciado 

En matemáticas, la siguiente expresión es siempre verdadera: 
```text
seno(x)<=1

```
Diseñar un algoritmo para verificar esta propiedad en la (utilizando la función interna `sen`) para los valores de x que van de -10.0 hasta 10.0 en pasos de 0.2. 

##  Soluciones 

###  Pseudocódigo 
```text
 ALGORITMO seno
 ENTRADAS:
    (* No hay entradas *)
 SALIDAS:
    (* Un mensaje indicando si la condición seno(x)<=1 se cumple *)
 VARIABLES:
    X: REAL
    funcion: LÓGICO
 INICIO
    (* Encontrar algún caso en que no se cumpla la condición *)
    X <-- -10
    funcion <-- VERDADERO
    REPETIR
       SI sen(X)>1  ENTONCES
          funcion<--FALSO
       FIN_SI
       X <-- X+0.2
    HASTA (X>10) O (funcion=FALSO)
 
    (* Mostrar el resultado *)
    SI funcion=FALSO  ENTONCES
       ESCRIBIR "NO verifica la función"
    SI_NO
       ESCRIBIR "SI verifica la función"
    FIN_SI
 FIN

```
###  Solución en C
```c

#include <stdio.h>
#include <stdlib.h>
//Incluir math.h para utilizar la función seno: sin(x)
#include <math.h>  
 
#define VERDADERO 1
#define FALSO     0
 
int main(void){
  //ENTRADAS: (No hay entradas)
  //SALIDAS:  (Mensaje indicando si la condición sen(x)<=1 se cumple)
  //VARIABLES:
  float X;
  int funcion;
 
   //(Encontrar algún caso en que no se cumpla la condición)
   X=-10;
   funcion=VERDADERO;
   do{
      if(sin(X)>1){
         funcion=FALSO;
      }
      X=X+0.2;
   }while(! ((X>10)||(funcion==FALSO)) );
 
   //(Mostrar el resultado)
   if(funcion==FALSO){
      printf("NO verifica la funcion");
   }else{
      printf("SI verifica la funcion");
   }
}

```
###  Programa en Matlab 
```matlab

% Programa Confirmar_Seno
% Descripción: verificar la propiedad del seno.
% Entradas: ninguna.
% Salidas: mensaje de confirmación de que se cumple la propiedad.
% Variables:
%    x: REAL
%    funcion: LOGICO
 
%Comprobamos si se cumple la propiedad
funcion=false
for x=-10:0.2:10
    if sin(x)>1,
        funcion=true;
    end
end
 
%Mostramos un mensaje 
if funcion
    disp('No se cumple');
else
    disp('Se cumple');
end
```