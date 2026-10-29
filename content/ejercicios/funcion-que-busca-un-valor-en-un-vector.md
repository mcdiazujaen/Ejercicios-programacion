---
title: "Funcion que busca un valor en un vector"
date: 2024-01-01
draft: false
languages: ['c', 'pseudocódigo']
categories: ['enunciado']
tags: ['Sin Matlab']
---

# Funcion que busca un valor en un vector

##  Enunciado 

Diseñar una función que tenga como entradas un vector, su tamaño y un valor que debe buscarse en ese vector. La función debe devolver **verdadero** si el valor se encuentra en el vector, y un **falso** si la búsqueda es infructuosa. Ni el vector ni el valor deben ser alterados. 

##  Soluciones 

###  Diseño en Pseudocódigo 
```text
 FUNCION  Buscar(v:ARRAY(1..1000) DE REAL; n:ENTERO; x:REAL): LÓGICO
 ENTRADAS:
    v: ARRAY(1..1000) DE REAL  ''(*Vector donde se realiza la búsqueda*)''
    n: ENTERO                  ''(*Número de elementos del vector*)''
    x: REAL                    ''(*Valor que queremos buscar dentro del vector*)''
 SALIDAS:
    enc: LOGICO    ''(*VERDADERO si el valor de x está en el array, y FALSO en caso contrario*)'' 
 VARIABLES:
    i:ENTERO
 INICIO
    ''(*Recorrer el array hasta encontrar el valor o llegar al final*)''
    i <-- 1
    MIENTRAS x<>v(i) Y i<=n   HACER
       i <-- i+1
    FIN_MIENTRAS
 
    ''(*Comprobar si se ha encontrado el valor*)''
    SI v(i)=x  ENTONCES
       enc <-- VERDADERO
    SI_NO
       enc <-- FALSO
    FIN_SI
 
    ''(*Devolver el resultado*)''
    DEVOLVER (enc)
 FIN
```

###  Programa en C 
```c

 #include <stdio.h>
 #include <stdlib.h>
 
 int Buscar(float v[1001], int n, float x){
    /*------
    ENTRADAS:
       v: Vector donde se realiza la búsqueda
       n: Números de elementos del vector
       x: Valor que queremos buscar dentro del vector
    --------*/
    //SALIDAS:
    bool enc;  //VERDADERO  si el valor x está en el array, y FALSO en caso contrario
    //VARIABLES: 
    int i;
 
    /*Recorrer el array hasta encontrar el valor o llegar al final.*/
    i=1;
    while (x!=v[i] && i<=n){
       i=i+1;
    }
 
    /*Comprobar si se ha encontrado el valor*/
    if (v[i]==x){
       enc=true;
    }else{
       enc=false;
    }
 
    /*Devolver el resultado*/
    return( enc );
}
```