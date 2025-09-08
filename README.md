Generador de Secuencia Numérica

Este script en Python crea una secuencia de números basándose en un rango que tú defines y la guarda en un archivo de texto (.txt).  Es una herramienta útil para generar listas de números de forma rápida y eficiente para pruebas o análisis de datos.
Uso

El script utiliza argumentos de línea de comandos. Debes especificar los siguientes parámetros al ejecutarlo en tu terminal.

Parámetro
Tipo
Requerido
Descripción
--inicio
int
Sí
El número con el que comenzará la secuencia.
--fin
int
Sí
El número con el que terminará la secuencia (incluido).
--nombre
str
Sí
	
El nombre del archivo que se va a generar (sin la extensión .txt).
Ejemplo de uso

Para crear una secuencia de números del 0 al 100 y guardarla en un archivo llamado mi_secuencia.txt, usa el siguiente comando:

python generador_diccionario.py --inicio 0 --fin 100 --nombre mi_secuencia

El script te preguntará si deseas sobrescribir el archivo en caso de que ya exista.
Requisitos
El script solo requiere una instalación de Python 3. No se necesitan librerías adicionales.
