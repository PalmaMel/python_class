# Marcos de Lectura de distintas secuencias 

Fecha: 31/05/2024

**Participantes**:

- Melissa Palma <email:melissap@lcg.unam.mx>
## Descripcion del Problema

El codigo es un script en Python que permite al usuario leer secuencias de ADN desde un archivo FASTA y procesarlas segun los seis posibles marcos de lectura (tres directos y tres inversos). El usuario proporciona el archivo de entrada, y el script lista todas las secuencias disponibles. Luego, el script procesa cada secuencia automáticamente para extraer los codones correspondientes en cada uno de los seis marcos de lectura, manejando adecuadamente los marcos de lectura inversos al invertir la secuencia. Finalmente, los codones resultantes se escriben en un archivo de salida cuyo nombre depende de la identificación de la secuencia procesada, facilitando la organización y análisis posterior de los resultados.

## Especificacion de Requisitos
### Requisitos Funcionales

1. Lectura de Secuencias desde Archivo FASTA:
    - El programa debe ser capaz de leer un archivo FASTA proporcionado por el usuario.
    - Las secuencias leídas deben ser listadas con su indice, ID y descripción para permitir la selección.
2. Procesamiento de Secuencia:
    - El programa debe procesar cada secuencia en todos los seis posibles marcos de lectura (tres directos y tres inversos).
    - Si el marco de lectura es inverso, la secuencia debe ser invertida antes de procesar los codones.
    - Los codones deben ser extraídos y listados de acuerdo al marco de lectura.
3. Salida de Resultados:
    - Los codones resultantes deben ser escritos en un archivo de salida.
    - El nombre del archivo de salida debe depender de la identificación de la secuencia procesada (e.g., output_seq1.txt).
4. Interacción con el Usuario:
    - El programa debe mostrar al usuario todas las secuencias disponibles con su indice, ID y descripcion.
    - Debe procesar cada secuencia en todos los marcos de lectura posibles automáticamente sin necesidad de seleccion adicional.
    - Debe informar al usuario sobre la finalizacion del procesamiento y la creación de los archivos de salida correspondientes.

## Analisis y diseno

El script presentado es un programa en Python que permite a los usuarios procesar secuencias de ADN almacenadas en archivos FASTA. A traves de una interfaz de linea de comandos, el programa lee un archivo FASTA especificado por el usuario, muestra las secuencias disponibles con sus identificadores y descripciones, y procesa cada secuencia en todos los marcos de lectura posibles (tres directos y tres inversos). Cada secuencia procesada genera un archivo de salida con los codones correspondientes separados por espacios, facilitando su analisis posterior. El diseno modular del programa facilita su mantenimiento y extensibilidad, mientras que el uso de la biblioteca Biopython simplifica la manipulación de secuencias de ADN.

```
    Python select_sequence.py <archivo_entrada.fasta>
```

El formato de los datos de entrada sera un archivo con las secuencias en formato FASTA. La salida será un archivo con los codones en cada uno de los seis marcos de lectura posibles, separados por un espacio.

- **Actor**: Usuario
- **Descripcion**: El actor proporciona un archivo 
- **Flujo principal**:
    1. El actor inicia el sistema.
    2. El sistema comprueba que los argumentos sean validos.
    3. El sistema lee el archivo FASTA especificado por el usuario y muestra una lista de secuencias disponibles con sus identificadores y descripciones.
    4. El sistema procesa cada secuencia en todos los marcos de lectura posibles (directos e inversos).
    5. Si el marco de lectura es inverso, el sistema invierte la secuencia antes de extraer los codones.        
    6. Los codones resultantes se guardan en un archivo de salida con un nombre que depende de la identificación de la secuencia procesada.
    7. El sistema informa al usuario sobre la finalizacion exitosa del procesamiento y la ubicación del archivo de salida.