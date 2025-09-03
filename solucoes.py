def sao_anagramas(string1, string2):
  # TODO: Implementar a lógica
  pass

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
  # TODO: Implementar a lógica
  pass

