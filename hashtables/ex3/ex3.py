def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    # dic = {}
    # lists = dict((l) for l in arrays)

    # dic = {}
    # for i in range(len(arrays)):
    #     dic[i] = dict.fromkeys(arrays[i], 0)

    dic = []
    for array in arrays:
        dic.append(dict.fromkeys(array, 0))
    
    result = dic.pop()
    for d in dic:
        result = result & d.keys()

    # result = list(reduce(lambda x, y: x & y.keys(), dic))

    # result = dic[0]
    # for i in range(1, len(dic)-1):
    #     result = result & dic[i].keys()

    result = list(result)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
