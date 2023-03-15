class U20181049 :
        
    def __init__(self, nombre:str):
            self.nombre = nombre
                
    def tarea(self) -> str:
            pass
        
class lavarRopa(U20181049) :
    def tarea(self) -> str:
            return f"{self.nombre} esta lavando ropa" 
        
class tenderRopa(U20181049) :
    def tarea(self) -> str:
            return f"{self.nombre} esta tendiendo ropa" 
        

class recogerRopa(U20181049) :
    def tarea(self) -> str:
        return f"{self.nombre} esta recogiendo la ropa" 
        
lavarRopa1 = lavarRopa('ruben')
tenderRopa1 = tenderRopa('ruben')
recogerRopa1 = recogerRopa('ruben')

print(lavarRopa1.tarea())
print(tenderRopa1.tarea())
print(recogerRopa1.tarea())