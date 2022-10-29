class Key:
    size = ""
    colour = ""

    def __init__(self, size, colour):
        self.size = size
        self.colour = size

    @property
    def size(self): # getter 
        return self.size

    @size.setter # setter 
    def size(self, new_size):
        self.size = new_size

    @property # getter
    def colour(self):
        return self.colour

    @size.setter # setter
    def colour(self, new_colour):
        self.colour = new_colour

    def open(self):
        print("La puerta se abrió.")

    def close(self):
        print("La puerta se cerró.")

    def __str__(self):
        string_object = f"Tamaño: {self.size}\nColor: {self.colour}"

  