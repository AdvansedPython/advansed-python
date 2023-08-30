START_NUMBER = 2
ROWS = 4
COLUMNS = 9
LINES = 2
local_start_number = START_NUMBER # Не уверен что так можно, когда есть константа, а я делаю
# с ее помощью другую изменяемую. Это нормально?

for i in range(LINES):
    for j in range(COLUMNS):
        for k in range(ROWS):
            first_num = local_start_number + k
            second_num = START_NUMBER + j
            print(f"{first_num} X {second_num} = {first_num * second_num}", end="\t")
        print()
    local_start_number = 6
    print()