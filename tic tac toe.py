import tkinter as tk

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Morpion")
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.tour = 'X'
        self.gameover = False
        self.create_widgets()

    def create_widgets(self):
        self.cells = []
        for i in range(3):
            row = []
            for j in range(3):
                cell = tk.Button(self.master, text=' ', font=('Helvetica', 60), width=3, height=1,
                                 command=lambda i=i, j=j: self.jouer(i, j))
                cell.grid(row=i, column=j)
                row.append(cell)
            self.cells.append(row)

        self.status = tk.Label(self.master, text="C'est le tour de " + self.tour, font=('Helvetica', 16))
        self.status.grid(row=3, column=0, columnspan=3)

        self.restart_button = tk.Button(self.master, text='Rejouer', font=('Helvetica', 16),
                                         command=self.rejouer)
        self.restart_button.grid(row=4, column=0, columnspan=3)

    def jouer(self, ligne, colonne):
        if self.gameover:
            return

        if self.board[ligne][colonne] == ' ':
            self.board[ligne][colonne] = self.tour
            self.cells[ligne][colonne].config(text=self.tour)

            if self.check_win():
                self.status.config(text=self.tour + ' a gagné!')
                self.gameover = True
                return

            if self.check_tie():
                self.status.config(text='Match nul!')
                self.gameover = True
                return

            self.tour = 'O' if self.tour == 'X' else 'X'
            self.status.config(text="C'est le tour de " + self.tour)

    def check_win(self):
        # Vérifie les lignes
        for ligne in self.board:
            if ligne[0] == ligne[1] == ligne[2] != ' ':
                return True

        # Vérifie les colonnes
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return True

        # Vérifie les diagonales
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True

        return False

    def check_tie(self):
        for ligne in self.board:
            for cellule in ligne:
                if cellule == ' ':
                    return False
        return True

    def rejouer(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.tour = 'X'
        self.gameover = False
        for i in range(3):
            for j in range(3):
                self.cells[i][j].config(text=' ')
        self.status.config(text="C'est le tour de " + self.tour)

root = tk.Tk()
jeu = TicTacToe(root)
root.mainloop()
