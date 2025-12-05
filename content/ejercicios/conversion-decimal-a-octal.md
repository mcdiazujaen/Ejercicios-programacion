---
title: "Conversion decimal a octal"
date: 2024-01-01
draft: false
languages: ['c', 'pseudocódigo']
categories: ['enunciado']
tags: ['sin_matlab']
---

# Conversion decimal a octal

##  Enunciado 

Formular un algoritmo para convertir números enteros decimales en base 10 a sus respectivas representaciones octales en base 8, por medio de sucesivas divisiones. Por ejemplo, para calcular la representación octal de 150, se divide sucesivamente por 8 y los restos que van quedando se almacenan ordenadamente. 

Paso |  Dividendo |  Divisor |  Cociente |  Resto   
---|---|---|---|---  
1 |  150 |  8 |  18 |  **6**  
2 |  18 |  8 |  2 |  **2**  
3 |  2 |  8 |  0 |  **2**  
  
226(8 = 2*82+2*81+6*80=150(10

Generalizar y que haga un cambio de base como dato la base a la que se quiera pasar. mostrar los dígitos en orden inverso. 

##  Soluciones 

###  Diseño en Pseudocódigo 
```text
 PROGRAMA CambioDeBase
 ENTRADAS:
    numero: ENTERO  ''(*Número en formato decimal que se desea cambiar de base*)''
 SALIDAS:
    resul: ARRAY (0..100) DE ENTEROS  ''(*Array que almacenará el resultado en orden inverso*)''
    digitos: ENTERO                   ''(*Número de elementos del array, es decir, número de dígitos en la nueva base*)''
 VARIABLES
    dividendo: ENTERO
    resto: ENTERO
    cociente:ENTERO
    i: ENTERO
 INICIO
    ''(*Leer las entradas necesarias para el cambio de base*)''
    ESCRIBIR "Introduzca un número en formato decimal: "
    LEER numero
 
    ''(*Realizar el cambio de base*)''
    digitos <-- 0
    dividendo <-- numero
    MIENTRAS dividendo > 0 HACER
       cociente <-- dividendo DIV 8  ''(*Se realiza una división entera*)''
       resto <-- dividendo MOD 8 
       resul(digitos) <-- resto
       digitos <-- digitos + 1
       dividendo <-- cociente
    FIN_MIENTRAS
 
    ''(*Mostrar el resultado almacenado en el array en orden inverso*)''
    ESCRIBIR "El numero decimal ", numero, " equivale en base 8 a: "
    PARA i <-- digitos-1 HASTA 0 CON INCREMENTO DE -1 HACER
       ESCRIBIR resul(i)
    FIN_PARA
 FIN

```
###  Programa en C
```c

 #include <stdlib.h>
 
 int main(void){
    //ENTRADAS:
    int numero;     //Número en formato decimal que se desea cambiar de base
    //SALIDAS:
    int resul[101]; //Array que almacenará el resultado en orden inverso
    int digitos;    //Número de elementos del array, es decir, número de dígitos en la nueva base
    //VARIABLES
    int dividendo;
    int resto;
    int cociente;
    int i;
 
    //Leer las entradas necesarias para el cambio de base
    printf("Introduzca un número en formato decimal: ");
    scanf("%i", numero);
 
    //Realizar el cambio de base
    digitos = 0;
    dividendo = numero;
    while( dividendo > 0 ){
       cociente = dividendo/8;  //Se realiza una división entera porque ambos operandos son enteros
       resto    = dividendo%8;
       resul[digitos] = resto;
       digitos = digitos + 1;
       dividendo = cociente;
    }
 
    //Mostrar el resultado almacenado en el array en orden inverso
    printf("El numero decimal %i equivale en base 8 a: ", numero);
    for( i=digitos-1; i>=0; i--){
       printf("%i",resul[i]);
    }
    printf("\n");
 }
```