import argparse

parser = argparse.ArgumentParser()
parser.add_argument("x", type=int, nargs="+")
args = parser.parse_args()

print(sum(args.x))
