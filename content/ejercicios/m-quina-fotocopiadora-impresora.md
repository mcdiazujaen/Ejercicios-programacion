---
title: "Máquina fotocopiadora-impresora"
date: 2024-01-01
draft: false
categories: ['enunciado']
tags: ['sin_matlab', 'sin_solución']
---

# Máquina fotocopiadora-impresora

##  Enunciado 

Tenemos que controlar una máquina de fotocopiadora-impresora. Esta máquina tiene 3 modos: 

  * _Modo 1_ : actúa de fotocopiadora, 
  * _Modo 2_ : impresora 
  * _Modo 3_ : escáner. 

La maquina conforme le van llegando trabajos los va sirviendo, siguiendo una priorización. Cuando se le envían trabajos a la maquina, esta dispone de una matriz en memoria, llamada trabajos donde se almacena el identificador de trabajo (Columna 1) y el número de páginas (Columna 2), el modo en que va a trabajar (Columna 3) y el orden en el que se van a servir los trabajos (Columna 4). Un ejemplo de cómo podría ser esta matriz con 6 trabajos se muestra a continuación: 

ID |  Num |  Modo |  Prioridad   
---|---|---|---  
6 |  15 |  1 |  1   
7 |  55 |  2 |  6   
8 |  2 |  1 |  2   
9 |  5 |  3 |  4   
10 |  1 |  3 |  5   
11 |  2 |  1 |  3   
  
El ID del trabajo, es incremental, según vayan llegando trabajos, se le va poniendo un número. El número de copias y el modo se le da al sistema como entrada cada vez que llega un trabajo. La prioridad de los trabajos habrá que calcularla cada vez que llegue un trabajo nuevo al sistema o se elimine un trabajo del sistema. Así pues, en el ejercicio se pide: 

###  Apartado 1 

Realizar un subalgoritmo que dado como entrada un modo de la fotocopiadora (valor: 1,2 o 3), la matriz de trabajos, y el tamaño de la matriz, se muestre por pantalla la lista de trabajos ordenada por ID que hay pendientes de realizar en este modo. Pista: La matriz ya está ordenada por ID. 

_Ejemplo_ : Entrada: Modo: 1 Salida: 
```text
  Trabajo 6
  Trabajo 8
  Trabajo 11
```

###  Apartado 2 

Realizar un subalgoritmo que dado como entrada la matriz y su tamaño devuelva la posición de la matriz (o sea el número de fila) del próximo trabajo a realizar. Si no se encuentra ningún trabajo entonces el subalgoritmo devolverá un -1. Pista: El próximo trabajo a realizar es aquel que tenga el valor 1 en la columna de prioridades (Columna 4). 

_Ejemplo_ : En la matriz anterior, devolvería la posición: 1 

###  Apartado 3 

Realizar un subalgoritmo que dado como entrada un modo (o sea un valor: 1, 2 o 3) y un número de copias a realizar devuelva si es aceptable o no un trabajo, si lo es devolverá verdadero, y sino devolverá falso. Se considera aceptable cuando el número de copias no supera 20 en modo escáner o fotocopiadora. En modo impresora no tiene límite. 

_Ejemplo_ : Entrada: Modo: 1, 10 copias. Devuelve Verdadero 

###  Apartado 4 

Realizar un subalgoritmo que actualice las prioridades del sistema. Para ello se da como entrada la matriz de trabajos y su tamaño. El algoritmo comenzará a dar prioridades a los trabajos con el identificador más bajo pero en el siguiente orden: primero estarán los que sean de fotocopiadora (Modo 1), después los del escáner (Modo 3) y por último los de impresora (Modo 2). Pista: los trabajos ya están ordenados por orden de llegada y por tanto los identificadores más bajos están en las primeras posiciones. 

_Ejemplo_ : 

ID |  Num |  Modo |  Prioridad   
---|---|---|---  
6 |  15 |  1 |  1   
7 |  55 |  2 |  6   
8 |  2 |  1 |  2   
9 |  5 |  3 |  4   
10 |  1 |  3 |  5   
11 |  2 |  1 |  3   

###  Apartado 5 

Realizar un subalgoritmo que de alta un trabajo nuevo. Para hacer esto, se tendrá que pasar como entrada la matriz, el tamaño, el modo en el que se va a trabajar, el número de copias que se quiere realizar y el último identificador de trabajo usado. Una vez hecho esto, se comprueba si el número de copias es correcto usando el subalgoritmo del apartado 3). Si lo es entonces, se añade en la matriz una fila nueva con: el nuevo identificador de trabajo actualizado, es decir, sería el último identificador más 1, el número de copias y el modo. Por último se llama al subalgoritmo 4) para actualizar la lista de prioridades. 

_Ejemplo_ : Entrada: Modo: 1, Nº copias: 10, Ultimo ID trabajo: 11. 

Primero se Inserta la fila, si es posible 

ID |  Num |  Modo |  Prioridad   
---|---|---|---  
6 |  15 |  1 |  1   
7 |  55 |  2 |  6   
8 |  2 |  1 |  2   
9 |  5 |  3 |  4   
10 |  1 |  3 |  5   
11 |  2 |  1 |  3   
12 |  10 |  1 |   
  
Segundo se Recalculan las prioridades 

ID |  Num |  Modo |  Prioridad   
---|---|---|---  
6 |  15 |  1 |  1   
7 |  55 |  2 |  7   
8 |  2 |  1 |  2   
9 |  5 |  3 |  5   
10 |  1 |  3 |  6   
11 |  2 |  1 |  3   
12 |  10 |  1 |  4   

###  Apartado 6 

Realizar un subalgoritmo que elimine un trabajo de la matriz. Se dará como entrada la posición del trabajo a eliminar en la matriz, la matriz y el tamaño de ésta. Entonces se eliminará la fila, y se correrán todas las celdas una posición hacia arriba. Una vez hecho esto, se actualizarán las prioridades del sistema usando el subalgoritmo del apartado 4). 

_Ejemplo_ : Entrada: posición: 1 

Primero se elimina trabajo y se decrementa el tamaño. 

ID |  Num |  Modo |  Prioridad   
---|---|---|---  
7 |  55 |  2 |  7   
8 |  2 |  1 |  2   
9 |  5 |  3 |  5   
10 |  1 |  3 |  6   
11 |  2 |  1 |  3   
12 |  10 |  1 |  4   
  
Segundo: se reordena 

ID |  Num |  Modo |  Prioridad   
---|---|---|---  
7 |  55 |  2 |  6   
8 |  2 |  1 |  1   
9 |  5 |  3 |  4   
10 |  1 |  3 |  5   
11 |  2 |  1 |  2   
12 |  10 |  1 |  3   

###  Apartado 7 

Hacer el algoritmo principal que realice las siguientes operaciones utilizando un menú con las siguientes opciones: 

  1. Mostrar. En esta opción se mostrarán los trabajos que hay pendientes de hacer: Primero, Escáner, después Impresora y por último Fotocopiadora (usar subalgoritmo del apartado 1). 
  2. Nuevo. En esta opción se insertará un nuevo trabajo (usar subalgoritmo del apartado 5). Nota: habrá que pedir al usuario el modo y el número de copias. 
  3. Imprimir: En esta opción primero se buscará el siguiente trabajo a imprimir (usar subalgoritmo del apartado 2) y dada la posición obtenida, si se puede, se eliminará dicho trabajo (usando el subalgoritmo del apartado 6). 
  4. Terminar