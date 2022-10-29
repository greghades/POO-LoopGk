class Ice_Cream:
    colour = ""
    flavour = ""

    def __init__(self, colour, flavour):
        self.colour = colour
        self.flavour = flavour

    @property #getter
    def colour(self): 
        return self.size

    @colour.setter #setter
    def colour(self, new_colour):
        self.colour = new_colour

    @property
    def flavour(self):
        return self.flavour

    @flavour.setter
    def flavour(self, new_flavour):
        self.flavour = new_flavour

    def melt(self):
        print("El helado se derritió.")

    def freeze(self):
        print("El helado se congeló.")

    def __str__(self):
        string_object = f"Color: {self.colour}\nSabor: {self.flavour}"
    
        