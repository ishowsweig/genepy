def get_evens(start, stop):
    return [x for x in range(start, stop) if x % 2 == 0]


print(get_evens(900, 1000))
