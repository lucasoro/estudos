# Percorre uma string e retorna a quantidade de vogais >> RECURSIVAMENTE

def vocals(string, counter, vocal_list):

    if len(string) == 1:
        if string in vocal_list:
            return counter + 1
        else:
            return counter

    return vocals(string[1:], counter + 1, vocal_list) if string[0] in vocal_list else vocals(string[1:], counter, vocal_list)


print(vocals("asdaosdhnasdada", 0, ["a", "e", "i", "o", "u"]))