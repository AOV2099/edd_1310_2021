from arboles_binarios import BinarySearchTree

abb = BinarySearchTree()
abb.insert(50)
abb.insert(30)
abb.insert(60)
abb.insert(15)
abb.insert(23)
abb.insert(110)
abb.insert(90)
abb.insert(120)
abb.insert(100)
abb.insert(55)
abb.insert(58)
abb.insert(115)

abb.tranversal()
#abb.tranversal("preorden")
#abb.tranversal("posorden")

#res = abb.search(30)
#print(f"El resultado es => {res.data}")

abb.remove(90)
abb.tranversal()