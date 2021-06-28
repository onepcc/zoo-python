#  Cada animal debe tener al menos un nombre, una edad, un nivel de salud y un nivel de felicidad. 
# La clase Animal debe tener un método display_info que muestre el nombre, la salud y la felicidad del animal. 
# También debe tener un método de alimentación que aumente la salud y la felicidad en 10.

class Animal:
    def __init__(self, nombre,edad,salud =50,felicidad=50):
        
        self.nombre = nombre
        self.edad = edad
        self.salud = salud
        self.felicidad = felicidad

    def info(self):
        print(f"""
        Animal: {self.__class__.__name__} 
        Nombre: {self.nombre.upper()} 
        Edad: {self.edad}
        Salud: {self.salud}
        Felicidad {self.felicidad}""")
        return self
    
    def comer(self):
        if self.salud < 100:
            self.salud+= 10
            self.felicidad+= 10
        print(f"""Animal {self.nombre} ha comido ahora salud y felicidad aumento a: {self.felicidad}""")
        return self
    
    def ruido(self):
        raise NotImplementedError

# Comience creando una clase Animal y luego al menos 3 clases específicas de animales que hereden de Animal.
# En al menos una de las clases de Animal child que ha creado, agregue al menos un atributo único. 
# Dele a cada animal diferentes niveles predeterminados de salud y felicidad. 
# Los animales también deben responder al método de alimentación con diferentes niveles de cambios en la salud y la felicidad.


        




