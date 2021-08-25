"""
https://www.hackerrank.com/contests/linguagens-de-programacao-para-ciencia-de-dados/challenges/text-wrap
"""
import textwrap


def wrap(string, max_width):
    return textwrap.fill(string, max_width)
