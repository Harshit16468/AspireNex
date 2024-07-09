import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False

def minimax(game, depth, alpha, beta, maximizing):
    case = game.current_winner
    if case == 'O':
        return 1
    elif case == 'X':
        return -1
    elif not game.empty_squares():
        return 0

    if maximizing:
        max_eval = float('-inf')
        for move in game.available_moves():
            game.make_move(move, 'O')
            eval = minimax(game, depth + 1, alpha, beta, False)
            game.board[move] = ' '
            game.current_winner = None
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in game.available_moves():
            game.make_move(move, 'X')
            eval = minimax(game, depth + 1, alpha, beta, True)
            game.board[move] = ' '
            game.current_winner = None
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def get_best_move(game, maximizing):
    best_move = None
    if maximizing:
        best_eval = float('-inf')
        for move in game.available_moves():
            game.make_move(move, 'O')
            eval = minimax(game, 0, float('-inf'), float('inf'), False)
            game.board[move] = ' '
            game.current_winner = None
            if eval > best_eval:
                best_eval = eval
                best_move = move
    else:
        best_eval = float('inf')
        for move in game.available_moves():
            game.make_move(move, 'X')
            eval = minimax(game, 0, float('-inf'), float('inf'), True)
            game.board[move] = ' '
            game.current_winner = None
            if eval < best_eval:
                best_eval = eval
                best_move = move
    return best_move

class TicTacToeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic-Tac-Toe")
        self.game = TicTacToe()
        self.buttons = []
        self.human_letter = 'X'
        self.ai_letter = 'O'
        self.create_board()
        self.ask_first_player()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.master, text='', font=('normal', 40), width=5, height=2,
                                   command=lambda row=i, col=j: self.make_move(row, col))
                button.grid(row=i, column=j)
                self.buttons.append(button)

    def ask_first_player(self):
        result = messagebox.askyesno("First Move", "Do you want to go first?")
        if not result:
            self.human_letter = 'O'
            self.ai_letter = 'X'
            self.ai_move()

    def make_move(self, row, col):
        index = 3 * row + col
        if self.game.board[index] == ' ':
            self.game.make_move(index, self.human_letter)
            self.buttons[index].config(text=self.human_letter)
            self.check_game_over()

            if not self.game.current_winner and self.game.empty_squares():
                self.master.after(500, self.ai_move)

    def ai_move(self):
        move = get_best_move(self.game, self.ai_letter == 'O')
        self.game.make_move(move, self.ai_letter)
        self.buttons[move].config(text=self.ai_letter)
        self.check_game_over()

    def check_game_over(self):
        if self.game.current_winner:
            winner = "You" if self.game.current_winner == self.human_letter else "AI"
            messagebox.showinfo("Game Over", f"{winner} win!")
            self.close()
        elif not self.game.empty_squares():
            messagebox.showinfo("Game Over", "It's a tie!")
            self.close()
    def close(self):
        self.master.quit()
        self.master.destroy()

def main():
    root = tk.Tk()
    TicTacToeGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()