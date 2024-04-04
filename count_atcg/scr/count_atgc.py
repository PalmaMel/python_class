# Abre el archivo en modo lectura
with open('archivo.txt', 'r') as file:
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

# Imprime el resultado
print(f'El símbolo A aparece {count_A} veces.')
print(f'El símbolo C aparece {count_C} veces.')
print(f'El símbolo G aparece {count_G} veces.')
print(f'El símbolo T aparece {count_T} veces.')



