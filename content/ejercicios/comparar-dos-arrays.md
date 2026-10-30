---
title: "Comparar dos arrays"
date: 2024-01-01
draft: false
languages: ['c', 'matlab', 'pseudocódigo']
categories: ['enunciado']
---

# Comparar dos arrays

## Enunciado

Diseñar un subalgoritmo que devuelva **VERDAD** si los dos arrays dados como entrada son iguales y **FALSO** , en otro caso. 

## Soluciones

### Diseño en pseudocódigo

```text
 FUNCION IGUALES(VAR V:ARRAY DE REALES; VAR W:ARRAY DE REALES; n,m:ENTEROS):LOGICO
 
 ENTRADAS:
   V: ARRAY DE REALES  (*Primer array que vamos a comparar*)
   W: ARRAY DE REALES  (*Segundo array que se quiere comparar*)
   n: ENTERO           (*Tamaño del array V*)
   m: ENTERO           (*Tamaño del array W*)
 SALIDAS:
   igual: LOGICO       (*VERDAD si los array V y W son iguales, FALSO en caso contrario*)
 VARIABLES:
   i: ENTERO
 
 INICIO
   igual <-- VERDAD
   SI (n=m) ENTONCES
     i <-- 1
     MIENTRAS ((i<=n) Y (igual)) HACER
       SI (V(i)<>W(i)) ENTONCES
         igual <-- FALSO
       FIN SI
       i<--i+1
     FIN MIENTRAS
   SI_NO
     igual<-FALSO
   FIN SI
   DEVOLVER igual
 FIN
```

### Solucion en C

```text
  int IGUALES(float V[],float W[], int n, int m){
  /*ENTRADAS:
    V: Primer array que vamos a comparar (el primer valor está en la posición 1)
    W: Segundo array que se quiere comparar (el primer valor está en la posición 1)
    n: Tamaño del array V
    m: Tamaño del array W
  */
  //SALIDAS
    int igual; //VERDAD si los dos arrays V y W so iguales, FALSO en caso contrario
  //VARIABLES
    int i;
 
    igual=1;
    if(n==m){
        i=1;
        while( (i<=n) && (igual) ){
           if(V[i]!=W[i]){
             igual=0;
           }
           i=i+1;
        }
    }else{
        igual=0;
    }
    return(igual);
 }
```

### Programa en Matlab

#### Solución con programación clásica

```matlab
function igual=iguales(v,w)
%FUNCIÓN igual=iguales(v,w)
%DESCRIPCIÓN: Diseñar un subalgoritmo que devuelva VERDAD si los arrays 'v' y 'w' son iguales y FALSO, en otro caso.
%ENTRADAS:
%   v, w: ARRAYS DE REALES; arrays que se van a comparar
%SALIDAS:
%   igual: LÓGICO; Verdadero si los array son iguales y falso en caso contrario.
%VARIABLES:
%   pos:ENTERO
 
    if length(v)==length(w),
        igual=true;
        pos=1;
        while (pos<=length(v))&&(igual==true)
            if v(pos)~=w(pos)
                igual=false;
            end
            pos=pos+1;
        end
    else
        igual=false;
    end
```

#### Solución Matlab

```matlab
function igual=iguales(v,w)
%FUNCIÓN igual=iguales(v,w)
%DESCRIPCIÓN: Diseñar un subalgoritmo que devuelva VERDAD si los arrays 'v' y 'w' son iguales y FALSO, en otro caso.
%ENTRADAS:
%   v, w: ARRAYS DE REALES; arrays que se van a comparar
%SALIDAS:
%   igual: LÓGICO; Verdadero si los array son iguales y falso en caso contrario.
%VARIABLES:
%   pos:ENTERO
 
    igual=false;
    if length(v)==length(w)
        if v==w
            igual=true;
        end
    end
```
