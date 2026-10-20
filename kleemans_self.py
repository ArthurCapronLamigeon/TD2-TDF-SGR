import csv

def read_csv(path):
    with open(path, encoding="utf-8") as fichier:
        lecteur = csv.reader(fichier, delimiter=";")
        data = list(lecteur)
    return data

def structurer_reference_freqs(data) :
    nb_langues = len(data[0])
    dico = {}
    for i in range (1,nb_langues) :
        dico[data[0][i]] = {}
        for k in range(1,len(data)):
            dico[data[0][i]][data[k][0]]= float(data[k][i].strip("%")) /100
    return dico
    
def compter_occurences(s) :
    alphabet = "abcdefghijklmnopqrstuvwxyzßàáâãäåæçèéêëìíîïðñòóôöøùúüýþąćĉčďęěĝğĥıĵłńňœřśŝşšťŭůźżž"
    alphabet_maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZSSÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÖØÙÚÜÝÞĄĆĈČĎĘĚĜĞĤIĴŁŃŇŒŘŚŜŞŠŬŮŹŻŽ"
    occurence = {}
    nb_lettres = 0
    for lettre in alphabet :
        occurence[lettre] = 0
    for c in s :
        for i in range(len(alphabet)) :
            if c == alphabet[i] or c === alphabet_maj[i] :
                occurence[alphabet[i]] = occurence[alphabet[i]] + 1
                nb_lettres +=1
    return occurence
    frequence = {}
    for key in occurence :
        frequence[key] = occurence[key]/nb_lettres

if __name__ == "__main__" :
    data = read_csv("letter_frequency.csv")
    print(structurer_reference_freqs(data))