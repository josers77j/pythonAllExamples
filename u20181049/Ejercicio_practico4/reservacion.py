class reservacion :
    pass
    def __init__(self,id_reserva,fecha_reserva,seguro_devolucion,numero_acompañantes ,estatus) :
        self.id_reserva = id_reserva
        self.fecha_reserva = fecha_reserva
        self.seguro_devolucion = seguro_devolucion
        self.numero_acompañantes = numero_acompañantes
        self.estatus = estatus
        
    def mostrarReserva(self,nombre_Cliente,numero_Mesa,usuario):
        return 'cliente {} realizo una reserva para la fecha {} la cual tiene un seguro de devolucion {}, y cuenta con {} acompañantes para la mesa {} y quien atendio esta reservacion fue el usuario {}'.format(nombre_Cliente,self.fecha_reserva,self.seguro_devolucion,self.numero_acompañantes,numero_Mesa,usuario )
        
n_Reservacion = reservacion('R500','08/06/2023',1,5,1)
        # 1 = activo, 0 = inactivo
        #seguro de devolucion y estatus se manjena con booleanos