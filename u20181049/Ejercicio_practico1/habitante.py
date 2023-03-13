class habitante : 
    pass
    def __init__(self, nombre,apellido,edad,carrera):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.carrera = carrera
        
    def mostrarInformacion(self,nombre_Colonia, numero_Casa) : 
            return '{} {} tiene {} años, es un estudiante de {} y vive en la {} casa #{}'.format(self.nombre,self.apellido,self.edad,self.carrera,nombre_Colonia,numero_Casa)
        
persona = habitante('joel','perez',22,'lic en ciencias juridicas')