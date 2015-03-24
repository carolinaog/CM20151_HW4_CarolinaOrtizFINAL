#include <stdio.h>
#include <stdlib.h>
#define SHELLSCRIPT "\
#/bin/bash \n\
timeout 4 rec -c1 -b16 nombre.wav \n\
"
int main (void)
{
  	//Ejecute este archivo en la consola como ./grabar_mi_nombre.x Esto abrirá el grabador de voz "rec", Diga su nombre en 4 secs y termine de grabar digitando Ctrl+C . 
	//Se generará el archivo nombre.wav para proseguir con el siguiente punto
	puts("El sistema ejecutara el siguiente script antes de comenzar el metodo:");
 	puts(SHELLSCRIPT);
  	system(SHELLSCRIPT);
return 0;

}
