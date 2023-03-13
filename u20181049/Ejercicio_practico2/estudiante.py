class estudiante  :
    pass
    def __init__(self,nombre,apellido) :
        self.nombre = nombre
        self.apellido = apellido
    def mostrarInfo(self,m1,m2,m3,m4,m5) :
        return '{} {} cursa las materias {}, {}, {}, {} y {}'.format(self.nombre,self.apellido,m1,m2,m3,m4,m5)

alumno = estudiante('rudeus', 'greyrat')
    