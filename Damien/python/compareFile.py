from sys import argv, stderr
from time import time

global debug
debug = False


def trim(chaine):
    result = ""
    cpt = 0
    for lettre in chaine:
        if lettre != " ":
            result += str(lettre)
        else:
            cpt += 1

    return result


def formatFile(file):
    data = file.read()
    data = data.split('\n')
    result = ""

    for ligne in data:
        if ":" in ligne:
            ligne = ligne.split(":")[0]
        result += str(trim(ligne))

    return result


def loadFile(loadFile, affichage=None):

    fi = None
    if affichage is not None:
        global debug
        debug = affichage

    printf("Chargement du fichier {0}".format(loadFile))

    try:
        fi = open(loadFile, 'r')
        fi = formatFile(fi)
    except OSError:
        printf("Fichier introuvable", file=stderr)
        exit(-1)
    except:
        printf("Erreur imprévue", file=stderr)
        exit(-1)

    return fi


def printf(txt, **keyargs):

    if debug:
        print(txt)


def compare(pi, appro):

    printf("Debut de la comparaison...")
    # printf(pi)
    # printf("appro: {0}".format(appro))

    i = 0
    start = time()
    try:
        while pi[i].isnumeric() and appro[i].isnumeric() and i < len(pi)-1 and i < len(appro)-1:
            # print(pi[i], " is equals to ? ", appro[i])
            if pi[i] == appro[i]:
                i += 1
                continue
            else:
                break
    except IndexError:
        printf("Index Error")
    end = time()

    printf("Le nombre à une précision de {0} chiffre(s) en {1} s".format(i, (end - start)))
    appro = list(appro)
    appro.insert(1, '.')
    appro = "".join(appro)
    
    return appro, end-start, i



if __name__ == '__main__':

    debug = True
    compare(loadFile(argv[1]), loadFile(argv[2]))