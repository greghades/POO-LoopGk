import random
from assets.draws.draws import drawing
from assets.words.words import words

class Pencil():

    def __init__(self,color,size,width,eraser):
        self.color = color
        self.size = size
        self.width = width
        self.eraser = eraser
    
    def __str__(self):
        return f"Lapiz Color: {self.color} de tamaño: {self.size}cm con una anchura de {self.width}cm y un borrador {self.eraser}"
    

    def write(self):
       
        n = random.randint(0,5)
        print(words[n])
           
    def draw(self): 
        n = random.randint(0,4)
        print(drawing[n])

    def erase(self):
        eraser = """
                                                                       
                                          &&@&#                       
                                       #&@    ,&&                     
                                     @&,         &&(                  
                                  (&&              *&&                
                                &&*                   &&(             
                             #&&                        *&&           
                           @&*                           &&,          
                        (&&&&                         #&&             
                      &&/    &&(                    &&*               
                    &&         *&&               (&@                  
                   &&             @&(          &&*                    
               *    &&              /&&     (&@                       
                &&   *&&               &&/&&*                         
                  &&%   @&/            /&&                            
                          /&&        @&/                              
           *********         &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%   
        
        """
        print(eraser)
