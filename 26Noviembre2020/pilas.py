class Stack:
    def __init__(self):
        self.__data = list()
    
    def isEmpty( self ):
        return len(self.__data) == 0
    
    def lenght(self):
        return len(self.__data)
    
    def pop(self):
        try:
            return self.__data.pop()
        except:
            return "Pila vacía"

    def push(self, value):
        self.__data.append(value)
    
    def peek(self):
        return self.__data[ len(self.__data) - 1 ]
    
    def toString(self):
        for item in self.__data[::-1]:
            print("-------")
            print(f" | {item} | ")
        print("-------")


    
