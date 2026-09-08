# Documentación

## Entrega

La entrega se realiza vía **aula.usm.cl** en formato `.zip`.

## Multiplicación de matrices

Algoritmos: Naive, Strassen

### Programa principal
El programa principal está hecho en C++ (matrix_multiplication.cpp). Este código se encarga de recibir dos matrices desde archivos de 
la carpeta matrix_input, multiplicarlas usando el algoritmo indicado (Naive o Strassen), y guardar la matriz resultante en un nuevo 
archivo de texto en la carpeta matrix_ouput. También guarda el tiempo exacto que demoró la operación de cada algoritmo dentro de la 
carpeta measurements. Para compilarlo fácilmente, se utiliza su respectivo Makefile. (Nota: Las páginas web de donde se sacaron las 
implementaciones de los algoritmos están puestas como comentarios en la primera línea de cada archivo .cpp dentro de la carpeta 
algorithms).

### Scripts
Para la parte de Python usamos tres archivos principales:
matrix_generator.py: Este script se encarga de crear todas las matrices de prueba con distintos tamaños y tipos requeridos por la tarea.
Automatizacion_matriz.py: Ejecuta todas las combinaciones automáticamente llamando al programa de C++ una por una, ordenando los 
resultados y los tiempos.
plot_generator.py: Lee los archivos con los resultados de tiempo y dibuja los gráficos de forma automática guardándolos en formato PNG 
dentro de la carpeta de imágenes (plots).  

## Ordenamiento de arreglo unidimensional

Algoritmos: MergeSort, QuickSort, PatienceSort, std::sort.

### Programa principal
El programa principal en C++ (sorting.cpp) toma un archivo de texto con un arreglo sacado de array_input, lo ordena usando el algoritmo 
elegido y crea un archivo nuevo con el resultado dejado en array_output. Al mismo tiempo, toma el tiempo que se demoró en ordenar y lo 
guarda en la carpeta measurements dentro de cada subcarpeta del logaritmo usado. Igual que el de matrices, se compila usando el archivo 
Makefile. (Nota: Las fuentes y links de los algoritmos están documentadas al inicio de cada archivo .cpp). 

### Scripts
En la carpeta de scripts de Python para esta sección usamos tres archivos:
array_generator.py: Genera todos los arreglos de números de prueba, ya sean aleatorios, ascendentes o descendentes.
Automatizacion_sort.py: Muestra el tiempo de proceso en vivo en la consola y tiene un tope de 1 hora para evitar que el computador 
colapse con los arreglos demasiado grandes, de igual forma va ejecutando las combinaciones y llamando al programa c++.
plot_generator.py: Lee los archivos generados con las mediciones y dibuja todos los gráficos que se usaron en el informe final en 
formato PNG.

## Requisitos previos (Dependencias)
Para que el código compile y los scripts de Python funcionen correctamente sin errores, asegúrese de tener instalado:
* Un entorno Linux (o WSL en Windows) con el compilador `g++` y `make`.
* Python 3 con las siguientes librerías instaladas (se pueden instalar vía pip):
  * `pandas` (para organizar los datos)
  * `matplotlib` (para generar los gráficos)
  * `tqdm` (para visualizar la barra de carga en la terminal)

## Instrucciones de Ejecución
Para ejecutar cualquiera de los dos problemas (Matrices u Ordenamiento), los pasos son los mismos. Debe abrir su terminal de Linux, 
ubicarse dentro de la carpeta correspondiente (`code/sorting/` o `code/matrix_multiplication/`) y seguir estos pasos:

1. **Compilar el código C++:**
   Escriba el siguiente comando en la terminal para compilar el programa principal usando el Makefile:
   `make`

2. **Generar los datos de prueba (Opcional):**
   Si los archivos de texto de entrada no están creados, ejecute el generador:
   `python3 scripts/array_generator.py` (o `scripts/matrix_generator.py`)

3. **Correr la automatización:**
   Ejecute el automatizador de los programas. Este programa correrá todos los algoritmos, tomará los tiempos y creará los archivos de 
   salida automáticamente:
   `python3 scripts/Automatizacion_sort.py` (o `scipts/Automatizacion_matriz.py`)

4. **Generar los gráficos:**
   Una vez que el orquestador termine al 100%, ejecute el creador de gráficos en cada uno de las carpetas:
   `python3 scripts/plot_generator.py`
   Las imágenes PNG aparecerán listas dentro de la carpeta `data/plots/`.