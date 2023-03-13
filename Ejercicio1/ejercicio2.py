class animal:
    pass
    def __init__(self,nombre,edad,raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza

    def ladrar(self):
            return 'el perro {} ladra y despierta media ciudad'.format(self.nombre)
    def miagar(self):
        return 'la gata {} bajo la lluvia esta mauyando en idioma {}'.format(self.nombre, self.raza)
    def pelear(self):
        return 'el gallo {} se agarro con otro en un combate, siendo ambos de la misma raza {}'.format(self.nombre, self.raza)
    def nadar(self):
        return '{} nada bastante tranquilo, fresco mi pana de {} años'.format(self.nombre, self.edad)   
       
perro = animal("chorizo", 3, "labrador")
gato = animal("isabelle",4,"angora")
gallo = animal("chicharron", 6, "malaya")
cocodrilo = animal("guapo", 7, "americano")

print(perro.ladrar())
print(gato.miagar())
print(gallo.pelear())
print(cocodrilo.nadar())
