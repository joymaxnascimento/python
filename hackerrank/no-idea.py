"""
https://www.hackerrank.com/contests/linguagens-de-programacao-para-ciencia-de-dados/challenges/no-idea
"""

n, m = map(int, input().split(" "))
array = list(map(int, input().split(" ")))
a = set(map(int, input().split(" ")))
b = set(map(int, input().split(" ")))
h = 0

for v in array:
    if v in a:
        h += 1
    elif v in b:
        h -= 1
print(h)
