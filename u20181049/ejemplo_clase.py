class App :
    pass
    def __init__(self,nombre_cancion):
        self.nombre_cancion = nombre_cancion
        
rolita = App('zero to hero')

class Cliente : 
    pass
    def __init__(self,nombre,deporte):
        self.nombre = nombre
        self.deporte = deporte
    def accion(self, cancion):
        return '{} hace el deporte de {} y escucha la cancion {}'.format(self.nombre,self.deporte, cancion)
    
persona = Cliente('jose', 'artes marciales mixtas')
print(persona.accion(rolita.nombre_cancion))
    