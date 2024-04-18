import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--x", type=int, default=2, help="El número base")
args = parser.parse_args()

print(args.x ** 2)
