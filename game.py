from tkinter import Button, Tk, Grid, messagebox
import numpy as np


class TICTACTOE:
    def __init__(self):
        self.counter = 0
        self.table = np.zeros(shape=(3, 3), dtype=np.int8)
        self.btnMap = [[], [], []]

    def winCheck(self, val):
        for i in range(3):
            if (self.table[:, i] == val).all() or (self.table[i, :] == val).all():
                return True
        if (self.table.diagonal() == val).all() or (
            np.fliplr(self.table).diagonal() == val
        ).all():
            return True
        return False

    def click(self, row, col):
        if self.btnMap[row][col].cget("text") == " ":
            val = 1 if self.counter % 2 == 0 else -1
            player = "X" if self.counter % 2 == 0 else "O"
            self.table[row][col] = val
            self.btnMap[row][col].configure(text=player)
            self.counter += 1
            if self.winCheck(val):
                messagebox.showinfo(
                    "WINNER", f"Congrats!! PLAYER {player} have won the game!"
                )
                self.newGame()
            elif self.counter > 8:
                messagebox.showinfo("DRAW", "Nobody WON")
                self.newGame()
        else:
            messagebox.showwarning("Warning", "Box already marked!")

    def newGame(self):
        if messagebox.askyesno("Again?", "Do you want to play again?"):
            self.counter = 0
            self.table = np.zeros(shape=(3, 3), dtype=np.int8)
            for row in range(3):
                for col in range(3):
                    self.btnMap[row][col].configure(text=" ")
        else:
            self.app.destroy()

    def board(self):
        self.app = Tk()
        self.app.geometry("500x500")
        self.app.title("TIC TAC TOE")
        for row in range(3):
            for col in range(3):
                btn = Button(
                    self.app,
                    text=" ",
                    bg="#F9FBFF",
                    fg="#5c6274",
                    font=("Calibiri", 36, "bold"),
                    command=lambda x=row, y=col: self.click(row=x, col=y),
                )
                self.btnMap[row].append(btn)
                btn.grid(row=row, column=col, sticky="NSEW")
                Grid.rowconfigure(self.app, row, weight=1)
                Grid.columnconfigure(self.app, col, weight=1)
        self.app.mainloop()


game = TICTACTOE().board()
