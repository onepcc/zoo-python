from animal import Animal

class Perro(Animal):
    def __init__(self, nombre,rasgo,edad,salud =50,felicidad=50):
        super().__init__(nombre,edad,salud =salud,felicidad=felicidad)
        self.rasgo = rasgo
    
    def comer(self):
        if self.salud < 100:
            self.salud+= 20
            self.felicidad+= 20
        print(f"El {self.__class__.__name__} {self.nombre.upper()} ha comido ahora salud y felicidad aumento a: {self.felicidad}")
        return self
    
    def ruido(self):
        print(f"El {self.__class__.__name__} {self.nombre.upper()} hace {self.rasgo*3}")
        return self

    def __str__(self):
        """ Informacion del animal """
        return f"El {self.__class__.__name__} puede 'comer' y hacer 'ruido' "