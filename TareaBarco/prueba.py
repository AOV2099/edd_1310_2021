from colas import Queue,BoundedPriorityQueue

q1= Queue()
q1.enqueue(3)
q1.enqueue(33)
q1.enqueue(23)
print(q1.to_string())

print ("Prueba 2 de Queue")
c1={"id": 1,"nombre": "Mario", "balance": 20.5}
c2={"id": 2,"nombre": "Diana", "balance": 3456.5}
c3={"id": 3,"nombre": "Bartolo", "balance": 1000000.0}

atencion= Queue()
atencion.enqueue(c1)
atencion.enqueue(c2)
atencion.enqueue(c3)
print(atencion.to_string())
siguiente= atencion.dequeue()
print(f"Bienvenido Sr.{siguiente['nombre']}, en que podemos servirle el dia de hoy")
print(atencion.to_string())
print("")

print("Pruebas de las colas con prioridad acotada")
maestres = {"prioridad":4 , "descripción":"Maestres","persona":["juan P","Andres P"]}
niños = {"prioridad":2 , "descripción":"Niños","personas":["Santi H","Ángel H"]}
mecanicos = {"prioridad":4 , "descripción":"Mecánicos","persona":["Raul L","Carlos M"]}
mujeres = {"prioridad":3 , "descripción":"Mujeres","personas":["Lupe L","Carla M","Susan R"]}
tercera_edad = {"prioridad":2 , "descripción":"3ra edad","personas":["Rodrigo L","Juana W"]}
ninas = {"prioridad":1 , "descripción":"Niñas","personas":["Lila F","Mari G"]}
hombres = {"prioridad":3 , "descripción":"Hombres","personas":["Victor K","Jorge G"]}
vigia = {"prioridad":4 , "descripción":"Vigia","persona":"Jorge H"}
capitan = {"prioridad":5 , "descripción":"Capitan","persona":"Arturo G"}
timonel = {"prioridad":4 , "descripción":"Timonel","persona":"Carlos R"}

cpa = BoundedPriorityQueue(7)
cpa.enqueue(maestres['prioridad'], maestres)
cpa.enqueue(niños['prioridad'], niños)
cpa.enqueue(mecanicos['prioridad'], mecanicos)
cpa.enqueue(mujeres['prioridad'], mujeres)
cpa.enqueue(tercera_edad['prioridad'], tercera_edad)
cpa.enqueue(ninas['prioridad'], ninas)
cpa.enqueue(hombres['prioridad'], hombres)
cpa.enqueue(vigia['prioridad'], vigia)
cpa.enqueue(capitan['prioridad'], capitan)
cpa.enqueue(timonel['prioridad'], timonel)
print("")
cpa.to_string()
print("")
cpa.dequeue()
cpa.dequeue()
cpa.dequeue()
cpa.dequeue()
cpa.dequeue()
cpa.dequeue()
cpa.dequeue()
cpa.dequeue()
cpa.dequeue()
cpa.dequeue()
cpa.dequeue()
print("")
cpa.to_string()
