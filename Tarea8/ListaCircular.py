
class Node:
    def __init__(self, value, next=None):
        self.next = next
        self.data = value

class CircularList():

    def __init__( self ):
        self.__currRef = None
        self.__size = 0

    def is_empty( self ):
        return self.__currRef == None
    
    def size( self ):
        print(f"Tamaño -> {self.__size}")

    def search (self, value ):
        curr_node = self.__currRef
        if self.__currRef != None:
            for i in range(self.__size):
                if curr_node.data == value:
                    return True
                curr_node = curr_node.next
        return False

    
    def insert_value( self, value ):
        if self.__currRef == None:
            self.__currRef = Node(value)

        elif self.search(value) == True:
            print("El valor ya se encuentra en la lista")
            self.__size -= 1

        elif value >= self.__currRef.data and self.__currRef.next == None:
            self.__currRef.next = Node(value,self.__currRef)
            self.__currRef = self.__currRef.next

        elif value >= self.__currRef.data:
            self.__currRef.next = Node(value,self.__currRef.next)
            self.__currRef = self.__currRef.next

        elif value <= self.__currRef.data and self.__currRef.next == None: 
            self.__currRef.next = Node(value,self.__currRef)

        elif value <= self.__currRef.next.data:
            self.__currRef.next = Node(value,self.__currRef.next)

        else:
            curr_node = self.__currRef.next
            while curr_node.data != self.__currRef.data:
                if value > curr_node.data and value < curr_node.next.data:
                    curr_node.next = Node(value,curr_node.next)
                curr_node = curr_node.next

        self.__size += 1
    
    def remove_value( self, value ):
        curr_node = self.__currRef
            
        if self.__currRef == None:
            print("No hay valores que remover")
        
        elif value == curr_node.data:
            print("Intentó borrar el nodo de referencia")
        else:
            
            while curr_node.next != None and curr_node.next != self.__currRef:
                if curr_node.next.data == value:
                    curr_node.next = curr_node.next.next
                    self.__size -= 1
                    return None
                else:
                    curr_node = curr_node.next

    
    def transversal( self ): #imprime
        if self.is_empty() :
            print("No hay valores en la lista")
        else:
            curr_node = self.__currRef.next
            while curr_node:
                print(f"{curr_node.data} -> ", end="")
                curr_node = curr_node.next
                if curr_node == self.__currRef:
                    print(f"{self.__currRef.data} -> ", end="")
                    print("")
                    break
    
    
            
    
    