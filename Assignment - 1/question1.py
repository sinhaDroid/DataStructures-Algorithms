
def question1(s, t):

    # len of s, t
    s_len = len(s)
    t_len = len(t)

    # sort the t string using sorted function
    t_sort = sorted(t)

    for x in range(s_len - t_len + 1):
        temp = s[x: x + t_len]
        print sorted(temp)

        # match with sorted value of temp with sorted value of t
        if t_sort == sorted(temp):
            return True
    
    return False

print(question1("udacity", "ad"))
