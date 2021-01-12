class ColaConPrioridad:
    def __init__(self):
        self.__data = list()

    def is_empty(self):
        return len(self.__data) == 0
    
    def to_str(self): 
        print("             ⛵⛵⛵    <----Botes salvavidas")
        print(' ------------------------------------------------')
        for item in self.__data:
            print(f'\t| \t{item}    \t|')
            print( ' ------------------------------------------------')
        print("               🚢    <----Barco hundiéndose")
        print('\n')
        

    def isEmpty(self): 
        return len(self.__data) == 0
  
    def enqueue(self, prioridad, elem, entrada = 0): 
        #self.__data.append( [prioridad, elem, entrada] ) 
        if len(self.__data) ==  0:
            self.__data.append( [prioridad, elem, entrada] ) 
            
        else:
            if  elem not in self.__data:
                for i in self.__data:
                    if prioridad == i[0]:
                        entrada += 1
                self.__data.append( [prioridad, elem, entrada] )

            self.__data = sorted(self.__data, key = lambda x: (x[0], x[2])) #Ordena tomando dos parametros
    
    def dequeue(self): 
        if not self.is_empty():
            print("Pasajero evacuado exitosamente")
            return self.__data.pop(0)
            
        else:
            print("Ningun pasajero a bordo")
            return None
    def length(self):
        return len(self.__data)



