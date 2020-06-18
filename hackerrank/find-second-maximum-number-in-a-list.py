"""
https://www.hackerrank.com/contests/linguagens-de-programacao-para-ciencia-de-dados/challenges/find-second-maximum-number-in-a-list
"""

n = int(input())
arr = map(int, input().split())
lista = list(set(arr))
lista.sort()
print(lista[-2])
