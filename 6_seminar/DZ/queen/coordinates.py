from random import randint as rnd


def _random_coordinates():
    return [rnd(1,8) for x in range(2)]

def create_coordinates():

    coordinates = []
    while len(coordinates) < 8:
        coordinate = _random_coordinates()
        if coordinate not in coordinates:
            coordinates.append(coordinate)

    return coordinates