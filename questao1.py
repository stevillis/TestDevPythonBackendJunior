"""
1) Escreva uma função que recebe um array não vazio de inteiros distintos e um inteiro representando uma soma alvo. Se quaisquer dois números no array de 
entrada somam a soma alvo, a função deve retorná-los no array de saída, em qualquer ordem. Se nenhum par de números no array de entrada somarem a soma alvo, 
a função deve retornar um array vazio.
Note que a soma alvo deve ser obtida somando dois inteiros diferentes do array, você não pode somar um inteiro com ele mesmo.
Você pode assumir que existirá no máximo um par de números somando a soma alvo.
Exemplo de entrada
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
 
Exemplo de saída
[-1, 11] // pode ser na ordem invertida
"""


def funcao(array, target):
    start_index = 0
    while start_index < len(array) - 1:
        for current_index in range(start_index, len(array)):
            current_value = array[start_index]
            if start_index != current_index:
                next_value = array[current_index]
                sum = current_value + next_value
                if sum == target:
                    list_sum = [current_value, next_value]
                    list_sum.sort()
                    return list_sum

        start_index += 1
    return []


print(funcao([3, 5, -4, 8, 11, 1, -1, 6], 10))
