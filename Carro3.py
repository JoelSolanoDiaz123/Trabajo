import time
class Auto:
    Color = ""
    Modelo = ""
    Llantas = 0
    Puertas = 0
    Velocidades = 0
    def Mostar_Datos(self):
        print("color:", self.Color)    
        print("Modelo: ", self.Modelo)
        print("Llantas: ",self.Llantas)
        print("Puertas: ",self.Puertas)
        print("Velocidades: ",self.Velocidades)
    def encender(self):
        print("El auto se encendio")

    def apagar(self):
        print("el auto se apago")

    def Acelerar(self, Velocidad):     
        for  j in range(0,Velocidad,5):
            print("El auto va a una velocidad de" ,j, " Km/h")
            time.sleep(0.5)
        print("el auto llego a una velocidad de" , Velocidad, "Km\h")
       
    def Frenar(self,Velocidad,frenado):
        for j in range(Velocidad,frenado,-5):
             f = int(input("¿Desea seguir frenando?: "))
             if f == 1:    
                 print("El auto eva a una velocidad de: ",j,"Km/h")
                 time.sleep(0.5)           
             else:
                 print("El auto llego a una velocidad de ",j,"Km/h")
                 time.sleep(0.5)
                 break
                       
Carro = Auto()
Carro.Color = "Azul"
Carro.Modelo = "Mazda"
Carro.Llantas = 4
Carro.Puertas = 4
Carro.Velocidades = 5
Carro.Mostar_Datos()
Carro.encender()
Carro.Acelerar(65)
Carro.Frenar(65,0)
Carro.apagar()
