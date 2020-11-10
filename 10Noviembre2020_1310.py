class Nodo:

    def __init__(self,dato):
        self.__dato = dato
        self.__siguiente = None

    def get_dato(self): #Regresa el dato
        return self.__dato

    def set_dato(self,d):
        self.__dato = d 

    def get_siguiente(self):
        return self.__siguiente

    def set_siguiente(self,d):
        self.__siguiente = d
        
    def set_siguiente(self,d):
        self.__siguiente = d

    def to_String(self):
        return (" | " + str(self.__dato) + " | " + str(self.__siguiente) + " | -->")

    def show( self ):
        curr_node = self # Head
        print(" Inicio de la estructura ligada:")
        print("|" + str(curr_node.get_dato() ) + "| -->" , end ="" )

        while( curr_node.get_siguiente() != None ):
            curr_node = curr_node.get_siguiente()
            print("|" + str(curr_node.get_dato() ) + "| -->" , end ="" )

        print("\nFin")


# Ejemplo 1
a = Nodo( 10 )
a.show()

# ejemplo 2
a.set_siguiente( Nodo(20) )
a.show()

# ejemplo 3
a.get_siguiente().set_siguiente( Nodo(30) )
a.show()

# ejemplo 4
a.get_siguiente().get_siguiente().set_siguiente( Nodo(40) )
a.show()

# ejemplo 5
a.get_siguiente().get_siguiente().get_siguiente().set_siguiente( Nodo(50) )
a.show()


#cambiando valores 

# ejemplo 6: cambiar 10 por 12
a.set_dato( 12 )
a.show()

# ejemplo 7: cambiar 40 por 46
a.get_siguiente().get_siguiente().get_siguiente().set_dato(46)
a.show()

# ejemplo 8: cambiar 20 por 25
a.get_siguiente().set_dato(25)
a.show()

a.get_siguiente().get_siguiente().set_dato( None )
a.show()