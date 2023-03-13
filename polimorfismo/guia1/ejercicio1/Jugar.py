class Jugar :
    def __init__(self, tipoJugador) :
        self.tipoJugador = tipoJugador
        
jugador1 = Jugar('tryhard')
jugador2 = Jugar('speedrunner')

#realice el ejercicio de ambas formas por si acaso
#tanto dentro de la propia clase padre, como haciendo los import heredando    
class Dopa(Jugar) :
    nombre = 'dopa'
    pass
    def jugarJuego() :
        return 'Todo {} el {} en el metal gear solid'.format(jugador1.tipoJugador,n_player.nombre)
    
class Boba(Jugar) :
    nombre = 'boba'
    pass
    def jugarJuego() :
        return 'toda {} la {} en el metal gear solid'.format(jugador2.tipoJugador,n_player.nombre)
    
n_player = Dopa
print(n_player.jugarJuego())    
n_player = Boba
print(n_player.jugarJuego())   