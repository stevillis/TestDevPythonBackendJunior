"""
3) Escreva uma função que recebe uma string não vazia e a comprima de forma a substituir as sequências de caracteres iguais por um contador seguido do caractere em si. 
Por exemplo, "AAA" deve ser codificado como "3A", "AABBB" como "2A3B" e assim por diante.
Para complicarmos um pouco, a string de entrada pode conter qualquer caractere, incluindo números e caracteres especiais. E já que as strings codificadas devem ser 
decodificáveis, nós não podemos ingenuamente codificar uma string longa simplesmente pelo número de repetições. Por exemplo, "AAAAAAAAAAAA" (12 A's) não poderia ser 
codificada como "12A", uma vez que esta string poderia ser decodificada tanto como "AAAAAAAAAAAA" quanto "1AA". Logo, repetições de 10 ou mais caracteres, devem ser 
codificadas de forma dividida, ou seja, o exemplo acima deveria ser codificado como "9A3A".
 
Exemplo de entrada
string = "BBBBBBBBBBBBBAACCCDD"
 
Exemplo de saída
"9B4B2A3C2D"
"""


def replace_equal_character(string):
    char_dict = dict()
    for char in string:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            if char_dict[char] < 9:
                char_dict[char] += 1
            else:
                new_key = char + str(char_dict[char])
                if char_dict.get(new_key):
                    char_dict[new_key] += 1
                else:
                    char_dict[new_key] = 1

    result_string = ""
    for character, count in char_dict.items():
        if len(character) == 2:
            character = character[0]
        result_string += str(count) + str(character)

    return result_string


if __name__ == "__main__":
    # string = "AAA"  # -> "3A"
    # string = "AABBB"  # -> "2A3B"
    # string = "AAAAAAAAAAAA"  # -> "9A3A"
    string = "BBBBBBBBBBBBBAACCCDD"  # -> "9B4B2A3C2D"
    print(replace_equal_character(string))
