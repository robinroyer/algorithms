import sys


"""
Function to return an arg if provided to the script

number: number of the arg in sys.argv
return: l'argument demandé ou une chaine de caracteres vide
"""
def getArgv(number):
    try:
        sys.argv[number]
    except IndexError:
        return ""
    else:
        return sys.argv[number]