class menu :
    
    def __init__(self, comida):
        self.comida = comida
        
    pl1 = 'hamburguesas con papas' 
    pl2 = 'tacos de birria'
    pl3 = 'nachos'
    pl4 ='bebidas de industria la constancia'
    
n_comida = menu('comida')
    
class cliente(menu) :
    pass
    
    def __init__(self,nombre) :
        self.nombre = nombre
    
    def pedirComida(self) :
        return '{} ha pedido {} y {}'.format(self.nombre, self.pl1,self.pl3)     

    def mostrarMenu(self) :
        return 'hola {}, el menu contiene {}, {}, {} y {}'.format(self.nombre,self.pl1,self.pl2,self.pl3,self.pl4,self.)
    
client = cliente('oscar')    

print(client.mostrarMenu())        
print(client.pedirComida())        

class cocina(cliente) :
    empleado = 'cocinero'
    pass
    def prepararPedido(self) :
        return 'El {} esta preparando {} y {} para {}'.format(self.empleado,self.pl1,self.pl3, self.nombre)
    
    def entregarPedido(self) :
        return 'El {} entrega el pedido de {} y {} al cliente {}'.format(self.empleado,self.pl1,self.pl3, self.nombre)
cocinando = cocina(client.nombre)

print(cocinando.prepararPedido())
print(cocinando.entregarPedido())