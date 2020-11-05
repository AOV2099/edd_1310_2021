class Array:
    def __init__( self, tam ):
        self.__info = [ None for x in range (tam) ]

    def get_item( self, position):
        try:
            dato = self.__info[ position ]

        except Exception as e:
            dato = (f"Error de posición: {e}")

        return dato
    
    def set_item( self , dato, position):
        try:
            self.__info[ position ] = dato

        except Exception as e:
             print(f"Error : {e}")
    
    def get_length( self ):
        return len( self.__info )
    
    def clear( self, dato):
        self.__info = [ dato for x in range (len(self.__info	)) ]

    def __iter__( self ):
        return IteradorArreglo( self.__info )
    


class IteradorArreglo:
    def __init__( self, arr ):
        self.__arr = arr
        self.__indice = 0
    
    def __iter__( self ):
        return self
    
    def __next__( self ):
        if self.__indice < len(self.__arr):
            dato = self.__arr[self.__indice]
            self.__indice += 1
            return dato
        else:
            raise StopIteration
    



