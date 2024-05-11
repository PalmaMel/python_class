'''
codon_frecuency.py: Modulo para contar la frecuencua de determindo codon en una secuencia de DNA 

Este módulo proporciona funciones diseñadas específicamente para determinar el número de apariciones de un 
codón en una secuencia de ADN. Esta capacidad es invaluable en estudios genéticos, ya que permite analizar 
con precisión la frecuencia de ocurrencia de codones particulares, lo que a su vez puede proporcionar 
información crucial sobre la función y la expresión génica.

Funciones: 
calculate_codon_count: Devuelve numero de apariciones del codon


'''
def calculate_codon_count (sequence,codon):
    # Validación básica de la secuencia
    if not sequence:
        raise ValueError("La secuencia proporcionada está vacía.")

    sequence = sequence.upper()
    if any(c not in 'ACGT' for c in sequence):
        raise ValueError("La secuencia contiene caracteres no válidos.")
    
    if len(codon) != 3:
        raise ValueError("Error: El codon debe tener una longitud de 3 bases.")
    if not all(base in "ACGT" for base in codon):
        raise ValueError ("Error: El codon solo puede contener las bases A, C, G o T.")
    else: 
        count = sequence.count(codon)
        '''total_bases = len(sequence)
        frequency = (count / (total_bases/3)) * 100
        return frequency'''
        return count

if __name__ == "__main__":
    test_sequence = "GTACGTACGTA"
    codon = 'GTA'
    codoncount = calculate_codon_count(test_sequence, codon)
    print(f"Aparición del codón en la secuencia de prueba: {codoncount:.2f}")
