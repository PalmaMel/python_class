'''
calculate_codon_count.py:  Script para calcular el numero de apariciones de un codon

Este script lee una secuencia de ADN desde un archivo dado y recibe desde linea de comandos 
el codon que se desea contar sus apariciones, de este codon se van a ir contando las
apariciones en la secuencia. La secuencia de ADN debe estar en un archivo de texto y solo 
contener los caracteres 'A', 'C', 'G' y 'T', no acepta 'N'


uso: 
    python calculate_codon_count.py <path_to_dna_file> AAA
argumentos: 
    <path_to_dna_file> : Ruta al archivo de texto que contiene la secuencia de ADN.
    AAA codon del cual se quiere obtener numero de apariciones

'''


import argparse
from dna_analysis.operations.codon_count import calculate_codon_count
from dna_analysis.utils.file_io import read_dna_sequence

def main():
    parser = argparse.ArgumentParser(description="Calcula la frecuencia de un codon en una secuencia de ADN." )
    parser.add_argument("file", type=str, help="Archivo de ADN del cual leer la secuencia.")
    parser.add_argument("codon", type=str, help="Codon para calcular su frecuencia en la secuencia de ADN.")
    
    args = parser.parse_args()
    file_path = args.file
    codon = args.codon.upper()
    
    try:
        # Leer la secuencia del archivo especificado utilizando la función proporcionada por file_io.py
        sequence = read_dna_sequence(file_path)
        # contar aparicion del codon proporcionado 
        codon_count =  calculate_codon_count(sequence,codon)
        # Mostrar el resultado al usuario
        print(f"El numero de apariciones del {codon} en la secuencia es: {codon_count:.2f}%")
    except Exception as e:
        print(f"Error: {str(e)}")