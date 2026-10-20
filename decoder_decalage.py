import chiffrement_decalage as cd
import sys
def lire_stdin():
    """Lit l'entrée standard en invitant l'utilisateur à l'aide d'un message si le flux d'entrée n'est pas redirigé"""
    if sys.stdin.isatty():
        sys.stderr.write("Saisissez du texte (Ctrl+D pour terminer) :\n")
    return sys.stdin.read()


def dechiffrage(s):
    for i in range(26) :
        yield cd.chiffrer(s,i), i

if __name__ == "__main__" :
    for dec in dechiffrage(lire_stdin()) :
        print (dec)
        

    
