---
title: "Calculo de la diferencia entre dos fechas"
date: 2024-01-01
draft: false
languages: ['c', 'pseudocódigo']
professors: ['angel']
categories: ['análisis', 'comentario', 'enunciado']
---

# Calculo de la diferencia entre dos fechas

##  Enunciado 

Modifica el programa [**tiempo.c**](/ejercicios/función-sin-argumentos/) de manera que permita introducir las dos horas, incluyendo los segundos, utilizando el formato 3:22:17 y calcule la diferencia en horas, minutos y segundos. Además deberá avisar en el caso de que la segunda hora sea anterior a la primera o si se teclea una hora errónea, es decir, que el número correspondiente a las horas sea mayor que 24 ó el de los minutos mayor que 60, etc. Guarda este programa como **tiempo2.c**. 

##  Soluciones 

###  Programa en C por **Angel**

Solución comentada al Ejercicio: 
```c

/* fichero tiempo2.c */
#include <stdio.h>
void main(void) {
  int horas, minutos;
  long diferencia, segundos1, segundos2;
  long segs(void);
  printf("Escribe la primera hora (formato 3:22:14): ");
  segundos1=segs();
  do {
      printf("Escribe la segunda hora (posterior): ");
      segundos2=segs();
  } while (segundos2<=segundos1);
  diferencia=segundos2-segundos1;
  horas=(int)(diferencia/3600);
  diferencia=diferencia%3600;
  minutos=(int)(diferencia/60);
  diferencia=diferencia%60;
  printf("La diferencia es %d hora(s), %d minuto(s), %d segundo(s).\n", horas, minutos, diferencia);
}
long segs(void) {
  int horas, minutos, segundos, pass = 0;
  long total;
  do {
      pass=0;
      scanf("%d:%d:%d", &horas, &minutos, &segundos);
      if (horas>24)
          pass=1;
      if (minutos>60)
          pass=1;
      if (pass==1) { 
          printf("Hora incorrecta!!!!\n");
          printf("Escribe la hora correcta: ");
      }
  } while(pass==1);
  total=(long)horas*3600;
  total+=(minutos*60+segundos);
  return total;
}
```

####  Comentario 

Para calcular la diferencia entre las dos horas es necesario convertirlas antes en segundos, para así poder restarlas. Después hay que convertir este número, en segundos, a horas, minutos y segundos. Para obtener las horas se divide el número entre 3600 segundos/hora, quedándonos con el número entero que resulta. El resto de esta división, es decir, el resto de los segundos se convertirán a minutos dividiendo por 60 segundos/minuto. El número entero resultante de esta división serán los minutos y el resto los segundos. Dentro de la funcion **segs()** aparece un bucle **do while** , que como ya sabemos siempre se ejecuta al menos una vez. En nuestro caso el bucle se ejecutará sólo una vez, si el usuario ha tecleado correctamente la hora. De lo contrario, es decir, si se equivoca al teclear el número correspondiente a las horas, los minutos o los segundos, la variable pass tomará el valor 1, que es la condición para que el bucle se vuelva a ejecutar. De esta forma se pueden teclear otra vez los datos. Obsérvese que la función **segs()** devuelve un valor de tipo **long** , esto es debido a que si la diferencia entre horas es 24 (máximo valor posible). Este valor en segundos (86400) supera la capacidad de una variable de tipo **int**. Dentro de **main()** también hay otro bucle **do while** , que se ejecuta más de una vez en el caso de que la segunda hora sea anterior a la primera, dando así la posibilidad de volver a teclear la hora. 

###  Diseño en Pseudocódigo
```text
 FUNCION segs():ENTERO
 ENTRADAS:
   _(No tiene entradas, las lee por teclado)_
 SALIDAS: 
   total: ENTERO  _(Número de segundos de la hora introducida por teclado)_
 VARIABLES:
   horas:   ENTERO
   minutos: ENTERO
   segundos:ENTERO
   pass:    ENTERO
 INICIO
            
   REPETIR
      pass <-- 0
      LEER horas, minutos, segundos
      SI horas>24 ENTONCES
              pass<--1
      FIN_SI
      SI minutos>60 ENTONCES
          pass<--1
      FIN_SI
      SI pass=1 ENTONCES
          ESCRIBIR "Hora incorrecta!!!!"
          ESCRIBIR "Escribe la hora correcta: "
      FIN_SI
   HASTA pass<>1
                       
  total <-- horas*3600
  total <-- total+(minutos*60+segundos)
  DEVOLVER total
                  
 FIN

_(Programa principal)_              
 ALGORITMO tiempo2
 ENTRADAS:
     segundos1:ENTERO  _(Primera hora en segundos)_
     segundos2:ENTERO  _(Segunda hora en segundos)_
 SALIDAS:
     horas: ENTERO      _(Horas de la diferencia entre horas)_
     minutos: ENTERO    _(Minutos de la diferencia entre horas)_
     diferencia: ENTERO _(Segundos de la diferencia entre horas)_
 VARIABLES:
                                    
 INICIO
     _(Leer las horas)_         
     ESCRIBIR "Escribe la primera hora (formato 3:22:14): "
     segundos1<--segs()
     REPETIR
         ESCRIBIR "Escribe la segunda hora (posterior): "
         segundos2<--segs()
     HASTA segundos2 > segundos1

     _(Calcular la diferencia horaria)_
     diferencia<--segundos2-segundos1
     horas<--diferencia DIV 3600
     diferencia<--diferencia MOD 3600
     minutos<--diferencia DIV 60
     diferencia<--diferencia MOD 60

     _(Mostrar el resultado)_
     ESCRIBIR "La diferencia es ",horas, " hora(s), ", minutos, " minuto(s), ", diferencia, " segundo(s)."

 FIN
```

####  Comentario 

En pseudocódigo no tiene sentido la limitación de leer la hora en el formato _3:22:17_ , por lo tanto, no se ha tomado en cuenta.