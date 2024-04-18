import argparse

parser = argparse.ArgumentParser(description='Ejemplo de argumento booleano en argparse.')
parser.add_argument('--flag', '-f', action='store_true',
                    help='Activa el flag')

args = parser.parse_args()

if args.flag:
    print('Flag activado')
else:
    print('Flag no activado')

