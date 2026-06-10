class Cuenta:
    def __init__(self,saldo,categoria):
        self.saldo = saldo
        self.categoria= categoria

    def ingreso(self,ingreso):

        self.saldo += ingreso

    def gasto(self,gasto):

        self.saldo -= gasto

    
