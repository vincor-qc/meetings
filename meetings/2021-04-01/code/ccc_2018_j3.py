distances = [int(x) for x in input().split()]


def distance(a, b):
    if a == b:
        return 0

    min_city = min(a, b)
    max_city = max(a, b)

    return sum(distances[min_city - 1 : max_city - 1])


for first_city in range(1, 6):
    row = []
    for second_city in range(1, 6):
        dist = distance(first_city, second_city)
        row.append(str(dist))

    print(" ".join(row))
