def game():
    board_arr = [" "]*9
    count = 0
    while True:
        create_board(board_arr)
        pos = input("Player 1 move: ") if count%2 == 0 else input("Player 2 move: ")
        if  not pos.isdigit() or int(pos) > 9 or int(pos) < 1 :
            print("Please enter a valid value")
            continue
        if not insert_move(count%2,int(pos)-1,board_arr):
            print("Please enter a valid position that is unoccupied")
            continue
        if check_state(board_arr):
            create_board(board_arr)
            print(f"Player {count%2+1} wins!")
            break
        if " " not in board_arr:
            create_board(board_arr)
            print("It's a draw!")
            break
        count += 1
        

def check_state(arr):
    xymatrix = [[" "," "," "],[" "," "," "],[" "," "," "],]
    yxmatrix = [[" "," "," "],[" "," "," "],[" "," "," "],]
    arr_cpy = arr.copy()
    ##transforming board array into 2D x,y matrix
    for i in range(3):
        for j in range(3):
            xymatrix[i][j] = arr_cpy.pop(0)
        ##checking per row
        if all(char == xymatrix[i][0] for char in xymatrix[i]) and xymatrix[i][0] != " ":
            return True
    
    ##transforming x,y into y,x
    for i in range(3):
        for j in range(3):
            yxmatrix[j][i] = xymatrix[i][j]

    ##checking per column
    for i in range(3):
        if all(char == yxmatrix[i][0] for char in yxmatrix[i]) and yxmatrix[i][0] != " ":
            return True

    if (arr[0] == arr[4] == arr[8] or arr[2] == arr[4] == arr[6]) and arr[4] != " ":
        return True
    return False

def create_board(arr):
    board = ""
    arr_cpy = arr.copy()
    for i in range(5):
        if i%2==0:
            for j in range(5):
                if j%2==0:
                    board += str(arr_cpy.pop(0))
                else:
                    board += "|"
        else:
            board += "-+-+-"
        board += "\n"
    print(board)


def insert_move(player,pos,arr):
    if arr[pos] == " ":
        arr[pos] = 'x' if player == 0 else 'o'
        return True
    return False


game()
