class usuario :
    pass
    def __init__(self, user,password,status):
        self.user = user
        self.password = password
        self.status = status
    
    def inicioSesion(self,nombre_Empleado,tipo_Rol) :
      return 'El empleado {} ha iniciado sesion con su usuario {} de rol tipo {}'.format(nombre_Empleado,self.user,tipo_Rol)        
    
sesion = usuario('mc123','contraseña','activo')