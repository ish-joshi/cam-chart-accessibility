def bubble(items):
    size = len(items)

    for i in range(size):

        for j in range(size - 1 - i):

            curr = items[j]
            next = items[j + 1]

            if curr > next:
                items[j + 1] = curr
                items[j] = next

    print(items)


bubble([-1, 2, 3, 100, 5, -200])
