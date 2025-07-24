lista_inteiros = []
print("Exclusão dos impares de uma lista de inteiros")
qtd_inteiros = int(input("Digite a quantidad de inteiros na lista:"))

for inteiro in range(qtd_inteiros):
    lista_inteiros.append(("Digite qual número será colocado na lista:"))

for inteiro in lista_inteiros:
    if inteiro % 2 != 0:
        lista_inteiros.remove(inteiro)

print(lista_inteiros)