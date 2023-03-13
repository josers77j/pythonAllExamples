class Loteria :
    pass
    def __init__(self, figura1, figura2, figura3):
      self.figura1 = figura1
      self.figura2 = figura2
      self.figura3 = figura3


    def funcionamiento(self,cliente):
        if figura.figura1 == 'estrella' and figura.figura2 == 'estrella' and figura.figura3 == 'estrella':
            return '{} has obtenido un premio de $600'.format(cliente)
        elif figura.figura1 == 'estrella' and figura.figura2 == 'pera' and figura.figura3 == 'pera':   
            return '{} has obtenido un premio de $100'.format(cliente)
        elif figura.figura1 == 'manzana' and figura.figura2 == 'manzana' and figura.figura3 == 'pera':   
            return '{} has obtenido un premio de $300'.format(cliente)
        elif figura.figura1 == 'manzana' and figura.figura2 == 'manzana' and figura.figura3 == 'manzana':   
            return '{} has obtenido un premio de $400'.format(cliente)
        elif figura.figura1 == 'pera' and figura.figura2 == 'pera' and figura.figura3 == 'pera':   
            return '{} has obtenido un premio de $400'.format(cliente)    
        else:
            print('salimos peor :c')
          
figura = Loteria('estrella','estrella','estrella')

