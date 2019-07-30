import time
class Auto:
    Color = ""
    Numero = 0
    Llantas = 0
    Puertas = 0
    def Mostar_Datos(self):
        print("color:", self.Color)    
        print("Numero de avion: ", self.Numero)
        print("Llantas: ",self.Llantas)
        print("Puertas: ",self.Puertas)
    def Preguntar (self, Vel):
        print("Autorizacion para el despegue")
        for S in range(0,Vel,10):
            print("El avion va a velocidad crucero", S,"Km/h")
            time.sleep(2)    
        print("El avion va a velocidad crucero rumbo a la pista: ",S,"Km/h")
    def Llegada(self, Vel, Mas):
        print(" _______Bajar los flaps a 3________ ")
        print("_______________________________________________________")
        print("los flaps han bajado a " "3")
        print("___________________________________________________")
        print("Aumentar la velocidad a 180 Km/h")
        print("_______________________________________________________")
        for D in range(Vel,Mas,10):
            print("El avion aumenta la velocidad a:",D,"Km/h")
            time.sleep(0.8)
        print("El avion acendio")     
    
    def Preguntas(self):
        a = int(input("Desea subir los flaps a 0, Si no lo hace el avion seguira subiendo. 1 para si, 2 Para no: ")) 
        if a == 1:
            print("Los flaps Bajaron a 0")
        else:
            print("!El avion seguira subiendo!!!!!!!!!!!!")   
            print("Error")       
    def Pre2 (self):
        e = int(input("Desea subir los trenes de aterrizaje. 1 para si, 2 para no: "))     
        if e == 1:
            print("____________________________________")
            print("Los trenes de aterrizaje subieron") 
        else:
            print("Usted no ha subido los trenes de aterrizaje")
            print("Error") 
            Avion.Caer()
    def Caer(self):
        print("El avion callo por exeso de Errores")             

Avion = Auto()
Avion.Color = "Blanco"
Avion.Numero = 956713
Avion.Llantas = 6
Avion.Puertas = 2
Avion.Mostar_Datos()
Avion.Preguntar(50)
Avion.Llegada(40,190)
Avion.Preguntas()
Avion.Pre2()