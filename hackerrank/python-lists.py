"""
https://www.hackerrank.com/contests/linguagens-de-programacao-para-ciencia-de-dados/challenges/python-lists
"""

N = int(input())
conjunto = {}
lista = []
for i in range(N):
    comando, *line = input().split()
    valores = list(map(int, line))
    conjunto[comando] = valores
    if 'insert' in conjunto:
        lista.insert(conjunto['insert'][0], conjunto['insert'][1])
        del conjunto['insert']
    if 'print' in conjunto:
        print(lista)
        del conjunto['print']
    if 'remove' in conjunto:
        lista.remove(conjunto['remove'][0])
        del conjunto['remove']
    if 'append' in conjunto:
        lista.append(conjunto['append'][0])
        del conjunto['append']
    if 'sort' in conjunto:
        lista.sort()
        del conjunto['sort']
    if 'pop' in conjunto:
        lista.pop()
        del conjunto['pop']
    if 'reverse' in conjunto:
        lista.reverse()
        del conjunto['reverse']
