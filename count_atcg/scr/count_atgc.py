import sys

# Verifica que se haya proporcionado el nombre del archivo como argumento
if len(sys.argv) < 2:
    print("Uso: python programa.py nombre_del_archivo [nucleotidos]")
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
