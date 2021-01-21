
class NodoArbol:
    def __init__( self, value, left=None, right=None ):
        self.data = value
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.__root = None

    
    def insert( self, val ):
        #regla 1
        if self.__root == None:
            self.__root = NodoArbol( val )   
        #regla 2
        else:
            self.__insert__( self.__root, val )

    
    def __insert__(self, nodo, val):
        if nodo.data == val:
            print("El dato ya existe")
        elif val < nodo.data:
            #regla 1:
            if nodo.left == None:
                nodo.left = NodoArbol( val )
            #regla 2:
            else:
                self.__insert__( nodo.left, val)
        else:
            if nodo.right == None:
                nodo.right = NodoArbol( val )
            else:
                self.__insert__( nodo.right, val )


    def __recorrido_in( self, nodo ):
        if nodo:
            self.__recorrido_in( nodo.left )
            print( nodo.data, end=", " )
            self.__recorrido_in( nodo.right  )


    def __recorrido_pos( self, nodo ):
        if nodo:
            self.__recorrido_pos(nodo.left)
            self.__recorrido_pos(nodo.right)
            print(nodo.data, end=", ")
    

    def __recorrido_pre( self, nodo ):
        if nodo:
            print(nodo.data, end=", ")
            self.__recorrido_pre(nodo.left)
            self.__recorrido_pre(nodo.right)

    
    def tranversal(self, format = "inorden"):
        if format == "inorden":
            print("Recorrido inorden:")
            self.__recorrido_in( self.__root )
            print("")

        elif format == "preorden":
            print("Recorrido preorden:")
            self.__recorrido_pre( self.__root )
            print("")

        elif format == "posorden":
            print("Recorrido posorden:")
            self.__recorrido_pos( self.__root )
            print("")

        else:
            print("Este orden no existe.")

    
    def search(self, value):
        if self.__root == None: #vacio?
            return None
        else: #caso base de recursividad
            return self.__search( self.__root, value )
            
    
    def __search(self, nodo, value):
        if nodo == None: #vacio?
            print("NO Encontrado")
            return None

        elif nodo.data == value: #caso base de recursividad
            print("Encontrado")
            return nodo

        elif value < nodo.data:
            return self.__search( nodo.left, value)

        elif value > nodo.data:
            return self.__search( nodo.right, value)
        
    
    def remove( self, value ):
        
        encontrado = self.search( value )

        if encontrado.left == None and encontrado.right == None:
            print(f"Eliminando { encontrado.data }")
            encontrado = None
        
        elif (encontrado.left != None and encontrado.right == None) or (encontrado.left == None and encontrado.right != None):
            print(f"A eliminar { encontrado.data }")





'''arbol = NodoArbol( "R", NodoArbol("C", None, None), NodoArbol("H", None, None) )
#print( arbol.left.data )
#print( arbol.right.data )
#print(arbol.data)

arbol2 = NodoArbol( "4" , (NodoArbol("3", NodoArbol("2", NodoArbol( "1" ) ) ) ) , ( NodoArbol("5") ) )

print(arbol2.data)
print(arbol2.left.data)
print(arbol2.left.left.data)
print(arbol2.left.left.left.data)'''