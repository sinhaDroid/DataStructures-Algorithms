
def question2(a):
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
    return text.index(max(results, key=len)), results


# Should print (1, ['ala'])
print(question2("palaindromeasfudacity"))
