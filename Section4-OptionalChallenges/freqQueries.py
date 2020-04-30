def freqQuery(queries):
    collection = {}
    freq_dict = {}
    output = []
    for i in queries:
        arr = i
        if arr[0] == 1:
            if arr[1] not in collection:
                collection[arr[1]] = 1
            else:
                collection[arr[1]] += 1
        elif arr[0] == 2:
            if collection.get(arr[1]):
                collection[arr[1]] -= 1
        elif arr[0] == 3:
            if arr[1] in collection.values():
                output.append(1)
            else:
                output.append(0)
        else:
            continue

    return output


q = [[1,1],[2,2],[3,2],[1,1],[1,1],[2,1],[3,2]]
# q = [[1,3],[2,3],[3,2],[1,4],[1,5],[1,5],[1,4],[3,2],[2,4],[3,2]]
print(freqQuery(q))