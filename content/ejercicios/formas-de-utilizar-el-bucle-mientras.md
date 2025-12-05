---
title: "Formas de utilizar el bucle MIENTRAS"
date: 2024-01-01
draft: false
languages: ['pseudocódigo']
categories: ['enunciado']
---

# Formas de utilizar el bucle MIENTRAS

##  Enunciado 

Dar tres formas diferentes de cambiar el siguiente bucle de forma que se ejecute 20 veces en lugar de 19. ¿Cuál de los tres cambios hace que el valor de Cont vaya desde 1 a 20? 
```text
 Cont <-- 1
 MIENTRAS Cont < 20 HACER
   Cont <-- Cont+1
 FIN_MIENTRAS

```
##  Soluciones

###  Primera solución 

Lo que vamos a hacer para que el bucle llegue hasta 20, en lugar de hasta 19, es poner un igual ( <= ) al comparar _Cont_ en el bucle MIENTRAS, de esta forma contará desde 1 hasta 20. 
```text
 Cont <-- 1
 MIENTRAS **Cont <= 20** HACER
   Cont <-- Cont+1
 FIN_MIENTRAS

===Primera solución===
 cont=1;
 while (cont<=20){
  cont++;
}

```
###  Segunda solución 

Definiremos _Cont_ desde 0, así el bucle se ejecutará 20 veces pero llegará hasta 19 : 
```text
 **Cont <--  0**
 MIENTRAS Cont < 20 HACER
   Cont <-- Cont+1
 FIN_MIENTRAS

===Segunda solución===
  cont=0;
  while (cont<20){
      cont++;
  }

```
###  Tercera solución 

En este caso definiremos _Cont_ en el bucle MIENTRAS para que llegue hasta 20, lo haremos poniendo que sea menor que 21: 
```text
 Cont <-- 1
 MIENTRAS **Cont < 21** HACER
   Cont <-- Cont+1
 FIN_MIENTRAS

===Tercera Solucion===
 while(cont<21){
  cont++;
 }
```