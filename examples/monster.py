import argparse

# Crear el argparse object
parser = argparse.ArgumentParser(description="¡Crea una criatura a partir de un segmento de ADN!")

# Añadir los argumentos
parser.add_argument('DNA', type=str, help="El segmento de ADN que servirá de base para la criatura.")
parser.add_argument("-m", "--monster", action='store_true',
                    help="Usa este switch si quieres que la criatura sea un monstruo.")

args = parser.parse_args()

# Diccionario para "traducir" el ADN
dna_to_trait = {
    "A": "Tiene alas.",
    "T": "Tiene escamas.",
    "C": "Puede cambiar de color.",
    "G": "Puede brillar en la oscuridad."
}

def create_creature(dna, monster):
    creature_traits = []

    for base in dna:
        if base in dna_to_trait:
            trait = dna_to_trait[base]
            creature_traits.append(trait)

    if monster:
        creature_traits.append("Tiene colmillos grandes y afilados.")

    creature_traits_str = " ".join(creature_traits)
    print("Tu criatura:", creature_traits_str)

create_creature(args.DNA, args.monster)
