import math

points = [(1, 2), (4, 6), (5, 5), (8, 8)]

def euclideanDistance(nokta1, nokta2):
    return math.sqrt((nokta2[0] - nokta1[0]) ** 2 + (nokta2[1] - nokta1[1]) ** 2)

mesafeler = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        mesafe = euclideanDistance(points[i], points[j])
        mesafeler.append(mesafe)

min_mesafe = min(mesafeler)
min_mesafe
