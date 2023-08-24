import winsound

board = ['-','-','-','-','-','-','-','-','-']
current_player = "x"
winner = None
game_running = True

def display_board():
    print('|' + board[0] + '|' + board[1] + '|' + board[2] + '|')
    print("-------")
    print('|' + board[3] + '|' + board[4] + '|' + board[5] + '|')
    print("-------")
    print('|' + board[6] + '|' + board[7] + '|' + board[8] + '|')

def inp(current_player):
    inp = int(input("Enter between 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp - 1] == "-":
        board[inp - 1] = current_player
    else:
        print("Invalid input or position already taken. Try again.")

def checkhorizental():
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
    return False

def checkvertical():
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    return False

def checkrow():
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    return False

def checktie():
    if "-" not in board:
        global game_running
        print("Tie!")
        game_running = False

def checkwin():
    if checkhorizental() or checkvertical() or checkrow():
        print(f"Winner is {winner}")
        global game_running
        game_running = False
        winsound.PlaySound("python.wav", winsound.SND_FILENAME)

def switch_turn():
    global current_player
    if current_player == "x":
        current_player = "o"
    else:
        current_player = "x"

while game_running:
    display_board()
    inp(current_player)
    checkwin()
    checktie()
    switch_turn()
