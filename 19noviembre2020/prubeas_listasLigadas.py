from listas import LinkedList

l = LinkedList()
print(f"l está vacía?, { l.is_empty() }")

l.append(10)
l.append(5) 
l.append(6)
l.append(20)

print(f"l está vacía?, { l.is_empty() }")

l.transversal()
l.remove(10)
l.transversal()
l.preppend(0)
x = l.tail()
print( x )
l.transversal()
