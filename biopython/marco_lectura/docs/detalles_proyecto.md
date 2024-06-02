# Marcos de Lectura de distintas secuencias 

Fecha: 31/05/2024

**Participantes**:

- Melissa Palma <email:melissap@lcg.unam.mx>
## Descripcion del Problema

El codigo es un script en Python que permite al usuario leer secuencias de ADN desde un archivo FASTA, seleccionar una secuencia específica, y procesarla según un marco de lectura especificado (directo o inverso). El usuario proporciona el archivo de entrada y el script lista todas las secuencias disponibles, permitiendo la seleccion de una secuencia por su índice. Luego, el usuario elige un marco de lectura (1 a 6), y el script procesa la secuencia para extraer los codones correspondientes, manejando adecuadamente los marcos de lectura inversos al invertir la secuencia. Finalmente, los codones resultantes se escriben en un archivo de salida cuyo nombre depende del marco de lectura seleccionado, facilitando la organizacion y análisis posterior de los resultados.

## ## Especificacion de Requisitos
### Requisitos Funcionales

1. Lectura de Secuencias desde Archivo FASTA:
    - El programa debe ser capaz de leer un archivo FASTA proporcionado por el usuario.
    - Las secuencias leidas deben ser listadas con su índice, ID y descripcion para permitir la seleccion.
2. Seleccion de Secuencia:
    - El programa debe permitir al usuario seleccionar una secuencia especifica de la lista mostrada.
3. Selección de Marco de Lectura:
    - El programa debe permitir al usuario seleccionar un marco de lectura entre 1 y 6
4. Procesamiento de Secuencia:
    - El programa debe procesar la secuencia seleccionada segun el marco de lectura especificado.
    - Si el marco de lectura es inverso, la secuencia debe ser invertida antes de procesar los codones.
    - Los codones deben ser extraidos y listados de acuerdo al marco de lectura.
5. Salida de Resultados:
    - Los codones resultantes deben ser escritos en un archivo de salida.
    - El nombre del archivo de salida debe depender del marco de lectura seleccionado (e.g., output_frame_1.txt).
6. Interaccion con el Usuario:
    - El programa debe solicitar al usuario la secuencia a usar y el marco de lectura mediante entradas de teclado.
    - Debe verificar que el marco de lectura ingresado sea valido (entre 1 y 6).
    - Debe informar al usuario si el marco de lectura es invalido y terminar la ejecucion.

## Analisis y diseño

El script presentado es un programa en Python que permite a los usuarios procesar secuencias de ADN almacenadas en archivos FASTA. A traves de una interfaz de linea de comandos, el programa lee un archivo FASTA especificado por el usuario, muestra las secuencias disponibles con sus identificadores y descripciones, permite la seleccion de una secuencia especifica, solicita al usuario que elija un marco de lectura entre 1 y 6, procesa la secuencia seleccionada para extraer los codones correspondientes segun el marco de lectura especificado, y finalmente guarda los codones resultantes en un archivo de salida con un nombre que depende del marco de lectura elegido. El diseño modular del programa facilita su mantenimiento y extensibilidad, mientras que el uso de la biblioteca Biopython simplifica la manipulacion de secuencias de ADN.

```
    Python select_sequence.py <archivo_entrada.fasta>
```
El formato de los datos de entrada sera simplemente un archivo con las secuencias en formato Fasta. 
La salida sera un archivo con los codones aen el marco de lectra especificado y separados por un espacio.
- **Actor**: Usuario
- **Descripcion**: El actor proporciona un archivo 
- **Flujo principal**:
    1. El actor inicia el sistema 
    2. El sistema comprueba los argumentos sean validos
    3. El sistema lee el archivo FASTA especificado por el usuario y muestra una lista de secuencias disponibles con sus identificadores y descripciones.
    4. El actor selecciona una secuencia especifica de la lista mostrada.
    5. El sistema solicita al usuario que elija un marco de lectura entre 1 y 6.
    6. El actor selecciona un marco de lectura válido.
    7. El sistema procesa la secuencia seleccionada para extraer los codones correspondientes segun el marco de lectura especificado.
    8. Si el marco de lectura es inverso, el sistema invierte la secuencia antes de extraer los codones.
    9. Los codones resultantes se guardan en un archivo de salida con un nombre que depende del marco de lectura elegido.
    10. El sistema informa al usuario sobre la finalizacion exitosa del procesamiento y la ubicacion del archivo de salida.
