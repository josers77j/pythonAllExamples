from abc import ABC, abstractmethod

class Ruben :
        
    def __init__(self, nombre:str):
            self.nombre = nombre
            
            
    @abstractmethod
    def tarea(self) -> str:
            pass
        
class lavarRopa(Ruben) :
    def tarea(self) -> str:
            return f"{self.nombre} esta lavando ropa" 
        
class tenderRopa(Ruben) :
    def tarea(self) -> str:
            return f"{self.nombre} esta tendiendo ropa" 
        

class recogerRopa(Ruben) :
    def tarea(self) -> str:
        return f"{self.nombre} esta recogiendo la ropa" 
        
lavarRopa1 = lavarRopa('ruben')
tenderRopa1 = tenderRopa('ruben')
recogerRopa1 = recogerRopa('ruben')

print(lavarRopa1.tarea())
print(tenderRopa1.tarea())
print(recogerRopa1.tarea())