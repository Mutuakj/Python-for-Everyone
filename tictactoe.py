
import tkinter
def set_tile(row, column):
    global curr_player

    if (game_over):
        return

    if board[row][column]["text"] != "":
        return

    board[row][column]["text"] = curr_player #mark the board

    if curr_player == playerO: #switch player
        curr_player = playerX
    else:
        curr_player = playerO

    label["text"] = curr_player+"'s turn"

    # check for winning conditions
    check_winner()
def check_winner():
    global turns, game_over
    turns += 1

    #horizontally, check 3 rows
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"] + " is the winner!", foreground=color_yellow)
            for column in range(3):
                board[row][column].config(foreground=color_yellow, background=color_lightgray)
            game_over = True
            return

    #vertically, check 3 columns
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"] + " is the winner!", foreground=color_yellow)
            for row in range(3):
                board[row][column].config(foreground=color_yellow, background=color_lightgray)
            game_over = True
            return

    #diagonally
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"] + " is the winner!", foreground=color_yellow)
        for i in range(3):
            board[i][i].config(foreground=color_yellow, background=color_lightgray)
        game_over = True
        return

    #anti-diagonally
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"] + " is the winner!", foreground=color_yellow)
        for i in range(3):
            board[0][2].config(foreground=color_yellow, background=color_lightgray)
            board[1][1].config(foreground=color_yellow, background=color_lightgray)
            board[2][0].config(foreground=color_yellow, background=color_lightgray)
        game_over = True
        return

    #Add the tie condition
    if turns == 9:
        game_over = True
        label.config(text="Tie!", foreground=color_yellow)
def new_game():
    global turns, game_over

    turns = 0
    game_over = False
    label.config(text=curr_player+"'s turn", foreground="white")

    for row in range(3):
        for col in range(3):
            board[row][col].config(text="", fg=color_blue, bg=color_gray)

#game setup
# Two players. Player X and O
playerX = "X"
playerO = "O"

# A variable to keep track who the current player is
curr_player = playerX

# A three by three board
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

# Custom colors
color_blue = "#4584b6"
color_yellow = "#ffde57"
color_gray = "#343434"
color_lightgray = "#646464"

turns = 0
game_over = False

# window setup
window = tkinter.Tk() #Create the game window
window.title("Tic-Tac-Toe")
window.resizable(False, False)

# Create a frame that will hold the components
frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=curr_player+"'s turn", font=("Consolas", 20), background=color_gray, foreground="White")

label.grid(column=0, row=0, columnspan=3, sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Consolas", 50, "bold"),
                                            background=color_gray, foreground=color_blue, width=4, height=1,
                                            command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row+1, column=column)

button = tkinter.Button(frame, text="restart", font=("Consolas", 20), background=color_gray,
                        foreground="white", command=new_game)
button.grid(column=0, row=4, columnspan=3, sticky="we")


frame.pack()

# center the window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width - window_width) / 2)
window_y = int((screen_height - window_height) / 2)

# format the window with this new x & y values "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
# Add components i.e buttons and the text label
# Create a loop that will keep the window open
window.mainloop()


