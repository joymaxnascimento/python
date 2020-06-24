"""
https://www.hackerrank.com/contests/linguagens-de-programacao-para-ciencia-de-dados/challenges/python-string-formatting
"""


def print_formatted(number):
    tabamnho = len(bin(number))
    for n in range(number):
        print(str((n + 1)).rjust(tabamnho - 2) + (oct(n + 1).replace('0o', '')).rjust(tabamnho - 1) + (
            hex(n + 1).replace('0x', '').upper()).rjust(tabamnho - 1) + (
            bin(n + 1).replace('0b', '')).rjust(tabamnho - 1))
