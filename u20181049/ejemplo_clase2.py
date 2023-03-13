class Producto :
    pass
    def __init__(self,nombre,color,precio):
        self.nombre = nombre
        self.color = color
        self.precio = precio

    def verProducto(self, categoria):
        return 'el producto {} color {} de la categoria {} tiene el precio de {}'.format(self.nombre,self.color,categoria,self.precio)    
    
producto1 = Producto('xbox series s','blanco',299)
