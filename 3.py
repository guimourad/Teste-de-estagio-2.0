'''
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
'''




import json

# Função para calcular o menor valor de faturamento
def menor_valor(faturamento):
    menor = None
    for fat in faturamento:
        if fat["valor"] > 0:  # Ignorando dias com faturamento zero
            if menor is None or fat["valor"] < menor:
                menor = fat["valor"]
    return menor

# Função para calcular o maior valor de faturamento
def maior_valor(faturamento):
    maior = None
    for fat in faturamento:
        if fat["valor"] > 0:  # Ignorando dias com faturamento zero
            if maior is None or fat["valor"] > maior:
                maior = fat["valor"]
    return maior

# Função para calcular o número de dias acima da média mensal
def dias_acima_media(faturamento):
    soma_faturamento = 0
    dias_com_faturamento = 0
    
    # Somando o faturamento total e contando os dias válidos
    for fat in faturamento:
        if fat["valor"] > 0:  # Ignorando dias com faturamento zero
            soma_faturamento += fat["valor"]
            dias_com_faturamento += 1
    
    # Calculando a média mensal
    if dias_com_faturamento > 0:
        media = soma_faturamento / dias_com_faturamento
    else:
        media = 0
    
    # Contando o número de dias com faturamento acima da média
    dias_acima = 0
    for fat in faturamento:
        if fat["valor"] > 0 and fat["valor"] > media:
            dias_acima += 1
    
    return dias_acima

# Processamento dos dados do faturamento
def processar_faturamento(arquivo_json):
    with open(arquivo_json, 'r') as file:
        dados = json.load(file)
    
    faturamento = dados.get('faturamento', [])
    
    menor = menor_valor(faturamento)
    maior = maior_valor(faturamento)
    acima_media = dias_acima_media(faturamento)
    
    return menor, maior, acima_media

# Executa diretamente o processamento e exibe os resultados
menor, maior, acima_media = processar_faturamento('faturamento.json')
print(f"Menor valor de faturamento: {menor}")
print(f"Maior valor de faturamento: {maior}")
print(f"Número de dias com faturamento acima da média: {acima_media}")
