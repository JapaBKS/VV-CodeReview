import string

def sao_anagramas(string1, string2):
  # TODO: Implementar a lógica
  pass

def cifra_de_cesar(texto, deslocamento):
  # TODO: Implementar a lógica
  pass

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