import argparse
from re import sub
from turtle import update

class Usuario:
    def __init__(self,nombre,saldo):

        self.nombre = nombre
        self.saldo = saldo

    def ingreso(self,ingreso):

        self.saldo += ingreso

    def gasto(self,gasto):

        self.saldo -= gasto

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
    budget_parser.add_argument("amount", help="valor del nuevo presupuesto")

    update_parser = subparser.add_parser("update", help= "modifica un gasto")
    update_parser.add_argument("id", help= "id del gasto a modificar")

parser = comandos_parser()


def expense_tracker(user : Usuario):

    print("Expense tracker")
    print("-"*20)

    print("Cuenta : " + user.nombre)



cuantaMov = {}
user = Usuario("Gabriel",10000)

expense_tracker(user)