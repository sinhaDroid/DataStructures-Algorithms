"""
    Given two strings s and t, determine whether some anagram of t 
    is a substring of s. For example: if s = "udacity" and t = "ad", 
    then the function returns True. Your function definition should 
    look like: question1(s, t) and return a boolean True or False.
"""


def question1(s, t):

    # len of s, t
    s_len = len(s)
    t_len = len(t)

    # sort the t string using sorted function
    t_sort = sorted(t)

    for x in range(s_len - t_len + 1):
        temp = s[x: x + t_len]

        # match with sorted value of temp with sorted value of t
        if t_sort == sorted(temp):
            return True

    return False


print(question1("udacity", "ad"))
