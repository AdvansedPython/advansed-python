

def print_desk(coordinates: list):
    
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

