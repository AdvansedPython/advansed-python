from random import randint as rnd


class Queen:

    def __init__(self):
        self.coordinates = self.create_coordinates()



    def _random_coordinates(self):
        return [rnd(1,8) for x in range(2)]

    def create_coordinates(self):

        coordinates = []
        while len(coordinates) < 8:
            coordinate = self._random_coordinates()
            if coordinate not in coordinates:
                coordinates.append(coordinate)

        return coordinates


    def check_queen(self) -> bool:

        coordinates = self.coordinates # Можно ли делать при переписке на класс такое?

        x_set = {x[0] for x in coordinates}
        y_set = {y[1] for y in coordinates}

        if len(x_set) < len(coordinates) or len(y_set) < len(coordinates):
            return False

        
        for x, y in coordinates:
            i, j = x, y
            my_count = 0

            while i < 9 and j < 9:
                if [i,j] in coordinates:
                    my_count += 1
                i+=1
                j+=1

                if my_count > 1:
                    return False

            i, j = x, y
            my_count = 0
            while i > 0 and j > 0:
                if [i,j] in coordinates:
                    my_count += 1
                i-=1
                j-=1

                if my_count > 1:
                    return False
                
            i, j = x, y
            my_count = 0
            while i < 9 and j > 0:
                if [i,j] in coordinates:
                    my_count += 1
                i+=1
                j-=1

                if my_count > 1:
                    return False
                
            i, j = x, y
            my_count = 0
            while i > 0 and j < 9:
                if [i,j] in coordinates:
                    my_count += 1
                i-=1
                j+=1

                if my_count > 1:
                    return False
                

        return True


    def print_desk(self):
        
        coordinates = self.coordinates

        print("    1   2   3   4   5   6   7   8")
        print("  —————————————————————————————————")
        for i in range(8):
            print(f"{i+1} ",end="")
            print("|", end="")
            for j in range(8):
                if [i+1,j+1] in coordinates:
                    print(" ♕ |", end="")
                else:
                    print("   |", end="")
            print()
            print("  —————————————————————————————————")




