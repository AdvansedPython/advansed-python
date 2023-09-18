

def check_queen(coordinates: list) -> bool:

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


