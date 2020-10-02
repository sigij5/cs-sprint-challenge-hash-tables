def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    num_dict = {num: num * -1 for num in a}
    
    result = []
    for key in num_dict:
        if key > 0 and num_dict[key] in num_dict:
            result.append(key)
    # print(result)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
