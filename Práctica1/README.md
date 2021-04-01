# Práctica 1

Jesús Alberto Reyes Gutiérrez

La especificación de la práctica se encuentra en el archivo
_Practica1-2021-2.pdf_ de esta carpeta.

## Para correr el programa

Desarrollé la práctica con **Python 3** por lo que este es necesario y 
usé la librería _**pygame**_ para crear la interfaz de usuario por lo
que es necesario instalarla antes de correr el programa. Esto se puede
hacer con el siguiente comando usando _pip3_:

```
pip3 install pygame
```

Para correr el programa (ejecutando desde _src_) hay dos opciones:

1. Pasando el tamaño de la cuadrícula como argumento, esto es,
   siguiendo lo establecido en la especificación. Por ejemplo:
   
   ```
   python3 main.py 4
   ```
   
2. Sin pasar el tamaño como argumento. Para esto sólo se ejecuta con
   _python3_ el archivo _main.py_ y después se elegirá el tamaño en la 
   interfaz de usuario (ver la siguiente sección). Por ejemplo:
   
   ```
   python3 main.py
   ```

## Sobre la interfaz de usuario
Si no se seleccionó un tamaño al ejecutar se mostrará una pantalla en
la que el programa esperará a que se elija un valor para _k_ con el
teclado. Después aparecerá una cuadrícula del tamaño dado, aquí se debe
seleccionar con el mouse el que será el cuadrito especial y después de
esto se adoquina la cuadrícula.

Al terminar de adoquinar se puede dar clic en la pantalla para volver a
la pantalla de selección o puede terminar el programa cerrando la
ventana.

## Sobre los archivos fuente
La carpeta _src/_ contiene los archivos fuente que son _adoquinador.py_
y _main.py_.
* _adoquinador.py_ contiene las funciones necesarias para calcular
   los adoquines del problema.
* _main.py_ contiene el método _main_ en el que se desarrolla la
  interfaz de usuario.