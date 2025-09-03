def sao_anagramas(string1, string2):
  try:
    palavra1, palavra2 = string1.replace(" ", ""), string2.replace(" ", "")
    palavra1, palavra2 = palavra1.lower(), palavra2.lower()
    list1, list2 = list(palavra1), list(palavra2)
    return sorted(list1) == sorted(list2)
  except:
    print("Formato inválido")

def cifra_de_cesar(texto, deslocamento):
  # TODO: Implementar a lógica
  pass

def encontrar_maior_palavra(frase):
  # TODO: Implementar a lógica
  pass
