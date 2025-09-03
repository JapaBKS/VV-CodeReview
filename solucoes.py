import string

def sao_anagramas(string1, string2):
    try:
        palavra1, palavra2 = string1.replace(" ", ""), string2.replace(" ", "")
        palavra1, palavra2 = palavra1.lower(), palavra2.lower()
        list1, list2 = list(palavra1), list(palavra2)
        return sorted(list1) == sorted(list2)
    except:
        print("Formato inválido")


def cifra_de_cesar(texto, deslocamento):
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']
    cifra = []
    for char in texto:
        if char.lower() in alfabeto:
            index = (alfabeto.index(char.lower()) + deslocamento) % 26
            if char.isupper():
                cifra.append(alfabeto[index].upper())
            else:
                cifra.append(alfabeto[index])
        else:
            cifra.append(char)

    return "".join(cifra)


def encontrar_maior_palavra(frase):
    try:
        # garante que é string
        frase = str(frase)
        palavras = [p.strip(string.punctuation) for p in frase.split()]
        return max(palavras, key=len) if palavras else ""
    except Exception:
        # se der qualquer erro inesperado
        return ""

# Exemplos de teste
print(encontrar_maior_palavra("O rato roeu a roupa do rei de Roma"))  # roupa
print(encontrar_maior_palavra("A jornada de mil milhas começa com um único passo."))  # jornada
print(encontrar_maior_palavra("Seja forte e corajoso"))  # corajoso
