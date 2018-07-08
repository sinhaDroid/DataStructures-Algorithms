"""
    Given a string a, find the longest palindromic substring contained in a. 
    Your function definition should look like question2(a), and return a string.
"""


def question2(a):
    # make sure a is a string
    if type(a) != str:
        return "Error: 'a' is not a string"

    # make sure 'a' has atleast 2 characters
    if len(a) < 2:
        return a

    # convert string to lowercase
    text = a.lower()

    # append result here
    results = []

    for i in range(len(text)):
        for j in range(0, i):
            temp = text[j: i + 1]

            # if palindromic string found, append in results
            if temp == temp[::-1]:
                results.append(temp)

    # return max string with index
    return results


print(question2(3))
# Should print - Error: 'a' is not a string

print(question2("aa"))
# Should print - ['aa']

print(question2("palaindromeasfudacity"))
# Should print - ['ala']


# Explanation

"""
    To find a longest palindromic substring conained in string 'a'. It should have only
    string and must have atleast 2 characters. Checking the palindrome will take worst 
    case O(n) time and can be started from the center. Since there are only O(n) location
    any palindromic substring can be rooted, we can easily check all possible combinations 
    and will only take order O(n^2) time. 
    Therefore, the time complexity of this algorithm is O(n^2).
    Excluding the space used to load 'a', we only need to store left and right index of the 
    longest palindromic substring. 
    Therefore, the space complexity of this algorithm is O(1).
"""
