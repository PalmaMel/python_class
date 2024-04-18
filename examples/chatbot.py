import argparse
import random

parser = argparse.ArgumentParser(description="¡Hablemos! Pídele al chatbot que cuente un chiste o que te salude")

# Añadir los argumentos
parser.add_argument("-c", "--chiste", action='store_true',
                    help="Pide al chatbot que cuente un chiste.")
parser.add_argument("--nombre", type=str,
                    help="Dile tu nombre al chatbot.")
args = parser.parse_args()

chistes = ["¿Por qué no se puede confiar en los átomos? ¡Porque hacen todo a las espaldas!",
           "¿Qué le dice un bit al otro? Nos vemos en el bus",
           "¿Cómo saluda un informático? ¡HOLA MUNDO!"]

def chat(args):
    if args.nombre:
        print(f"¡Hola, {args.nombre}! ¿Cómo estás?")
    if args.chiste:
        print(random.choice(chistes))

chat(args)
