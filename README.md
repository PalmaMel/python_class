# Contador atgc

Este es un script de Python diseñado para contar las ocurrencias de A, T, C y G en un FASTA.

## Uso

El script  recorre cada línea del archivo FASTA (ignorando la primera línea del encabezado) y cuenta las ocurrencias de las bases A, T, C y G en esas líneas. Luego devuelve un diccionario que contiene el recuento de cada base.

```
def contar_apariciones_atcg(archivo):
    """
    Función para contar las apariciones de las bases A, T, C, y G en un archivo FASTA.
    
    Parámetros:
        archivo (str): La ruta al archivo FASTA.
    
    Retorna:
        dict: Un diccionario que contiene el recuento de cada base (A, T, C, G).
    """
    # Inicializar el diccionario para contar las apariciones de las bases
    conteo_bases = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    
    # Leer el archivo FASTA
    with open(archivo, 'r') as f:
        # Ignorar la primera línea del encabezado
        next(f)
        # Leer el resto del archivo línea por línea
        for linea in f:
            # Contar las bases en la línea actual
            for base in linea.strip():
                if base.upper() in conteo_bases:
                    conteo_bases[base.upper()] += 1
                    
    return conteo_bases

# Uso del script
if __name__ == "__main__":
    archivo_fasta = 'archivo.fasta'  # Cambiar por la ruta a tu archivo FASTA
    conteo = contar_apariciones_atcg(archivo_fasta)
    print("Apariciones de A:", conteo['A'])
    print("Apariciones de T:", conteo['T'])
    print("Apariciones de C:", conteo['C'])
    print("Apariciones de G:", conteo['G'])

```

## Salida

El script imprime a pantalla el recuento de apariciones de cada base.

## Control de errores



## Pruebas

El script 

```
python
```

## Datos

El script está diseñado para operar en archivos de texto plano, con un número por línea. No hay restricciones en el número de líneas en el archivo.

## Metadatos y documentación

Este README ofrece información de uso básico. Para obtener información más detallada sobre el diseño y la implementación del script, consulte [Enlace a la documentación].

## Código fuente

El código fuente está disponible en este repositorio. Se acoge con satisfacción cualquier contribución o sugerencia a través de solicitudes pull request.

## Términos de uso

Este script está disponible bajo la licencia [nombre de la licencia]. Consulte el archivo LICENSE para obtener más detalles.

## Como citar

Si utiliza este script en su trabajo, por favor cite: [información de citación].

## Contáctenos -=-

Si tiene problemas o preguntas, por favor abra un problema en este repositorio o póngase en contacto con nosotros en: [información de contacto].

