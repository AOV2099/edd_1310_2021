from colasNoCota import ColaConPrioridad


cola = ColaConPrioridad() 
cola.enqueue(4, "Maestre") 
cola.enqueue(2, "Niños") 
cola.enqueue(4, "Mecánico") 
cola.enqueue(3, 'Onvres') 
cola.enqueue(4, "Vigia") 
cola.enqueue(5, "Capitán") 
cola.enqueue(4, "Timonél")
cola.enqueue(3, "Mujeres")
cola.enqueue(2, "viejos")
cola.enqueue(3, "Envraz")
cola.enqueue(1, "Niñas")    
print("Grupos de pasajeros por evacuar = ", cola.length() )
cola.to_str()     

cola.dequeue() #sacar niñas
cola.dequeue() #sacar niños
print("Grupos de pasajeros por evacuar = ", cola.length() )
cola.to_str()    

    