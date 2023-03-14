from Karaoke import Karaoke, rolita2

class Cantante2(Karaoke) :
    cantante = 'chepe'
    pass
    def cantarRolita() :
        return '{} esta cantando {} a todo pulmon'.format(n_cantante.cantante,rolita2.cancion)
    
n_cantante = Cantante2
print(n_cantante.cantarRolita())

