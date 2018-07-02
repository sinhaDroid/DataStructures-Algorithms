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
# Should print (1, ['ala'])
