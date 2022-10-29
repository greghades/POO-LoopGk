from pencil import Pencil
from interface_pencil import interface_pencil


class main_pencil():
    
    def __init__(self):
        self.opc = 1
        self.pen = Pencil("Azul",10,2,"Blanca")
        self.interPen = interface_pencil()
       
    def start(self):
        self.interPen.welcome()
        while(self.opc != 0):
            self.opc = self.interPen.menu()
            if(self.opc == 1):
                self.pen.write()
            elif(self.opc==2):
                self.pen.draw()
            elif(self.opc==3):
                self.pen.erase()

mainUser = main_pencil()
mainUser.start()