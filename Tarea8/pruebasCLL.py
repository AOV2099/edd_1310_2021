from ListaCircular import *

cll = CircularList()

print(cll.is_empty())
print(cll.search(0))

cll.insert_value(5)
cll.insert_value(4)
cll.insert_value(1)
cll.insert_value(3)
cll.insert_value(2)
cll.insert_value(6)
cll.insert_value(6) #el valor ya se encuentra en la lista

cll.transversal()
cll.size()
cll.remove_value(1)
cll.remove_value(2)
cll.remove_value(3)
cll.insert_value(7)
cll.transversal()

print(cll.search(7))

cll.remove_value(1)
cll.size()
print(cll.is_empty())