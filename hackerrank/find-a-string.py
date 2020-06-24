"""
https://www.hackerrank.com/contests/linguagens-de-programacao-para-ciencia-de-dados/challenges/find-a-string
"""


def count_substring(string, sub_string):
    count = 0
    string2 = string[string.find(sub_string):len(string)+1]
    while sub_string in string2:
        count += 1
        string2 = string2[string2.find(sub_string)+1:len(string2)]
    return count
