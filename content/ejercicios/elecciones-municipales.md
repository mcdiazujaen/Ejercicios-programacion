---
title: "Elecciones municipales"
date: 2024-01-01
draft: false
languages: []
categories: ['enunciado']
tags: ['Sin Matlab', 'Sin solución']
---

# Elecciones municipales

##  Enunciado

Se necesita un programa que gestione la información de las elecciones municipales. Cada municipio se va a identificar mediante un número entero (entre **1** y **N**), cada partido mediante otro entero (entre **1** y **M**). Por cada municipio se va a recoger información acerca de su censo y el número de votos que ha recibido cada uno de los partidos. La información del censo se va a almacenar en un array de **N** elementos, de forma que en la posición **i** estará almacenado el censo del municipio **i**. La información acerca de los votos se almacenará en una matriz de tamaño **MxN** de forma que las columnas representan los municipios y las filas los partidos. 

Con este planteamiento diseña un algoritmo que resuelva los siguientes apartados: 

###  Módulo 1 

Módulo que lea la información y devuelva las estructuras de datos correspondientes: 

  * Debe leer desde teclado el vector que contiene el censo de los municipios. 
  * Debe leer desde un fichero llamado **recuentoVotos.txt** , la información de los votos conseguidos por los distintos partidos en los municipios. Con esta información debe devolver una matriz con las características descritas anteriormente. En el fichero todos los datos están en una fila, van todos los votos del partido 1 en cada uno de los municipios, a continuación los del partido 2 y así sucesivamente. El primer entero de dicho fichero es el número de partidos que se están considerando. Ejemplo para el caso de 3 partidos y 2 municipios 

Censo (_El municipio 1 tiene 110000 habitantes y el 2 tiene 4500_) 
```text
  110000  4500  
```

Fichero **recuentoVotos.txt** : 
```text
  3 20000 1600 10000 800  60000 480
```

Matriz resultante: (_En este caso se tienen que el partido 1 ha obtenido 20000 votos en el municipio 1 y el mismo partido ha obtenido 1600 en el municipio 2_) 
```text
  20000  1600 
  10000   800
  60000   480
```

###  Módulo 2 

Módulo que dado como parámetro de entrada el número de un municipio y los datos del censo y el recuento de votos, devuelva el % de participación y de abstención en dicho municipio. 

###  Módulo 3 

Módulo que devuelva el número de partido más votado en las elecciones, así como el número de votos obtenido por el mismo. 

###  Módulo 4 

Módulo principal que, utilizando los módulos anteriores, lea los datos y escriba en un fichero llamado **resultadosElecciones.txt** lo siguiente: 

  *  % de participación y abstención en cada municipio. 
  * Número del partido más votado y el número de votos que ha obtenido. 
  * Debe escribir los datos acompañados de comentarios que indiquen a qué hacen referencia. 

Se deben especificar de forma clara las variables de entrada, salida e intermedias así como sus tipos para cada uno de los módulos. 

##  Soluciones