class Humano:
    pass
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def hablar(self):
            return 'mi nombre es {} y tengo {} años'.format(self.nombre, self.edad)
    def correr(self, distancia):
        return 'el atleta {} corre a una distancia de {}'.format(self.nombre, distancia)
        # def hablar(self):
persona = Humano("jose", 23)


print(persona.correr('20 km/h'))