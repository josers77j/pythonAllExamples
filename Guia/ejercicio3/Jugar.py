from Loteria import Loteria
class Jugar(Loteria):
    pass
    def __init__(self, cliente):
      self.cliente = cliente
      
    def iniciarJuego(self) :
        return '{} ha introducido una moneda y ha comenzado el juego'.format(self.cliente)
    def detenerGiro(self) :
        return '*********** la maquina a dejado de girar *************'
    
n_cliente = Jugar('chabelo')

print(n_cliente.iniciarJuego())
print(n_cliente.detenerGiro()) 
# como tal la herencia esta en el metodo, ya que la maquina es la que decide que items son los que deben aparecer, no el cliente
print(n_cliente.funcionamiento(n_cliente.cliente))   
