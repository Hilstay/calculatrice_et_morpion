import tkinter

def check_nul():
    print("null")

def print_winner():
    global win
    if win is False:
        win = True
        print("le joueur", current_player, "a gagne le jeu")

def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

def check_win(cliked_row, clicked_col):
    # vicxtoire horizontale
    count = 0
    for i in range(3):
        current_button = buttons[i][cliked_row]
        # current_button.config(text='X')
        if current_button["text"] == current_player:
            count += 1
    if count == 3:
        print_winner()
    
                
    # verticelement
    count = 0
    for i in range(3):
        current_button = buttons[clicked_col][i]
        # current_button.config(text='X')
        if current_button["text"] == current_player:
            count += 1
    if count == 3:print_winner()
        
    # vitoire en diagonale
    count = 0
    for i in range(3):
        current_button = buttons[i][i]
        # current_button.config(text='X')
        if current_button["text"] == current_player:
            count += 1
    if count == 3:
        print_winner()
        
    # diagonale 2
    count = 0
    for i in range(3):
        current_button = buttons[2-i][i]
        # current_button.config(text='X')
        if current_button["text"] == current_player:
            count += 1
    if count == 3:
        print_winner()
        
    if win is False:
        count = 0
        for col in range(3):
            for row in range(3):
                current_button = buttons[col][row]
                if current_button["text"] == "X" or current_button["text"] == "O":
                    count += 1
                    print(count)
                    if count == 9:
                        print("match null")

def play_symbole(row, column):
    print("click", row , column)
    cliked_button = buttons[column][row]
    if cliked_button["text"] == "":
        cliked_button.config(text=current_player)
    check_win(row ,column)
    switch_player()

def draw_grid():
    for column in range(3):
        button_in_cols = []
        for row in range(3):
            button = tkinter.Button(root, font=("Arial", 50), height=3, width=5,
                                    command=lambda r=row, c=column: play_symbole(r, c)
                                    )
            button.grid(row=row, column=column)
            button_in_cols.append(button)
        buttons.append(button_in_cols)

buttons = []
current_player = "X"
win =False

# fenetre du jeu
root = tkinter.Tk()
root.minsize(500, 500)
root.title("TicTacToe")

draw_grid()

root.mainloop()