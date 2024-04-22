'''

Arguments
    posicionales:
        nombre_archivo
    opcionales
        [nucleotidos]

Usage
    Python count_atcg.py nombre_del_archivo [nucleotidos]
    
'''
import sys

# Verifica que se haya proporcionado el nombre del archivo como argumento
if len(sys.argv) < 2: #  lista con todos los argumentos pasados por línea de comandos, verifica dos arg
    print("Uso: Python count_atcg.py nombre_del_archivo [nucleotidos]")
    sys.exit(1)

nombre_archivo = sys.argv[1] # Guarda el elemento de la lista de sys.argv que es el nomb del archivo
try:
    # Abre el archivo en modo lectura
    with open(nombre_archivo, 'r') as file:
        # Lee la cadena de ADN del archivo
        dna_sequence = file.read() #  almacena la cadena leida del archivo

        # Verifica si el archivo está vacío
        if not dna_sequence.strip(): # elimina espacios en blanco al principio y al final de una cadena de caracteres
            # Se aplica primero .strip y despues se confirma si esta vacia
            print(f"ErrorFileEmpty: Sorry, the file '{nombre_archivo}' is empty")
            sys.exit(1)

        # Verifica si el archivo contiene caracteres no válidos (verifica es DNA)
        invalid_characters = set(dna_sequence) - {'A', 'C', 'G', 'T'} # resta ATCG a la secuencia
        if invalid_characters: # si no esta vacia manda el error
            print(f"ErrorInvalidChar: The file '{nombre_archivo}' contains invalid characters: {', '.join(invalid_characters)}")
            sys.exit(1)

except FileNotFoundError: # Mensaje de error cuando no se encuentre el archivo
    print(f"ErrorFileNotFound: Sorry, couldn´t find the file: '{nombre_archivo}'")
    sys.exit(1)
finally:
    print("Thanks for using my code! If used correctly, you should see the answer after this message")

# En caso de estar a minusculas los nucleotidos se pasan a mayusculas
#  Se obtienen los argumentos (nucleótidos) pasados después del nombre del archivo 
nucleotidos_especificos = set(arg.upper() for arg in sys.argv[2:]) if len(sys.argv) > 2 else {'A', 'C', 'G', 'T'}

# Si se proporcionaron argumentos de nucleótidos inválidos, mostrar un mensaje de error y salir
nucleotidos_invalidos = set(arg.upper() for arg in sys.argv[2:]) - {'A', 'C', 'G', 'T'} # resta ATCG al input
if nucleotidos_invalidos:
    print(f"ErrorInvalidArg: invalid base argument: {', '.join(nucleotidos_invalidos)}")
    sys.exit(1)

# Inicializa contadores para cada símbolo
count_A = 0
count_C = 0
count_G = 0
count_T = 0

# Itera sobre la cadena de DNA y cuenta las ocurrencias de cada símbolo
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
        print(f'La base {nucleotido} aparece {count} veces.')
else:
    print(f'La base A aparece {count_A} veces.')
    print(f'La base C aparece {count_C} veces.')
    print(f'La base G aparece {count_G} veces.')
    print(f'La base T aparece {count_T} veces.')