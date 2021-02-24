

def search(data, x, y):
    print(type(data))
    new = list(
        filter(lambda person: person[x] == y, data))
    print(new)
    return new
