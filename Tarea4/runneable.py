from Salaries import *
from Worker import *

data = Salaries("Tarea4\junio.dat")
print("SALARIOS:")
data.get_final_salaries()
print("--------------------------")
print("SALARIO BY ID:")
data.get_final_salary_byID("2345")
print("--------------------------")
print(data.get_empleado_mas_antiguo())
print("--------------------------")
print(data.get_empleado_mas_nuevo())

#print ( data.to_string() )
#print( data.get_salary( 2345 ) )
