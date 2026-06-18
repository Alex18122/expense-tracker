import argparse

class Usuario:
    def __init__(self,nombre,saldo):

        self.nombre = nombre
        self.saldo = saldo

    def ingreso(self,ingreso):

        self.saldo += ingreso

    def gasto(self,gasto):

        self.saldo -= gasto

def comandos_parser():

    parser = argparse.ArgumentParser(prog="Expense")

def expense_tracker(user : Usuario):

    print("Expense tracker")
    print("-"*20)

    print("Cuenta : " + user.nombre)



cuantaMov = {}
user = Usuario("Gabriel",10000)

expense_tracker(user)