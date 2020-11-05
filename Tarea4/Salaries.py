from Worker import Worker
from arrays import Array

class Salaries():

    def __init__ ( self, file ):
        with open( file, 'r' ) as txt:
            rows = txt.readlines()
            rows = [ r.replace(' ','').strip().split(',') for r in rows ]
            rows.remove(rows[0])
        self.__workers = Array( len(rows) )    
        
        for row in range( self.__workers.get_length() ):
            self.__workers.set_item( (Worker (rows[row][0], rows[row][1], rows[row][2], rows[row][3], rows[row][4], rows[row][5], rows[row][6])) , row )
    
    def get_final_salary_byID( self, id ):
        for employee in range( self.__workers.get_length() ):
            if(self.__workers.get_item(employee).get_id() == id):
                name = self.__workers.get_item(employee).get_name()
                res = self.__workers.get_item(employee).get_final_salary()
                print (f"Nombre-> {name} , Sueldo final -> {res}")

    def get_final_salaries( self ):
        for employee in range( self.__workers.get_length() ):
            name = self.__workers.get_item(employee).get_name()
            res = self.__workers.get_item(employee).get_final_salary()
            print (f"Nombre-> {name} , Sueldo final -> {res}")
     
    def get_empleado_mas_antiguo(self):
        antiguedad_e = self.__workers.get_item(0).get_antiguedad() 
        empleado = None

        for employee in range( self.__workers.get_length() ):
            if self.__workers.get_item(employee).get_antiguedad() > antiguedad_e: 
                antiguedad_e = self.__workers.get_item(employee).get_antiguedad() 
                empleado = self.__workers.get_item(employee)
            
        return(f"Empleado más antiguo-> {empleado.to_string()}Años de antiguedad -> {antiguedad_e}")
    
    def get_empleado_mas_nuevo(self):
        antiguedad_e = self.__workers.get_item(0).get_antiguedad() 
        empleado = None

        for employee in range( self.__workers.get_length() ):
            if self.__workers.get_item(employee).get_antiguedad() < antiguedad_e:
                antiguedad_e = self.__workers.get_item(employee).get_antiguedad() 
                empleado = self.__workers.get_item(employee)
            
        return(f"Empleado más nuevo-> {empleado.to_string()}Años de antiguedad -> {antiguedad_e}")
