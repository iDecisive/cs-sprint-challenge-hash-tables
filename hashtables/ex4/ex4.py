def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    hashT = {}
    result = []
    for item in a:
        if item in hashT:
            result.append(abs(item))
        else:
            hashT[item * -1] = item
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
