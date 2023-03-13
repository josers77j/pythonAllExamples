class paciente :
    pass
    def __init__(self, nombre,edad,estatura,peso):
        self.nombre = nombre
        self.edad = edad
        self.estatura = estatura
        self.peso = peso

    def reportePaciente(self,nombre,edad,estatura,peso):
        return 'el paciente {} con la edad de {} y estatura de {} metros,con un peso de {} libras, presenta un padecimiento de {} {} con las siguientes observaciones {}'.format(nombre,edad,estatura,peso,self.padecimiento,self.riesgo,self.observaciones)



class examenes(paciente) :
    pass
    def __init__(self,nombre,edad,estatura,peso,padecimiento,riesgo,observaciones):
        super().__init__(nombre,edad,estatura,peso)
        self.padecimiento = padecimiento     
        self.riesgo = riesgo
        self.observaciones = observaciones
    
    
n_reporte = examenes('valeria', 25, 1.49,101,'catarro','extremo','padecimiento de tos y gripe hace ya 15 dias')

print(n_reporte.reportePaciente(n_reporte.nombre,n_reporte.edad,n_reporte.estatura,n_reporte.peso))