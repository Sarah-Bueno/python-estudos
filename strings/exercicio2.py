"""Faça a leitura de uma linha de dados que contenha três
números separados por espaços em branco e carregue os objetos A, B, C com os
valores individuais.
Exemplo:
- Entrada: “35 22 87”
- Espera-se que o programa carregue A com 35, B com 22, C com 8"""

entrada = input("Digite a entrada: ")
lista = entrada.split()

A = lista[0]
B = lista[1]
C = lista[2]

print(A)
print(B)
print(C)
