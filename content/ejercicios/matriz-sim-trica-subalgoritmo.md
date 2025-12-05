---
title: "Matriz Simétrica Subalgoritmo"
date: 2024-01-01
draft: false
languages: ['pseudocódigo']
professors: ['lperez']
categories: ['enunciado']
tags: ['sin_matlab']
---

# Matriz Simétrica Subalgoritmo

##  Enunciado 

Diseñar un subalgoritmo que dada una matriz cuadrada y su tamaño nos diga si es o no simétrica. 

Ejemplo de matriz simétrica: 

1 |  4 |  7   
---|---|---  
4 |  2 |  9   
7 |  9 |  3   

##  Soluciones 

###  Diseño en Pseudocódigo 

####  Diseño 1 en Pseudocódigo por **lperez**
```text
FUNCION Calculo_simetrica(A, tam): LOGICO
ENTRADAS: A: ARRAY [1..tam, 1..tam] DE ENTEROS; matriz matemática 
                            cuadrada.
        tam: ENTERO, nº de filas y  columnas de A, tam>0. 
SALIDAS: VERDAD la matriz A es simétrica y FALSO si no lo es.
VARIABLES: i, j: ENTERO; p:LOGICO
INICIO
   p<--VERDAD
   PARA   i=1  HASTA  tam HACER
      PARA   j=1  HASTA  tam  HACER
         SI  A(i,j)<>A(j,i)
         ENTONCES p<--FALSO
         FIN_SI
      FIN_PARA
   FIN_PARA
   DEVOLVER p
FIN
```

####  Diseño 2 en Pseudocódigo por **lperez**
```text
FUNCION Calculo_simetria(A, tam): LOGICO
ENTRADAS: A: ARRAY [1..tam, 1..tam] DE ENTEROS; matriz matemática 
                            cuadrada.
        tam: ENTERO, nº de filas y  columnas de A, tam>0. 
SALIDAS: VERDAD la matriz A es simétrica y FALSO si no lo es.
VARIABLES: i, j: ENTERO; p:LOGICO
INICIO
  p<--VERDAD
  PARA   i=1  HASTA  tam HACER
     PARA j=i+1  HASTA  tam  HACER
        SI  A(i,j)<>A(j,i)
        ENTONCES p<--FALSO
        FIN_SI
     FIN_PARA
  FIN_PARA
  DEVOLVER p
FIN
```

####  Diseño 3 en Pseudocódigo por **lperez**
```text
FUNCION Calculo_simetria(A, tam): LOGICO
ENTRADAS: A: ARRAY [1..tam, 1..tam] DE ENTEROS; matriz matemática 
                            cuadrada.
        tam: ENTERO, nº de filas y  columnas de A, tam>0. 
SALIDAS: VERDAD la matriz A es simétrica y FALSO si no lo es.
VARIABLES: i, j: ENTERO; p:LOGICO
INICIO
  p<--VERDAD
  i<--1 
  MIENTRAS (i<= tam) AND (p) HACER
     j<--i+1
     MIENTRAS  (j<=tam ) AND (p)  HACER
        SI  A(i,j)<>A(j,i)
        ENTONCES p<--FALSO
        FIN_SI
     FIN_PARA
  FIN_PARA
  DEVOLVER p
FIN
```

####  Diseño 4 en Pseudocódigo por **lperez**
```text
PROCEDIMIENTO Calculo_simetria(A, tam, VAR simetria
ENTRADAS: A: ARRAY [1..tam, 1..tam] DE ENTEROS; matriz matemática 
                            cuadrada.
        tam: ENTERO, nº de filas y  columnas de A, tam>0. 
SALIDAS: simetria:LOGICO, VERDAD la matriz A es simétrica y FALSO si no lo es.
VARIABLES: i, j: ENTERO; 
INICIO
  simetria<--VERDAD
  i<--1 
  MIENTRAS (i<= tam) AND (p) HACER
     j<--i+1
     MIENTRAS  (j<=tam ) AND (p)  HACER
        SI  A(i,j)<>A(j,i)
        ENTONCES simetria<--FALSO
        FIN_SI
     FIN_PARA
  FIN_PARA
FIN
```

