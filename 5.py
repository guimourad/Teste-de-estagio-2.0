'''
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
'''

# Função para inverter a string
def inverter_string(texto):
    texto_invertido = ''

    #percorrer a string de trás para frente
    for i in range(len(texto) - 1, -1, -1):
        texto_invertido += texto[i]
    return texto_invertido

texto_original = input("Digite a string que deseja inverter: ")

texto_invertido = inverter_string(texto_original)
print(f"A string invertida é: {texto_invertido}")
