# Reading Frame 
Este script 
## Uso
El usuario puede utilizar el script proporcionando el nombre del archivo que contiene las secuencias de ADN en formato FASTA como argumento al ejecutar el programa desde la linea de comandos.

"""
    python script.py secuencias.fasta
"""
Una vez ejecutado el programa, seguirá las instrucciones proporcionadas por la interfaz de usuario para seleccionar una secuencia especifica y elegir un marco de lectura. Despues de completar estos pasos, el programa procesara la secuencia seleccionada y guardara los resultados en un archivo de salida con un nombre que refleja el marco de lectura elegido.
"""
import sys
import Bio.Seq
import re
from Bio.Seq import Seq
from Bio import SeqIO

def list_sequences(input_file): 
    """ Lee un archivo FASTA y lista todas las secuencias contenidas
    Args: 
        input_file: Ruta del archivo FASTA que contiene las secuencias
    Returns:
        lista de todas las secuencias leidas
    """
    sequences = list(SeqIO.parse(input_file, "fasta"))
    for i, record in enumerate(sequences):
        print(f"{i+1}: {record.id} - {record.description}")
    return sequences

def get_selected_sequence(sequences, index): 
    """selecciona una secuencia especifica de una lista de secuencias

    Args:
        sequences: Lista de secuencias leidas del archivo FASTA
        index: Indice de la secuencia que se desea seleccionar (basado en el indice mostrado al usuario)

    Returns:
        Secuencia (atributo seq) en la posicion 'index' de la lista de secuencias.
    """
    return sequences[index].seq

def Marco_de_lectura(ORF, sequence, output_file):
    """
    Toma una secuencia y un marco de lectura (ORF), y escribe los codones correspondientes en un archivo de salida

    Args:
        ORF: Marco de lectura especificado (número entre 1 y 6)
        sequence: La secuencia de ADN que se va a procesar
        output_file:  Ruta del archivo donde se escribiran los resultados
    Returns:
        Codones en el archivo de salida, separados por espacios
    """
    with open(output_file, 'w') as f:
        if ORF <= 3:
            # Calcular el indice de inicio segun el marco de lectura
            start_index = (ORF - 1) % 3
            
            # Extraer los codones dentro del rango del marco de lectura
            codons = re.findall(r"(.{3})", str(sequence[start_index:]))
            
            # Imprimir los codones separados por espacios
            codons_with_spaces = " ".join(codons)
            f.write(codons_with_spaces + "\n")
        else:
            ORF = ORF - 3
            sequence = sequence[::-1]
            print (sequence)
            # Calcular el indice de inicio segun el marco de lectura
            start_index = (ORF - 1) % 3
            
            # Extraer los codones dentro del rango del marco de lectura
            codons = re.findall(r"(.{3})", str(sequence[start_index:]))
            
            # Imprimir los codones separados por espacios
            codons_with_spaces = " ".join(codons)
            f.write(codons_with_spaces + "\n")

def main():
    if len(sys.argv) != 2:
        print("Uso: python select_sequence.py <archivo_entrada.fasta>")
        sys.exit(1)
    input_file = sys.argv[1]
    sequences = list_sequences(input_file)
    index = int(input("Introduce cual secuencia quieres usar: ")) - 1
    sequence = Bio.Seq.Seq (get_selected_sequence(sequences, index))
    print(f"Secuencia seleccionada:\n{sequence}")
    open_reading_frame = int(input("Inserte que marco de lectura quiere: "))
    if (open_reading_frame > 6) or (open_reading_frame < 1): # comprobar rango del marco de lectura
        print ("Marco de lectura invalido")
        sys.exit(1)
    output_file = f"output_frame_seq{index+1}_{open_reading_frame}.txt"
    Marco_de_lectura(open_reading_frame, sequence, output_file)
    print ("--------------------Results--------------------------")
    print(f"Codones escritos en el archivo: {output_file}")
    print ("Se recomienda cambiar el nombre del archivo a uno mas significativo")
main()
"""
## Salida

El programa proporcionara como salida un archivo de texto que contendra los codones extraidos de la secuencia de ADN segun el marco de lectura especificado por el usuario. El nombre de este archivo de salida dependera del marco de lectura seleccionado, y contendra los codones separados por espacios. Este archivo proporciona una representacion de los codones presentes en la secuencia de ADN seleccionada, lo que facilita su analisis y posterior procesamiento para estudios genéticos y biologicos.

## Metadatos y documentacion

Este README ofrece informacion de uso basico. Para obtener informaciÃ³n mÃ¡s detallada sobre el diseno y la implementacion del script, consulte [Enlace a la documentacion].

## Codigo fuente

El codigo fuente esta disponible en este repositorio. Se acoge con satisfacciÃ³n cualquier contribucion o sugerencia a travÃ©s de solicitudes pull request.

## Terminos de uso

Este script esta disponible bajo la licencia Apache. Consulte el archivo LICENSE para obtener mas detalles.

## Como citar

Si utiliza este script en su trabajo, por favor cite: [informacion de citacian].

## Contactenos -=-

Si tiene problemas o preguntas, por favor abra un problema en este repositorio o pongase en contacto con nosotros en: [informacian de contacto].