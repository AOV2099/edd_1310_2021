from stack import Stack

def DeleteMidPointStack( stack , pos = 1 ):
    const = round( (stack.lenght() + pos) / 2) 
    
    if pos != const:
        newStack = stack
        lastVal = stack.peek()
        newStack.pop()
        DeleteMidPointStack( newStack, pos = pos + 1 )
        newStack.push(lastVal)
    else:
        print( f"Valor en medio de la pila -> {stack.peek()}" )
        stack.pop()


def mainStack():
    pila = Stack()
    pila.push("1")
    pila.push("2")
    pila.push("3")
    pila.push("4") # <- Medio
    pila.push("5")
    pila.push("6")
    pila.push("7")
 
    print("-------- PILA ORIGINAL --------")   
    pila.to_string()

    DeleteMidPointStack( pila )
    print("-------- PILA MODIFICADA --------")
    pila.to_string()
    

mainStack()