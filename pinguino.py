from animal import Animal

class Pinguino(Animal):
    def __init__(self, nombre,edad,nadar="nadar",salud =60,felicidad=80):
        super().__init__(nombre,edad,salud =salud,felicidad=felicidad)
        self.rasgo = nadar
    
    def __str__(self):
        """ Informacion del pinguino """
        return "El pinguino puede 'comer' y 'slide' "
    

    def comer(self):
        if self.salud < 100:
            self.salud+= 25
            self.felicidad+= 25
        print(f"El {self.__class__.__name__} {self.nombre.upper()} ha comido ahora salud y felicidad aumento a: {self.felicidad}")
        return self
    
    def slide(self):
        if self.felicidad < 100:
            self.salud+= 5
            self.felicidad+= 35
        print(f"El {self.__class__.__name__} {self.nombre.upper()} aumento felicidad a: {self.felicidad} luego de {self.rasgo}")
        return self
    