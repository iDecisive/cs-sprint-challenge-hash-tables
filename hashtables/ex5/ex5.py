
def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    hashT = {}
    result = []
    for f in files:
        temp = f.split('/')
        if temp[-1] in hashT:
            hashT[temp[-1]].append(f)
        else:
            hashT[temp[-1]] = [f]

    for q in queries:
        if q in hashT:
            result += hashT[q]
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
