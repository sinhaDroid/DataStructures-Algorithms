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


# Explanations

"""
    The two strings are anagram by checking and comparing all character of 
    one string to be present as a substring of another string. This should only
    accept two strings and if one of the string is empty, then both string will 
    always be anagram. For 's' and 't' to be anagram, 's'must have at least as much
    character as 't'. We will split and sort the character of 't' using sorted function
    and store it in temporary variable. We will check every possible consecutive substring
    in 's' with string 't'. If any set is anagram of 't', then we return True, else False.
    Comparing counts of all characters will be done in constant time since there are 
    only limited amount of characters to check. Looping through all possible consecutive 
    substrings will take worst case O(len(s)). 
    Therefore, the time complexity of this algorithm is O(len(s)).
    Since, the number of characters in 't' and 's' are bounded, the space used to load 't' 
    and 's' is 0(1).
    Therefore, the space complexity of this algorithm is O(1).
"""
