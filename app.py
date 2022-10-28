class Pencil():
    def __init__(self,color,size,width,eraser):
        self.color = color
        self.size = size
        self.width = width
        self.eraser = eraser
    
    def __str__(self):
        return f"Lapiz Color: {self.color} de tamaño: {self.size}cm con una anchura de {self.width}cm y un borrador {self.eraser}"
    

    def write(self):
        words = []
        opc = True
        while(opc):
            word = input("Que desea escribir?: ")
            words.append(word)
            print("Lista de palabras\n")
            for w in words:
                print(w+"\n")
            opc = int(input("Desea agragar otra palabra?\nSI=1\nNO=0\nOpcion:"))

pencil1 = Pencil("Azul",10,2,"Blanco")
print(pencil1)
pencil1.write()