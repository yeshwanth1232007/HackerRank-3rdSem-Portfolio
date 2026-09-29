def dynamicArray(n, queries):
    seqList = [[] for _ in range(n)]

    lastAnswer = 0
    answer = []

    for query in queries:
        query_type = query[0]
        x = query[1]
        y = query[2]

        idx = (x ^ lastAnswer) % n

        if query_type == 1:
            seqList[idx].append(y)

        elif query_type == 2:
            lastAnswer = seqList[idx][y % len(seqList[idx])]
            answer.append(lastAnswer)

    return answer
