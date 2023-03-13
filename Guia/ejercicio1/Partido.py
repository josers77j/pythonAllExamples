from Banca import Banca
from Banca import jugador1
from Banca import jugador2
from Banca import jugador3
class Partido(Banca) :
    pass
    def __init__(self, posicion):
      self.posicion = posicion
      
    def cambioDeJugador(self) :
        return 'El jugador {} con el numero {} juega de {}'.format(nombreJugador,numeroJugador,self.posicion)

new_Posicion = Partido('delantero')    
nombreJugador = jugador1.nombre
numeroJugador = jugador1.numero

print(new_Posicion.cambioDeJugador())
    
new_Posicion = Partido('defensa')    
nombreJugador = jugador2.nombre
numeroJugador = jugador2.numero

print(new_Posicion.cambioDeJugador())

new_Posicion = Partido('volante')    
nombreJugador = jugador3.nombre
numeroJugador = jugador3.numero

print(new_Posicion.cambioDeJugador())
