from animal import Animal

class Gato(Animal):
    def __init__(self, nombre,edad,vidas=7,salud =50,felicidad=50):
        super().__init__(nombre,edad,salud =salud,felicidad=felicidad)
        self.rasgo = vidas
    
    def comer(self):
        if self.salud < 100:
            self.salud+= 8
            self.felicidad+= 8
        print(f"El {self.__class__.__name__} {self.nombre.upper()} ha comido ahora salud y felicidad aumento a: {self.felicidad}")
        return self
    
    def accidente(self):
        self.rasgo-=1
        print(f"El {self.__class__.__name__} {self.nombre.upper()} le quedan {self.rasgo} vidas")
        return self

    def __str__(self):
        """ Informacion del animal """
        return f"El {self.__class__.__name__} puede 'comer' y tener 'accidente' "