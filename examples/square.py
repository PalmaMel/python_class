import argparse

parser = argparse.ArgumentParser()
parser.add_argument("x", type=int, help="El número entero a elevar al cuadrado")
args = parser.parse_args()

print(args.x ** 2)
