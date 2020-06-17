"""
https://www.hackerrank.com/contests/linguagens-de-programacao-para-ciencia-de-dados/challenges/nested-list
"""

lista = []
saida = []
notas = set()
for i in range(int(input())):
    name = input()
    score = float(input())
    lista.append([score, name])
    notas.add(score)
sco = list(notas)
sco.sort()

segundo = sco[1]

for i in range(len(lista)):
    if segundo == lista[i][0]:
        saida.append(lista[i][1])
saida.sort()
for i in range(len(saida)):
    print(saida[i])
