class Worker:
    def __init__( self, id, name, p_lastname, m_lastname, extra_hours, base_salary, contract_year ):
        self.__id = id
        self.__name = name
        self.__p_lastname = p_lastname
        self.__m_lastname = m_lastname
        self.__extra_hours = extra_hours
        self.__base_salaray = base_salary
        self.__contract = contract_year
        self.__antiguedad = 2020 - int(contract_year)

    def to_string( self ):
        return (f"""
        ID -> {self.__id}, 
        Name -> {self.__name}, 
        Apellidos -> {self.__p_lastname} {self.__m_lastname}, 
        Horas Extras -> {self.__extra_hours}, 
        Salario Base -> {self.__base_salaray},
        Año de contratación -> {self.__contract}
        """)

    #getters & setters
    def set_id ( self, id):
        self.__id = id
    def get_id ( self ):
        return self.__id 


    def set_name ( self, name):
        self.__name = name
    def get_name ( self ):
        return self.__name 

    
    def set_p_lastname ( self, p_lastname):
        self.__p_lastname = p_lastname
    def get_p_lastname ( self ):
        return self.__p_lastname


    def set_m_lastname ( self, m_lastname):
        self.__m_lastname = m_lastname
    def get_m_lastname ( self ):
        return self.__m_lastname

    
    def set_extra_hours ( self, extra_hours):
        self.__extra_hours = extra_hours
    def get_extra_hours ( self ):
        return int(self.__extra_hours)
    
    
    def set_base_salary ( self, base_salary):
        self.__base_salaray = base_salary
    def get_base_salary ( self ):
        return int(self.__base_salaray)
    
    def set_contract_year ( self, contract_year ):
        self.__contract = contract_year
    def get_contract_year ( self ):
        return self.__contract

    def get_antiguedad(self):
        return self.__antiguedad
    
    def get_final_salary( self ):
        return float(self.__base_salaray) + (float (self.__extra_hours) * 276.5  ) + ( float(self.__base_salaray) * 0.03 * self.__antiguedad )

    