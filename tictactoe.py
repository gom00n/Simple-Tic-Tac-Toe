def someone_won(matrix):
    if (matrix[0] == matrix[1] == matrix[2] == "X")\
    or (matrix[3] == matrix[4] == matrix[5] == "X")\
    or (matrix[6] == matrix[7] == matrix[8] == "X")\
    or (matrix[0] == matrix[3] == matrix[6] == "X")\
    or (matrix[0] == matrix[3] == matrix[6] == "X")\
    or (matrix[1] == matrix[4] == matrix[7] == "X")\
    or (matrix[2] == matrix[5] == matrix[8] == "X")\
    or (matrix[0] == matrix[4] == matrix[8] == "X")\
    or (matrix[6] == matrix[4] == matrix[2] == "X"):
        return "X wins"
    elif (matrix[0] == matrix[1] == matrix[2] == "O")\
    or (matrix[3] == matrix[4] == matrix[5] == "O")\
    or (matrix[6] == matrix[7] == matrix[8] == "O")\
    or (matrix[0] == matrix[3] == matrix[6] == "O")\
    or (matrix[0] == matrix[3] == matrix[6] == "O")\
    or (matrix[1] == matrix[4] == matrix[7] == "O")\
    or (matrix[2] == matrix[5] == matrix[8] == "O")\
    or (matrix[0] == matrix[4] == matrix[8] == "O")\
    or (matrix[6] == matrix[4] == matrix[2] == "O"):
        return "O wins"

def print_string():
    print("---------")
    print(f"""| {string[0]} {string[1]} {string[2]} |
| {string[3]} {string[4]} {string[5]} |
| {string[6]} {string[7]} {string[8]} |""")
    print("---------")

string = list("_________")

print_string()
while True:
    coordinates = input().split()
    number = int((int(coordinates[0])-1)*3+int(coordinates[1]))-1
    moves = "XOXOXOXOX"
    counter = 0
    if coordinates[0] not in ["1","2","3"] or coordinates[1] not in ["1","2","3"]:
        print("Coordinates should be from 1 to 3!")
        continue
    elif string[number] != "_":
        print("This cell is occupied! Choose another one!")
        continue
    elif coordinates[0].isdigit() == False and coordinates[1].isdigit() == False:
        print("You should enter numbers!")
        continue
    else:
        string[number] = moves[counter]
        counter+=1
        print_string()
        print(someone_won(string))
        if someone_won(string) != None:
            break
