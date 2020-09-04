def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    current = { 
        i : None for i in arrays[0] 
    }

    for arr in range(1, len(arrays)):
        next_set = {}
        for item in arrays[arr]:
            if item in current:
                next_set[item] = None
        current = next_set
    result = [*current.keys()]
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
