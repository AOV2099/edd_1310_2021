from dlListasV1 import *

dllist = DoubleLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.append(5)
dllist.append(6)
dllist.append(7)
dllist.append(8)
dllist.append(9)
dllist.append(10)


print(f"Is Empty -> {dllist.is_empty()}")
print(f"Size -> {dllist.get_size()}")

dllist.transversal()
dllist.reverse_transversal()

print("")

dllist.find_from_head( 4 )
dllist.find_from_tail( 4 )

print("")

dllist.remove_from_head(5)
dllist.remove_from_tail(7)

dllist.remove_from_head(1)
dllist.remove_from_tail(10)

dllist.transversal()
dllist.reverse_transversal()




