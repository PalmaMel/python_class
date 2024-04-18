import argparse

parser = argparse.ArgumentParser(description='Ejemplo de argparse con una lista de valores permitidos.')
parser.add_argument('--color', choices=['red', 'green', 'blue'],
                    help='Elige tu color preferido')

args = parser.parse_args()

print('Tu color preferido es:', args.color)
