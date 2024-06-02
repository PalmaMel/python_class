'''
Title
    Reading_Frame.py
Author
    Palma Luna Melissa   
Arguments
    posicionales:
        archivo_entrada.fasta
Usage
    Python select_sequence.py <archivo_entrada.fasta>

'''
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
