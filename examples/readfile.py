import argparse

parser = argparse.ArgumentParser(description="Lee archivo de entrada y salida")

# Agrega un argumento posicional para el archivo de entrada. 
parser.add_argument("input_file", type=str, 
			help="El archivo de texto que quieres procesar.")

# Agrega un argumento opcional para el archivo de salida.
# 'out.txt' como nombre de archivo por defecto.
parser.add_argument("--output", type=str, default="out.txt",
                    help="El archivo donde se guarda la salida. 'out.txt' por defecto.")
args = parser.parse_args()

print("Archivo de entrada: ", args.input_file)
print("Archivo de salida: ", args.output)
