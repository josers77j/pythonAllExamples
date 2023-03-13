class banco:
    pass
    def __init__(self,transaccion, monto):
        self.transaccion=transaccion
        self.monto=monto

    def retiroDeEfectivo(self, cliente):
        return '{} {} ${} en efectivo del cajero metro'.format(cliente,self.transaccion, self.monto)
    
    def cargoDeEfectivo(self, cliente):
        return '{} {} ${} en efectivo a su tarjeta'.format(cliente, self.transaccion, self.monto)
    
empleado = banco("retiro",100.00)
empresa = banco("cargo",4000.00)

print(empleado.retiroDeEfectivo("juan"))
print(empresa.cargoDeEfectivo("lara"))