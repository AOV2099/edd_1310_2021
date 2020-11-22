
class D_Node :
    def __init__( self, data, next = None, prev = None):
        self.next = next
        self.prev = prev
        self.data = data

class DoubleLinkedList:

    def __init__(self):
        self.__head = None 
        self.__tail = None
        self.__size = 0
	
    def is_empty( self ):
        return self.__head == None


    def append( self, val ):
        nuevo = D_Node( val )
        if self.__head == None: 
            self.__head = nuevo
            self.__tail = None
        else:
            curr_node = self.__head

            while curr_node.next != None:
                curr_node = curr_node.next
                
            curr_node.next = nuevo
            self.__tail = nuevo
            self.__tail.prev = curr_node
    
		
    def transversal( self ):
        curr_node = self.__head
        while curr_node != None:
            print(f"{curr_node.data} <-> ", end="")
            curr_node = curr_node.next
        print("")


    def reverse_transversal( self ):

        curr_node = self.__tail
        while curr_node != None:
            print(f"{curr_node.data} <-> ", end="")
            curr_node = curr_node.prev
        print("")


    def get_size( self ):
        curr_node = self.__head
        while curr_node != None:
            self.__size += 1 
            curr_node = curr_node.next
        return self.__size


    def find_from_head( self, value ): #find by value, not by index
        curr_node = self.__head
        index = 0
        dato = "No existe dato en la lista"

        if curr_node.data == value:
            dato = f"El valor suministrado({value}) se encuentra en la posición [{ index }] de Head-Tail"
        
        else:
            while(curr_node != None):
                if( curr_node.data == value):
                    dato = index
                    dato = f"El valor suministrado({value}) se encuentra en la posición [{ index }] de Head-Tail"
                index += 1
                curr_node = curr_node.next
        print(dato)
    

    def find_from_tail( self, value ): 
        curr_node = self.__tail
        index = 0
        dato = "No existe dato en la lista"

        if curr_node.data == value:
            dato = f"El valor suministrado({value}) se encuentra en la posición [{ index }] de Tail-Head"
        
        else:
            while(curr_node != None):
                if( curr_node.data == value):
                    dato = index
                    dato = f"El valor suministrado({value}) se encuentra en la posición [{ index }] de Tail-Head"
                index += 1
                curr_node = curr_node.prev
        print(dato)


    def remove_from_head( self, value ):
        curr_node = self.__head
        index = 0

        print(f"Eliminado el valor [{value}]...")
        
        if self.__head.data == value:
            self.__head = self.__head.next
            self.__head.prev = None

        elif self.__tail.data == value:
            self.__tail.prev.next = None 
            self.__tail = self.__tail.prev #nuevo head = 9
            
   
        elif self.__head.data != value and self.__tail.data != value:
            curr_anterior = None
            while curr_node.data != value and curr_node.next != None:

                curr_anterior = curr_node
                curr_node = curr_node.next
                index += 1

            if curr_node.data == value:
                curr_anterior.next = curr_anterior.next.next
                (curr_anterior.next).prev = curr_node.prev
                #
            else:
                print("El dato no existe en la lista")
        
        


    def remove_from_tail( self, value ):
        
        curr_node = self.__tail
        index = 0

        print(f"Eliminado el valor [{value}]...")

        if self.__tail.data == value:
            self.__tail = self.__tail.prev
            self.__tail.next = None


        elif self.__head.data == value:
            self.__head.next.prev = None #
            self.__head = self.__head.next #nuevo head = 2
            
            
        elif self.__tail.data != value and self.__head.data != value: 
            curr_anterior = None
            while curr_node.data != value and curr_node.prev != None:
                curr_anterior = curr_node
                curr_node = curr_node.prev
                index += 1

            if curr_node.data == value:
                curr_anterior.prev = curr_anterior.prev.prev
                (curr_anterior.prev).next = curr_node.next
                #print("Pos reversa " + str(index) )
            else:
                print("El dato no existe en la lista")

        


        




  