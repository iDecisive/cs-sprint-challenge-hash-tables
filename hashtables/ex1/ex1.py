def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """

    index_weight = {}
    for i in range(len(weights)):
        if limit - weights[i] in index_weight:
            return [i, index_weight[limit - weights[i]]]
        else: 
            index_weight[weights[i]] = i

    return None
