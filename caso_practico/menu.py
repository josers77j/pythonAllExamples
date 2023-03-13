class restaurante():
    pass
    def __init__(self, comida, bebida):
      self.comida = comida
      self.bebida = bebida
      
menu1 = restaurante('hamburger', 'nachos')

class pedidos(restaurante) :
    pass
    def __init__(self, cliente):
        self.cliente = cliente
    pass
    def vercliente(self) :
        return 'hola {} tu comida es {} con {}'.format(self.cliente,self.comida, self.bebida)

cliente = pedidos('nombre')

print(cliente.vercliente)
