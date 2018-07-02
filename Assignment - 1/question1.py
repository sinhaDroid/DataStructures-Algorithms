"""
    Given two strings s and t, determine whether some anagram of t 
    is a substring of s. For example: if s = "udacity" and t = "ad", 
    then the function returns True. Your function definition should 
    look like: question1(s, t) and return a boolean True or False.
"""


def question1(s, t):
    # make sure s is a string
    if type(s) != str:
        return "Error, s is not a string!"

    # make sure t is a string
    if type(s) != str:
        return "Error, t is not a string!"

    # len of s, t
    s_len = len(s)
    t_len = len(t)

    # make sure s has at least as much characters as t
    if s_len == 0 or s_len < t_len:
        return False

    # if t is empty, the answer should alwasy be True
    if t_len == 0:
        return True

    # sort the t string using sorted function
    t_sort = sorted(t)

    for x in range(s_len - t_len + 1):
        temp = s[x: x + t_len]

        # match with sorted value of temp with sorted value of t
        if t_sort == sorted(temp):
            return True

    return False

# Output


print(question1(2, "two"))
# It should print - Error, s is not a string!

print(question1("ad", "udacity"))
# It should print - false

print(question1("udacity", "ad"))
# It should print - true
