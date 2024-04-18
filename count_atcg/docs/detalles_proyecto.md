# Sumador de Números en Archivo

Fecha: 11/04/2024

**Participantes**:

- Melissa Palma <email:melissap@lcg.unam.mx>

## Descripción del Problema

Este es un proyecto cuenta el números de apariciones de las bases A, C, T y G en un archivo de texto.

El problema enunciado implica que se va a ir leyendo linea por linea del archivo porporcionado y se van a ir alamcenando la frecuencia de aparición de cada base

## Especificación de Requisitos

Requisitos funcionales

- El programa debe aceptar un nombre de archivo como argumento de línea de comandos 
- 
- Requisito

Requisitos no funcionales

- De no recibir especificacion de que nucleotidos de A, C , G o T va a contar el programa va a imprimir a pantalla la aparición de cada uno de ellos (A, C , G o T)
- Requisito
- Requisito



## Análisis y Diseño
El script proporcionado es un programa escrito en Python que cuenta las ocurrencias de cada base nucleotídica (A, C, G, T) en una secuencia de ADN. El script toma un archivo como entrada que contiene la secuencia de ADN y opcionalmente acepta una lista de bases nucleotídicas específicas que se deben contar.

El código comienza verificando si se proporciona al menos un argumento (el nombre del archivo) en la línea de comandos. Si no se proporciona ninguno, muestra un mensaje de uso y sale del script. El primer argumento se toma como el nombre del archivo que contiene la secuencia de ADN. El código abre el archivo especificado en modo lectura y lee su contenido. Verifica si la secuencia de ADN no está vacía y si contiene caracteres válidos (A, C, G, T). Si encuentra caracteres no válidos, muestra un mensaje de error y sale del script. 

Después el código inicializa contadores para cada base  (A, C, G, T) y luego itera sobre la secuencia de ADN. Cuenta las ocurrencias de cada base y almacena los resultados en los contadores correspondientes y finalmente, el código imprime el número de ocurrencias de cada base especificada por el usuario o de todas las bases si no se proporciona ninguna especificación. Utiliza el conjunto de argumentos de la línea de comandos para determinar qué bases contar.

```
 Python count_atcg.py nombre_del_archivo [nucleotidos]"
```

El formato de los datos de entrada será simplemente un archivo con la secuencia de DNA y los nulceotidos a contar, que pueden ser A,C,T Y G  La salida será una línea de texto que muestra el numero de apariciones de los nucleotidos especificados o de todos.


#### Caso de uso: 

```
         +---------------+
         |   Usuario     |
         +-------+-------+
                 |
                 | 1. Proporciona archivo de entrada y/o bases se quiere contar
                 v
         +-------+-------+
         |   Programa    |
         |               |
         |               | 
         |               |
         +---------------+
                |
                |
                v
             conteo 
```

- **Actor**: Usuario
- **Descripción**: El actor proporciona un archivo 
- **Flujo principal**:

	1. El actor inicia el sistema 
	2. El sistema comprueba los argumentos sean validos
	3. El sistema inicia contadores e itera sobre la secuencia de DNA
	4. El sistema imprime la frecuencia de aparición de las bases especificadas o de todas las bases
	
- **Flujos alternativos**:
	- Si el archivo proporcionado no existe
		1. El sistema muestra un mensaje de error "Sorry, couldn´t find the file: '{nombre_archivo}'"
	- Si el archivo esta vacio
		1. El sistema muestra un mensaje de error "Sorry, the file '{nombre_archivo}' is empty"
        - Si proporciona un argumento valido 
                1. El sistema muestra un mensaje de error: "Error: invalid base argument: {', '.join(nucleotidos_invalidos)}"
        - Si el archivo tiene una base invalida 
                1. El sistema muestra un mensaje de error: "Error: Sequence contains '{symbol}', it is invalid character"