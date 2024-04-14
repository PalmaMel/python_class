# Contador atgc

Este es un script de Python diseñado para contar las ocurrencias de A, T, C y G en un FASTA.

## Uso

 El usuario puede pasar el nombre del archivo que contiene la secuencia de ADN como primer argumento y, opcionalmente, especificar los nucleótidos de los cuales desea conocer la frecuencia de aparición como argumentos adicionales e imprira el recuento de aparición de estos, de no ser asi el programa imprimira en pantalla el recuento de todas las bases.

```
import sys

# Verifica que se haya proporcionado el nombre del archivo como argumento
if len(sys.argv) < 2:
    print("Uso: Python count_atcg.py nombre_del_archivo [nucleotidos]")
    sys.exit(1)

nombre_archivo = sys.argv[1]

# Obtener los nucleótidos específicos, si se proporcionan
nucleotidos_especificos = set(sys.argv[2:]) if len(sys.argv) > 2 else {'A', 'C', 'G', 'T'}

# Abre el archivo en modo lectura
with open(nombre_archivo, 'r') as file:
    # Lee la cadena de ADN del archivo
    dna_sequence = file.read()

# Inicializa contadores para cada símbolo
count_A = 0
count_C = 0
count_G = 0
count_T = 0

# Itera sobre la cadena de ADN y cuenta las ocurrencias de cada símbolo
for symbol in dna_sequence:
    if symbol == 'A':
        count_A += 1
    elif symbol == 'C':
        count_C += 1
    elif symbol == 'G':
        count_G += 1
    elif symbol == 'T':
        count_T += 1

# Imprime el resultado para los nucleótidos específicos o para todos si no se especifican
if nucleotidos_especificos:
    for nucleotido in nucleotidos_especificos:
        count = 0
        if nucleotido == 'A':
            count = count_A
        elif nucleotido == 'C':
            count = count_C
        elif nucleotido == 'G':
            count = count_G
        elif nucleotido == 'T':
            count = count_T
        print(f'El símbolo {nucleotido} aparece {count} veces.')
else:
    print(f'El símbolo A aparece {count_A} veces.')
    print(f'El símbolo C aparece {count_C} veces.')
    print(f'El símbolo G aparece {count_G} veces.')
    print(f'El símbolo T aparece {count_T} veces.')

```

## Salida

El script imprime a pantalla el recuento de apariciones de cada base si no se le especifico cuales se queria contar.

## Control de errores

Si no se ingresa el archivo o si no se encuentra el archivo ingresado el programa va a mandar un ensaje de eror a pantalla, otro mensaje de error proporcionado es para cuando el arcgivo esta vacio o contiene caracteres distintos a las bases.
El codigo acepta como argumentos las bases como minusculas o mayusculas, de ser lo primero las convierte a mayusculas.
## Pruebas

Ejemplo de uso:

```
# Ejemplo de uso: Tenemos un archivo prueba.txt 
# Este tiene la siguiente secuencia ATCGATCGATCGTACGTA
Python count_atgc.py prueba.txt A C  # ejecutamos de la sig manera 
Python ptueba.txt A C # pedimos solo cuente A y C

# la salida debe ser :
# El símbolo A aparece 4 veces.
# El símbolo C aparece 4 veces.

```

## Datos

El script está diseñado para operar en archivos de texto plano, con un número por línea. No hay restricciones en el número de líneas en el archivo.

## Metadatos y documentación

Este README ofrece información de uso básico. Para obtener información más detallada sobre el diseño y la implementación del script, consulte [Enlace a la documentación].

## Código fuente

El código fuente está disponible en este repositorio. Se acoge con satisfacción cualquier contribución o sugerencia a través de solicitudes pull request.

## Términos de uso

Este script está disponible bajo la licencia Apache. Consulte el archivo LICENSE para obtener más detalles.

## Como citar

Si utiliza este script en su trabajo, por favor cite: [información de citación].

## Contáctenos -=-

Si tiene problemas o preguntas, por favor abra un problema en este repositorio o póngase en contacto con nosotros en: [información de contacto].

