'''
1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será 
a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
escreva um programa na linguagem que desejar onde, informado um número, 
ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado
pertence ou não a sequência.1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1
e o próximo valor sempre será a soma dos 2 valores anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, 
informado um número, ele calcule a sequência de Fibonacci
e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
'''

def numero_fibonacci(num):
    # Função auxiliar para calcular a sequência de Fibonacci até um valor limite
    def sequencia_fibonacci(valor):
        sequencia = [0, 1]
        while sequencia[-1] < valor:
            sequencia.append(sequencia[-1] + sequencia[-2])
        return sequencia

    # Gera a sequência de Fibonacci até o valor de n
    fibonacci_sequencia = sequencia_fibonacci(num)

    print(f'Sequência de Fibonacci até {num}: {fibonacci_sequencia}')

    # Verifica se o número está na sequência
    if num in fibonacci_sequencia:
        return f'O número {num} pertence à sequência de Fibonacci.'
    else:
        return f'O número {num} não pertence à sequência de Fibonacci.'

# Exemplo de uso
numero = int(input("Informe um número: "))
resultado = numero_fibonacci(numero)
print(resultado)
