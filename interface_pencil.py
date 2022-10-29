class interface_pencil():

    def welcome(self):
         print("""
        █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
        █░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
        █░░║║║╠─║─║─║║║║║╠─░░█
        █░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
        █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
        
        """)

    def menu(self):
       
        print("1 = Escribir\n")
        print("2 = Dibujar\n")
        print("3 = Borrar\n")
        print("0 = Salir\n")
        opc = int(input("Opcion: "))

        return opc