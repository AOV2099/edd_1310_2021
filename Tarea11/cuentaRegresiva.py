
def cuentaReg( num ):
    if num >= 0:
        if num == 0:
            print("0")
            print("Fin")
        else:
            print( num )
            cuentaReg( num - 1 )
    
    else:
        print("Este no es un numero positivo")


def mainCuenta():
    cuentaReg( 10 )

mainCuenta()