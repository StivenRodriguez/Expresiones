import re
import string # Importamos el modulo regex

def ValidarCadenasConNumeros(cadena:string):
    patron = re.compile(r"^([aA-zZ][a-z]+[ ]?){1,6}")
    if patron.match(cadena):
        return True
    else:
        return False

def ValidarEnteros(numero:string):
    patron = re.compile(r"^[0-9]+$|^[-+][0-9]+$")
    if patron.match(numero):
        return True
    else:
        return False

def ValidarReales(numeroReal: string):
    patron = re.compile(r"^[-+]?[0-9]{1,3}\.[0-9]{1,3}$")
    if patron.match(numeroReal):
        return True
    else:
        return False

def ValidarNotacionCientifica(numeroNotacion: string):
    patron = re.compile(r"^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$")
    if patron.match(numeroNotacion):
        return True
    else:
        return False

def ValidarEmail(email:string): 
    patron = re.compile(r"[A-Za-z0-9._%-]+@[A-Za-z0-9._%-]+\.[a-z]{2,3}$")
    if patron.search(email):
        return True
    else:
        return False
