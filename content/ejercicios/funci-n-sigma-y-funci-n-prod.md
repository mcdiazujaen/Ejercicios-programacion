---
title: "Función SIGMA y función PROD"
date: 2024-01-01
draft: false
languages: ['pseudocódigo']
categories: ['enunciado']
tags: ['sin_matlab']
---

# Función SIGMA y función PROD

##  Enunciados 

###  Función SIGMA 

Diseñar una función SIGMA para calcular la suma de los _n_ elementos de un vector X (X y n son los parámetros de la función). 

###  Función PROD 

Diseñar la función PROD para calcular el producto de los _n_ elementos de un vector X (de nuevo X y n son los parámetros de la función). 

##  Soluciones 

###  Diseño en pseudocódigo 

####  Función SIGMA 
```text
 FUNCION SIGMA (VAR X: ARRAY DE REALES; n: ENTERO): REAL
 ENTRADAS:
   X: ARRAY DE REALES  _(Elementos que se van a sumar, la primera posición del array es 0)_
   n: ENTERO           _(Número de elementos que se van a sumar)_
 SALIDA:
   suma: REAL
 VARIABLES: 
   i: ENTERO
 INICIO
   suma <-- 0
   PARA i <-- 0  HASTA n CON INCREMENTO DE 1 HACER
     suma <-- suma + X(i)
   FIN PARA
   DEVOLVER (suma)
 FIN
```

####  Función PROD 
```text
 FUNCION PROD (VAR X: ARRAY DE REALES; n: ENTERO): REAL
 ENTRADAS: (Están definidas en la cabecera de la función)
   X: ARRAY DE REALES  _(Elementos que se van a multiplicar, la primera posición del array es 0)_
   n: ENTERO           _(Número de elementos que se van a multiplicar)_
 SALIDA:
   producto: REAL
 VARIABLES:
   i: ENTERO
 INICIO
   producto <-- 1
   PARA i <-- 1 HASTA n CON INCREMENTO DE 1 HACER
     producto <-- producto * X(i)
   FIN PARA
   DEVOLVER(producto)
 FIN
```

###  Programa en C

####  Función SIGMA
```c

float SIGMA(float X[], int n){
/*ENTRADAS:
  _float X[] -- > (Elementos que se van a sumar, la primera posición del array es 0)_
  _int n ------ > (Número de elementos que se van a sumar)_
*/
//SALIDAS
  float suma;
//VARIABLES
  int i;
  
  suma=0;
  for(i=0; i<=n; i++){
      suma=suma+X[i];
  }
  return(suma);
}
```

####  Función PROD
```text
 float PROD(float X[], int n){
 /*ENTRADAS:
  _float X[] -- > (es un array de reales,cuya primera posicion es 0)_
  _int n ------ > (número de elementos que se van a multiplicar)_
 */
 //SALIDAS:
   float producto;
 //VARIABLES:
   int i;
             
   producto=1;
   for(i=1; i<=n; i++){
     producto=producto*X[i];
   }
   return(producto);
}
```

####  Comentario

Las sección `ENTRADAS` de ambas funciones está totalmente comentada, ya que en C no se puede repetir la declaración de los parámetros (`X, n`) dentro de la función.