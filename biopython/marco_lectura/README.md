# Reading Frame 
Este script 
## Uso
El usuario puede utilizar el script proporcionando el nombre del archivo que contiene las secuencias de ADN en formato FASTA como argumento al ejecutar el programa desde la linea de comandos.

"""
    python script.py secuencias.fasta
"""
Una vez ejecutado el programa, seguira las instrucciones proporcionadas por la interfaz de usuario para seleccionar una secuencia especifica y elegir un marco de lectura. Despues de completar estos pasos, el programa procesara la secuencia seleccionada y guardara los resultados en un archivo de salida con un nombre que refleja el marco de lectura elegido.
"""
import sys
import Bio.Seq
import re
from Bio.Seq import Seq
from Bio import SeqIO
def list_sequences(input_file):
    """
    Lee un archivo FASTA y lista todas las secuencias contenidas

    Args:
        input_file: Ruta del archivo FASTA que contiene las secuencias

    Returns:
        Lista de todas las secuencias leidas
    """
    sequences = list(SeqIO.parse(input_file, "fasta"))
    for i, record in enumerate(sequences):
        print(f"{i+1}: {record.id} - {record.description}")
    return sequences

def Marco_de_lectura(ORF, sequence):
    """
    Toma una secuencia y un marco de lectura (ORF), y devuelve los codones correspondientes

    Args:
        ORF: Marco de lectura especificado (numero entre 1 y 6)
        sequence: La secuencia de ADN que se va a procesar

    Returns:
        Cadena de codones obtenidos del marco de lectura especificado
    """
    if ORF <= 3:
        start_index = (ORF - 1) % 3
    else:
        ORF = ORF - 3
        sequence = sequence[::-1]
        start_index = (ORF - 1) % 3
        
    codons = re.findall(r"(.{3})", str(sequence[start_index:]))
    codons_with_spaces = " ".join(codons)
    return codons_with_spaces

def main():
    if len(sys.argv) != 2:
        print("Uso: python select_sequence.py <archivo_entrada.fasta>")
        sys.exit(1)
    input_file = sys.argv[1]
    sequences = list_sequences(input_file)
    
    for sequence_record in sequences:
        sequence = sequence_record.seq
        sequence_id = sequence_record.id
        print(f"Procesando secuencia: {sequence_id}")
        
        # Crear un archivo para cada secuencia
        output_file = f"output_{sequence_id}.txt"
        with open(output_file, 'w') as f:
            for open_reading_frame in range(1, 7):
                codons = Marco_de_lectura(open_reading_frame, sequence)
                f.write(f"Marco de lectura {open_reading_frame}: {codons}\n")
        
        print(f"Resultados escritos en el archivo {output_file}")
    
    print("Procesamiento completo.")

main()

"""
## Salida

El programa proporcionara como salida un archivo de texto que contendra los codones extraidos de la secuencia de ADN segun el marco de lectura especificado por el usuario. El nombre de este archivo de salida dependera del marco de lectura seleccionado, y contendra los codones separados por espacios. Este archivo proporciona una representacion de los codones presentes en la secuencia de ADN seleccionada, lo que facilita su analisis y posterior procesamiento para estudios gen�ticos y biologicos.

## Metadatos y documentacion

Este README ofrece informacion de uso basico. Para obtener información más detallada sobre el diseno y la implementacion del script, consulte [Enlace a la documentacion].

## Codigo fuente

El codigo fuente esta disponible en este repositorio. Se acoge con satisfacción cualquier contribucion o sugerencia a través de solicitudes pull request.

## Terminos de uso

Este script esta disponible bajo la licencia Apache. Consulte el archivo LICENSE para obtener mas detalles.

## Como citar

Si utiliza este script en su trabajo, por favor cite: [informacion de citacian].

## Contactenos -=-

Si tiene problemas o preguntas, por favor abra un problema en este repositorio o pongase en contacto con nosotros en: [informacian de contacto].