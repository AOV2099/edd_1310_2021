class Nodo():
    def __init__( self, value, siguiente = None ):
        self.data = value #Falta Encapsulamiento
        self.siguiente = siguiente 

class LinkedList:
    def __init__( self ):
        self.__head = None

    def is_empty( self ):
        return self.__head == None

    def append( self, value ):
        nuevo = Nodo( value )
        if self.__head == None: #self is empty
            self.__head = nuevo
        else:
            curr_node = self.__head
            while curr_node.siguiente != None:
                curr_node = curr_node.siguiente
            curr_node.siguiente = nuevo

    def remove( self, value ):
        curr_node=self.__head

        if self.__head.data == value:
            self.__head = self.__head.siguiente
        
        else:
            curr_anterior = None
            while curr_node.data != value and curr_node.siguiente != None:
                curr_anterior=curr_node
                curr_node= curr_node.siguiente
        
            if curr_node.data == value:
                curr_anterior.siguiente= curr_anterior.siguiente.siguiente 
            else:
                print("El dato no existe en la lista")
            
    
    def  transversal ( self ):
        curr_node = self.__head
        while curr_node != None:
            print(f"{curr_node.data} -> ", end="")
            curr_node = curr_node.siguiente
        print("")

    def preppend(self, value):
        nuevo = Nodo( value, self.__head)
        self.__head = nuevo
        

    def tail(self):
        curr_node = self.__head
        while curr_node.siguiente != None:
            curr_node= curr_node.siguiente

        return(curr_node.data)
    
    def get(self, posicion = None):
        contador = 0
        curr_node = self.__head
        dato = "No existe dato en esta posición"
        
        while(curr_node):
            if(contador == posicion):
                dato = curr_node.data
            contador += 1
            curr_node = curr_node.siguiente

        print(f"El dato en la posición {posicion} es {dato}")


class NodoDoble():

    def __init__( self, data, prev = None, next = None):
        self.next = next
        self.prev = prev
        self.data = data

class DoubleLinkedList:

    def __init__(self):
        self.__head = ( NodoDoble(None)) 
        self.__tail = ( NodoDoble(None)) 
        self.__size = 0
    
    def getSize(self):
        return self.__size
    
    def is_empty(self):
        return self.__size == 0

    def append( self, val ):

        if self.is_empty():
            nuevo = NodoDoble(val)
            self.__head = nuevo
            self.__tail = nuevo
        else:
            nuevo = NodoDoble(val, self.__tail, None)
            self.__tail.next = nuevo
            self.__tail = nuevo 

        self.__size += 1
    
    def transversal( self ):
        curr_node = self.__head
        while curr_node != None:
            print(f" <- {curr_node.data} -> ", end="")
            curr_node = curr_node.next
        print("")

    def reverse_transversal( self ):
        curr_node = self.__tail
        while curr_node != None:
            print(f" <- {curr_node.data} -> ", end="")
            curr_node = curr_node.prev
        print("")

    def remove_from_head( self, value ):

        curr_node = self.__head   

        if self.__head.data == value:
            self.__head = self.__head.next
            self.__head.prev = None

        elif self.__tail.data == value:
            self.__tail.prev.next = None 
            self.__tail = self.__tail.prev

        elif self.__head.data != value and self.__tail.data != value:
              
            while curr_node.data != value and curr_node.next != None:
        
                curr_node = curr_node.next
            
            if curr_node.data == value:
                curr_node.prev.next = curr_node.next
                curr_node.next.prev = curr_node.prev
            else:
                print("El dato no existe en la lista")
            
            curr_node.next = None
            curr_node.prev = None
        self.__size -= 1
        
        

