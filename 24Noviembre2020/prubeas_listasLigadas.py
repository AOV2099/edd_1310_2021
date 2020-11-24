from listas import LinkedList

l = LinkedList()
print(f"l está vacía?, { l.is_empty() }")

l.append(10)
l.append(5) 
l.append(6)
l.append(20)
l.append(25)

print(f"l está vacía?, { l.is_empty() }")

l.transversal()
l.remove(10)
l.remove(6)
l.transversal()
l.preppend(0)
x = l.tail()
print( x )
l.transversal()
l.get(2)
