from transversales import expresionesRegulares
from transversales import automataExpresionesRegulares
import string # Importamos el modulo regex

def ValidarEnteros(numero:string):
    estadoEntero = expresionesRegulares.ValidarEnteros(numero)
    return estadoEntero

def ValidarReales(numeroReal:string):
    estadoNumeroReal = expresionesRegulares.ValidarReales(numeroReal)
    return estadoNumeroReal
    
def ValidarNotacionCientifica(numeroNotacion:string):
    estadoNotacion = expresionesRegulares.ValidarNotacionCientifica(numeroNotacion)
    return estadoNotacion

def ValidarEmail(email:string):
    estadoEmail = expresionesRegulares.ValidarEmail(email)
    return estadoEmail


def ValidarEnterosAutomata(numero: string):
    estadoEntero = automataExpresionesRegulares.validarnumeroEnteros(numero)
    return estadoEntero

def validarRealesAutomata(numero: string):
    estadoReal = automataExpresionesRegulares.validarnumerosReales(numero)
    return estadoReal