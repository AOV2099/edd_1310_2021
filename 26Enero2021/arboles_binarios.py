
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
        
    
    #def remove( self, value ):
        
     #   encontrado = self.search( value )

      #  if encontrado.left == None and encontrado.right == None:
          #  print(f"Eliminando { encontrado.data }")
         #   encontrado = None
        
       # elif (encontrado.left != None and encontrado.right == None) or (encontrado.left == None and encontrado.right != None):
        #    print(f"A eliminar { encontrado.data }")


    def remove( self, value ):
        
        if self.__root == None:
            print('Nada que eliminar')
        else:
            self.__remove( None, None, self.__root, value )
    
    def __remove( self, padre_hi, padre_hd, actual, value ):
        if actual == None:
            print("Caso Base")
            return None
        
        elif actual.data == value:
            print("Encontrado: ", actual.data)

            #caso 1: Hoja
            if actual.left == None and actual.right == None:
                if padre_hi != None:
                    padre_hi.letf = None
                else:
                    padre_hd.right = None
            #caso 2: Con los 2 hijos 
            if( actual.left != None and actual.right == None ) or (actual.left == None and actual.right != None):
                print("Es un nodo con un hijo")
                if actual.left != None:
                    actual.data = actual.left.data
                    actual.left = None
                else:
                    actual.data = actual.right.data
                    actual.right = None
            #caso3: Con los dos hijos 50,60,110
            #return actual

        elif value < actual.data:
            print("Buscar a la izquierda")
            self.__remove( actual, None, actual.left, value )
        else: 
            print("Buscar a la derecha")
            self.__remove( None, actual, actual.right, value )


'''arbol = NodoArbol( "R", NodoArbol("C", None, None), NodoArbol("H", None, None) )
#print( arbol.left.data )
#print( arbol.right.data )
#print(arbol.data)

arbol2 = NodoArbol( "4" , (NodoArbol("3", NodoArbol("2", NodoArbol( "1" ) ) ) ) , ( NodoArbol("5") ) )

print(arbol2.data)
print(arbol2.left.data)
print(arbol2.left.left.data)
print(arbol2.left.left.left.data)'''