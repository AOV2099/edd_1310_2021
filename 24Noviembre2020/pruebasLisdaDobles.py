from listas import DoubleLinkedList

ld = DoubleLinkedList()
print("Está vacia? -> ", ld.is_empty() )

ld.append(10)
ld.append(20)
ld.append(30)

print(f"Size -> {ld.getSize()}")

ld.transversal()
ld.reverse_transversal()

ld.remove_from_head(10)
ld.transversal()
ld.reverse_transversal()