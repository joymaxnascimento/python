"""
https://www.hackerrank.com/contests/linguagens-de-programacao-para-ciencia-de-dados/challenges/swap-case
"""


def swap_case(s):
    texto = ''
    for i in s:
        if i.islower():
            texto = texto + i.capitalize()
        else:
            texto = texto + i.lower()
    return texto
