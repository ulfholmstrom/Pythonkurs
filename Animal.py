
# coding: utf-8

# In[ ]:

class Dog:
    '''
    Detta är en klass som skapar en instans av en hund
    petname = Namn på hunden
    temp = Temparatur på hunden
    
    '''
    
    # Initialisation of the object, state of object
    def __init__(self, petname, temp):
        self.name = petname
        self.temperature = temp
    
    # Get status
    def status(self):
        print("dog name is ", self.name)
        print("dog temperature is ", self.temperature)
        
    # Set temperature - a method
    def setTemperature(self, temp):
        self.temperature = temp
        
    # Hunden kan skälla - en metod
    
    def bark(self):
        print('Woof!!!')

