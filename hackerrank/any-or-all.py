"""
https://www.hackerrank.com/contests/linguagens-de-programacao-para-ciencia-de-dados/challenges/any-or-all
"""

valor = input()
lista = input().split()
print(all(int(i) >= 0 for i in lista) and any(i == i[::-1] for i in lista))
