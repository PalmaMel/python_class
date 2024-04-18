import argparse

parser = argparse.ArgumentParser(description="Te encuentras con un dragon... ¿Qué deberías hacer?")
parser.add_argument("name", type=str, default="valiente desconocido",
                    help="Coloca tu nombre de héroe.")
parser.add_argument("-a", "--action", type=str, choices=["fight", "run"], required=True,
                    help="Decide tu acción. ¿Vas a luchar (fight) o huir (run)?")
args = parser.parse_args()

if args.action == "fight":
    print(f"{args.name} saca su espada y decide luchar...")
    print("Después de una batalla épica, {args.name} emerge victorioso!")
else:
    print(f"{args.name} decide que la discreción es mejor que el valor y decide huir rápidamente!")
    print("Escapas, pero el dragón todavía reina supremo...")