####  Comentario

En la primera solución se examinan todos los elementos de la matriz, de forma que comparará dos veces algunos elementos. 

En la segunda solución no compara dos veces los mismos elementos ya que se recorre los elementos que están por encima de la diagonal y compara a cada uno con su simétrico. 

Tanto en uno como en otro de los anteriores, si se encontrara un elemento que no cumple la simetría el subalgoritmo no terminaría sino que seguiría con las comparaciones hasta que el ciclo acabase (ya que se trata de ciclos PARA). 

En la tercer solución se recorre los elementos sobre la diagonal principal, igual que en la segunda solución, pero hace que el subalgoritmo acabe en el momento que encuentra dos elementos que no cumplen con la simetría. 

La cuarta solución es análoga a la tercera pero realizado con un procedimiento en lugar de con una función. 

###  Programa en C

####  Solución 1 en C
```c

//CONSTANTES: 
#define VERDAD 1
#define FALSO  0
              
int Calculo_simetrica(int A[1000][1000],int tam){
  //ENTRADAS:
     //_A: matriz matemática cuadrada_
     //_tam: numero de filas y de columnas de la matriz; tam >0_
  //SALIDAS:
     //_VERDAD (1) si la matriz A es simetrica y FALSO (0) si no lo es_
  //VARIABLES
  int i,j;
  int p;
               
  p=VERDAD;
  for(i=1; i<=tam; i++){
      for(j=1; j<=tam; j++){
           if(A[i][j]!=A[j][i]){
                p=FALSO;
           }
      }
   }
   return(p);
}
```

####  Solución 2 en C
```text
//CONSTANTES: 
#define VERDAD 1
#define FALSO  0
              
int Calculo_simetrica(int A[1000][1000],int tam){
  //ENTRADAS:
     //_A: matriz matemática cuadrada_
     //_tam: numero de filas y de columnas de la matriz; tam >0_
  //SALIDAS:
     //_VERDAD (1) si la matriz A es simetrica y FALSO (0) si no lo es_
  //VARIABLES
  int i,j;
  int p;
               
  p=VERDAD;
  for(i=1; i<=tam; i++){
      for(j=i+1; j<=tam; j++){
           if(A[i][j]!=A[j][i]){
                p=FALSO;
           }
      }
   }
   return(p);
}
```

####  Solución 3 en C
```text
//CONSTANTES: 
#define VERDAD 1
#define FALSO  0
              
int Calculo_simetrica(int A[1000][1000],int tam){
  //ENTRADAS:
     //_A: matriz matemática cuadrada_
     //_tam: numero de filas y de columnas de la matriz; tam >0_
  //SALIDAS:
     //_VERDAD (1) si la matriz A es simetrica y FALSO (0) si no lo es_
  //VARIABLES
  int i,j;
  int p;
               
  p=VERDAD;
  i=1;
  while((i<=tam)&&(p)){
     j=i+1;
     while((j<=tam)&&(p)){
        if(A[i][j]!=A[j][i]){
            p=FALSO;
        }
     }
  }
  return(p);
}
```

####  Solución 4 en C
```text
//CONSTANTES: 
#define VERDAD 1
#define FALSO  0
              
void Calculo_simetrica(int A[1000][1000],int tam, int &simetrica){
  //ENTRADAS:
     //_A: matriz matemática cuadrada_
     //_tam: numero de filas y de columnas de la matriz; tam >0_
  //SALIDAS:
     //simatrica: _VERDAD (1) si la matriz A es simetrica y FALSO (0) si no lo es_
  //VARIABLES
  int i, j;
            
  simetrica=VERDAD;
  i=1;
  while((i<=tam)&&(p)){
    j=i+1;
    while((j<=tam)&&(p)){
       if(A[i][j]1=A[j][i]){
              simetrica=FALSO;
       }
    }
  }
}
```