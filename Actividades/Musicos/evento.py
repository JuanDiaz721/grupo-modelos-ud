class evento:
    def __init__(self):
        self.name = input("Dígite nombre del evento: ")
        self.date = input("Dígite fecha del evento: ")
        self.agrupaciones = [banda]

    def organizar(self):
        print(f"El evento {self.name} se llevará a cabo el {self.date} y contará con las siguientes agrupaciones:")
        for banda in self.agrupaciones:
            print(f" - {banda.name} con los siguientes integrantes: ")
            for musico in banda.integrantes:
                print(f" - {musico.name}")

class banda:
    def __init__(self):
        self.name = input("Dígite nombre de la agrupación: ")
        self.integrantes = [musicos]

    def ensayar(self):
        print(f"La banda {self.name} está ensayando con los siguientes integrantes: ")
        for musico in self.integtegrantes:
            print(f" - {musico.name}")

    def tocarVivo(self):
        print(f"La banda {self.name} está tocando en vivo")
        if self.ensayar():
            print("La banda está tocando con éxito")
        else:
            print("La banda no está tocando con éxito")
class musicos:
    def __init__(self):
        self.name = input("Dígite nombre del músico: ")
        self.instrumento = [input("Dígite instrumento del músico: ")]
    
    def interpretar(self):
        print(f"El músico {self.name} está interpretando su instrumento(s): {self.instrumento}")

class instrumento:
    def sonar(self):
        print("El instrumento está sonando")

class guitarra(instrumento):
    def sonar(self):
        print("La guitarra está sonando")

class bajo(instrumento):
    def sonar(self):
        print("El bajo está sonando")

class bateria(instrumento):
    def sonar(self):
        print("La batería está sonando")

class voz(instrumento):
    def sonar(self):
        print("La voz está sonando")