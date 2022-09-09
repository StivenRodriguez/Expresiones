import re
import string # Importamos el modulo regex


def caracterNumDigits(character):
    global simbolo
    simbolo=""
    global Fin
    Fin=""
    digito="[0-9]"
    operador="[-+.]"
    letra="[Ee]"
    
    #comparamos si es digito o operador
    if(re.match(digito,character)):
        simbolo="Digito"
        return 0
    else:
        if(re.match(operador,character)):
            simbolo="Operador"
            return 1
        else:
            if(re.match(operador,character)):
                simbolo="Letra"
                return 3;
            if(character==Fin):
                return 2

def validarnumeroEnteros(cadena:string):
    caracterError = '';
    estado = 0
    tabla=[[1,1,"E"],[2,"E","E"],[3,"E","E"],[3,"E","A"]]
    data = '';  

    for  character in cadena:
        estadosig=estado
        #llamamos al metodo para saber si es un caracter valido y el valor retornado se guarda en charcaracter
        charcaracter= caracterNumDigits(character)
        #guardamos en estado el valor obtenido en la tabla segun las cordenadas que recibio anteriormente
        estado=tabla[estado][charcaracter]
        
        #Si el valor obtenido es una E imprimimos cadena no valida
        if (estado=="E"):
            caracterError = 'Cadena invalidad: ' +  character
            break

    #al concluir si el estado no es 3 que es el de aceptacion imprimimos cadena no valida    
    if(estado!=3):
       #cadena no valida 
       caracterError = 'Cadena no valida: ' +  character

    #si el estado es 3 es una cadena de aceptacion
    if(estado==3):
        #cadena valida
        caracterError = 'Cadena valida'
    
    return caracterError

def validarnumerosReales(cadena:string):
    caracterError = '';
    estado = 0
    tabla=[[1,1,"E"],[2,2,"E"],[3,"E","E"],[4,"E","E"],[4,"E","A"]]
    if (cadena.startswith('.')):
        caracterError = 'Cadena invalida: ' +  '.'
        return caracterError
    

    for  character in cadena:

        estadosig=estado
        #llamamos al metodo para saber si es un caracter valido y el valor retornado se guarda en charcaracter
        charcaracter= caracterNumDigits(character)
        #guardamos en estado el valor obtenido en la tabla segun las cordenadas que recibio anteriormente
        estado=tabla[estado][charcaracter]
        
        #Si el valor obtenido es una E imprimimos cadena no valida
        if (estado=="E"):
            caracterError = 'Cadena invalidad: ' +  character
            break


    #al concluir si el estado no es 5s que es el de aceptacion imprimimos cadena no valida    
    if(estado!=4):
       #cadena no valida 
       caracterError = 'Cadena no valida: ' +  character

    #si el estado es 5 es una cadena de aceptacion
    if(estado==4):
        #cadena valida
        caracterError = 'Cadena valida'
    
    return caracterError

def validarnotacionCientifica(cadena: string):
    caracterError = '';
    estado = 0
    tabla=[[1,1,"E"],[2,2,"E"],[3,"E","E"],[4,"E","E"],[4,"E","A"]]
    if (cadena.startswith('.')):
        caracterError = 'Cadena invalida: ' +  '.'
        return caracterError
    

    for  character in cadena:

        estadosig=estado
        #llamamos al metodo para saber si es un caracter valido y el valor retornado se guarda en charcaracter
        charcaracter= caracterNumDigits(character)
        #guardamos en estado el valor obtenido en la tabla segun las cordenadas que recibio anteriormente
        estado=tabla[estado][charcaracter]
        
        #Si el valor obtenido es una E imprimimos cadena no valida
        if (estado=="E"):
            caracterError = 'Cadena invalidad: ' +  character
            break


    #al concluir si el estado no es 5s que es el de aceptacion imprimimos cadena no valida    
    if(estado!=4):
       #cadena no valida 
       caracterError = 'Cadena no valida: ' +  character

    #si el estado es 5 es una cadena de aceptacion
    if(estado==4):
        #cadena valida
        caracterError = 'Cadena valida'
    
    return caracterError

