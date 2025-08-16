
from tkinter import *
import random

def next_turn(row, column):
    global player

    # Player move
    if buttons[row][column]['text'] == "" and check_winner() is False:
        buttons[row][column]['text'] = "X"

        if check_winner() is False:
            player = "O"
            label.config(text="O's turn")
            window.after(50, ai_move)  # AI move delayed by 50ms

        elif check_winner() is True:
            label.config(text="X wins")

        elif check_winner() == "Tie":
            label.config(text="Tie!")

def ai_move():
    global player

    if check_winner() is False:
        best_score = -float("inf")
        move = None

        # AI choosing best move using minimax 
        for r in range(3):
            for c in range(3):
                if buttons[r][c]['text'] == "":
                    buttons[r][c]['text'] = "O"
                    score = minimax(False)
                    buttons[r][c]['text'] = ""
                    if score > best_score:
                        best_score = score
                        move = (r, c)

        if move:
            buttons[move[0]][move[1]]['text'] = "O"

        if check_winner() is False:
            player = "X"
            label.config(text="X's turn")
        elif check_winner() is True:
            label.config(text="O wins")
        elif check_winner() == "Tie":
            label.config(text="Tie!")

#maximizing possibility of AI using minimax
def minimax(is_maximizing):
    result = check_winner_no_ui()
    if result == "O":  # AI wins
        return 1
    elif result == "X":  # Human wins
        return -1
    elif result == "Tie":
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for r in range(3):
            for c in range(3):
                if buttons[r][c]['text'] == "":
                    buttons[r][c]['text'] = "O"
                    score = minimax(False)
                    buttons[r][c]['text'] = ""
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for r in range(3):
            for c in range(3):
                if buttons[r][c]['text'] == "":
                    buttons[r][c]['text'] = "X"
                    score = minimax(True)
                    buttons[r][c]['text'] = ""
                    best_score = min(score, best_score)
        return best_score

def check_winner_no_ui():
    # check Rows
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            return buttons[row][0]['text']

    # check Columns
    for col in range(3):
        if buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text'] != "":
            return buttons[0][col]['text']

    # Diagonals
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return buttons[0][0]['text']
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return buttons[0][2]['text']

    if not empty_spaces():
        return "Tie"

    return None

def check_winner():
    #check rows
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    # check Columns
    for col in range(3):
        if buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text'] != "":
            buttons[0][col].config(bg="green")
            buttons[1][col].config(bg="green")
            buttons[2][col].config(bg="green")
            return True

    # Diagonals
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    elif empty_spaces() is False:
        for row in range(3):
            for col in range(3):
                buttons[row][col].config(bg="red")
        return "Tie"

    return False

def empty_spaces():
    return any(buttons[r][c]['text'] == "" for r in range(3) for c in range(3))

def new_game():
    global player
    player = "X"
    label.config(text="X's turn")
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", bg="#F0F0F0")

window = Tk()
window.title("Tic-Tac-Toe Unbeatable ")
player = "X"
buttons = [[0,0,0],[0,0,0],[0,0,0]]


label = Label(text=player + " turn", font=('consolas',50))
label.pack(side="top")


reset_button = Button(text="play again", font=('consolas',21), command=new_game)
reset_button.pack(side="top")


frame = Frame(window)
frame.pack()


for row in range(3):
    for col in range(3):
        buttons[row][col] = Button(frame, text="", font=('consolas',50), width=4, height=1,
                                   command=lambda row=row, col=col: next_turn(row,col))
        buttons[row][col].grid(row=row, column=col)



window.mainloop()