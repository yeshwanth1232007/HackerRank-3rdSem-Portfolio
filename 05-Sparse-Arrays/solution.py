def matchingStrings(stringList, queries):
    frequency = {}

    for string in stringList:
        frequency[string] = frequency.get(string, 0) + 1

    answer = []

    for query in queries:
        answer.append(frequency.get(query, 0))

    return answer
