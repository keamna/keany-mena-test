class Perro:

    def __init__(self, nombre, raza, color):
        self.nombre = nombre 
        self.raza = raza
        self.color = color

    def mostrarAtributos(self):
        print("Nombre:",self.nombre)
        print("Raza:",self.raza)
        print("Color:",self.color)
        

perro1 = Perro("Koffee", "Salchicha", "Café")
perro2 = Perro("Balú", "Salchicha", "Negro con manchas blancas")
perro1.mostrarAtributos()
perro2.mostrarAtributos()





