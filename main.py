import argparse
import json
from pathlib import Path
import shlex

from pydantic import BaseModel

class Cuenta(BaseModel):

    saldo: int
    nuevoSaldo: int
    descOperacion: str
    valorMovimiento: int

ARCHIVO = "registro.json"

def cargar_movimientos():

    if not Path(ARCHIVO).exists():

        return []

    with open(ARCHIVO,"w") as f :

        movimientos = json.load(f)

    return [Cuenta(**d) for d in movimientos]


def guardar_movimientos():

    registro = [mov.model_dump() for mov in movimientos]

    with open(ARCHIVO, "w") as f:
        json.dump(registro, f, indent= 2, default=str)


movimientos = cargar_movimientos()

def comandos_parser():

    parser = argparse.ArgumentParser(prog="expense-tracker")
    subparser = parser.add_subparsers(dest= "comando")

    #expense-tracker add --description "lunch" --amount 20
    addd_parser = subparser.add_parser("add", help= "agrega un nuevo gasto")
    addd_parser.add_argument("--description", help= "describir el gasto")
    addd_parser.add_argument("--amount", help= "valor total del gasto")

    list_parser = subparser.add_parser("list", help= "lista los gastos")
    list_parser.add_argument("--category", help= "filtra por categoria")

    summary_parser = subparser.add_parser("summary",help= "total de gastos")
    summary_parser.add_argument("--month",help="gastos de un mes especifico")

    del_parser = subparser.add_parser("delete", help= "elimina un gasto")
    del_parser.add_argument("id", help= "id del gasto a eliminar")

    budget_parser = subparser.add_parser("budget", help= "presupuesto mensual")
    budget_parser.add_argument("--new", help="actualiza el presupuesto mensual")
    budget_parser.add_argument("--amount", help="valor del nuevo presupuesto")

    update_parser = subparser.add_parser("update", help= "modifica un gasto")
    update_parser.add_argument("id", help= "id del gasto a modificar")

    return parser

parser = comandos_parser()

def guardar_movimientos():

    print("a")

def expense_tracker():

    print("Expense tracker")
    print("-"*20)

    while True:

        entrada = input("$ expense-tracker ")

        partes = shlex.split(entrada)
        args = parser.parse_args(partes)

        if args.comando == "add":
            print("a")
        elif args.comando == "list":
            print("b")
        elif args.comando == "summary":
            print("c")
        elif args.comando == "delete":
            print("d")
        elif args.comando == "budget":
            print("e")
        elif args.comando == "update":
            print("f")


cuentaMov = {}


expense_tracker()