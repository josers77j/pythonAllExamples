from Estudiante import Estudiante
from Estudiante import estudiante1
from Estudiante import estudiante2
from Estudiante import estudiante3
class Asistencia(Estudiante) :
    pass
    def __init__(self, estado,fecha):
        self.estado = estado
        self.fecha = fecha
    
    def marcarAsistencia(self) :
        return 'La asistencia del estudiante {} con carnet {} fue {} el dia {}'.format(nombreEstudiante,codigoEstudiante,self.estado,self.fecha)
    
nombreEstudiante = estudiante1.nombre
codigoEstudiante = estudiante1.codigo

tipoAsistencia = Asistencia('presente','05/09/2023')

print(tipoAsistencia.marcarAsistencia())

 
nombreEstudiante = estudiante2.nombre
codigoEstudiante = estudiante2.codigo

tipoAsistencia = Asistencia('ausente','05/09/2023')

print(tipoAsistencia.marcarAsistencia())

 
nombreEstudiante = estudiante3.nombre
codigoEstudiante = estudiante3.codigo

tipoAsistencia = Asistencia('justificada','05/09/2023')

print(tipoAsistencia.marcarAsistencia())