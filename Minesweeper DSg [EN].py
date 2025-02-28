import random
import tkinter as tk
from tkinter import messagebox
import sys

rob = 1
user = 0
bomb = 0
X = ''

A = 0
B = 0
C = 0
D = 0

E = 0
F = 0
G = 0
H = 0

I = 0
J = 0
K = 0
L = 0

M = 0
N = 0
O = 0
P = 0

oneone = 'A'
onetwo = 'B'
onethree = 'C'
onefour = 'D'

twoone = 'E'
twotwo = 'F'
twothree = 'G'
twofour = 'H'

threeone = 'I'
threetwo = 'J'
threethree = 'K'
threefour = 'L'

fourone = 'M'
fourtwo = 'N'
fourthree = 'O'
fourfour = 'P'

root = tk.Tk()
root.title(f"Minesweeper DSg")

def remove():
    DS_text.grid_remove()
    button_new_game.grid_remove()
    button_manual.grid_remove()
    heading_manual.grid_remove()
    manual_text.grid_remove()
    button_main.grid_remove()
    laying_label.grid_remove()
    label_bomb.grid_remove()
    entry_bomb.grid_remove()
    laying_button.grid_remove()
    b_A.grid_remove()
    b_B.grid_remove()
    b_C.grid_remove()
    b_D.grid_remove()

    b_E.grid_remove()
    b_F.grid_remove()
    b_G.grid_remove()
    b_H.grid_remove()

    b_I.grid_remove()
    b_J.grid_remove()
    b_K.grid_remove()
    b_L.grid_remove()

    b_M.grid_remove()
    b_N.grid_remove()
    b_O.grid_remove()
    b_P.grid_remove()

def opt_user():
    global A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P
    user = entry_bomb.get().upper()

    if user == 'A':
        A = 1
        start_game()
    elif user == 'B':
        B = 1
        start_game()
    elif user == 'C':
        C = 1
        start_game()
    elif user == 'D':
        D = 1
        start_game()
    elif user == 'E':
        E = 1
        start_game()
    elif user == 'F':
        F = 1
        start_game()
    elif user == 'G':
        G = 1
        start_game()
    elif user == 'H':
        H = 1
        start_game()
    elif user == 'I':
        I = 1
        start_game()
    elif user == 'J':
        J = 1
        start_game()
    elif user == 'K':
        K = 1
        start_game()
    elif user == 'L':
        L = 1
        start_game()
    elif user == 'M':
        M = 1
        start_game()
    elif user == 'N':
        N = 1
        start_game()
    elif user == 'O':
        O = 1
        start_game()
    elif user == 'P':
        P = 1
        start_game()
    else:
        messagebox.showerror('ERROR!', 'THE LETTER WAS ENTERED INCORRECTLY! RESTART THE PROGRAM! (use Caps Lock)')

def laying():
    global A
    global B
    global C
    global D

    global E
    global F
    global G
    global H

    global I
    global J
    global K
    global L 

    global M
    global N
    global O
    global P
    global user
    bot = random.randint(1, 16)

    if bot==1:
        A = 1
    elif bot==2:
        B = 1
    elif bot==3:
        C = 1
    elif bot==4:
        D = 1
    elif bot==5:
        E = 1
    elif bot==6:
        F = 1
    elif bot==7:
        G = 1
    elif bot==8:
        H = 1
    elif bot==9:
        I = 1
    elif bot==10:
        J = 1
    elif bot==11:
        K = 1
    elif bot==12:
        L = 1
    elif bot==13:
        M = 1
    elif bot==14:
        N = 1
    elif bot==15:
        O = 1
    elif bot==16:
        P = 1
    laying_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    label_bomb.grid(row=2, column=0, padx=10, pady=10)
    entry_bomb.grid(row=2, column=1, padx=10, pady=10)
    if entry_bomb is not None:
        user = entry_bomb
        laying_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

def field ():
    b_A.grid(row=1, column=0, padx=10, pady=10)
    b_B.grid(row=1, column=1, padx=10, pady=10)
    b_C.grid(row=1, column=2, padx=10, pady=10)
    b_D.grid(row=1, column=3, padx=10, pady=10)

    b_E.grid(row=2, column=0, padx=10, pady=10)
    b_F.grid(row=2, column=1, padx=10, pady=10)
    b_G.grid(row=2, column=2, padx=10, pady=10)
    b_H.grid(row=2, column=3, padx=10, pady=10)

    b_I.grid(row=3, column=0, padx=10, pady=10)
    b_J.grid(row=3, column=1, padx=10, pady=10)
    b_K.grid(row=3, column=2, padx=10, pady=10)
    b_L.grid(row=3, column=3, padx=10, pady=10)

    b_M.grid(row=4, column=0, padx=10, pady=10)
    b_N.grid(row=4, column=1, padx=10, pady=10)
    b_O.grid(row=4, column=2, padx=10, pady=10)
    b_P.grid(row=4, column=3, padx=10, pady=10)

def start_game():
    remove()
    field()
    
def new_game():
    remove()
    laying()

def press(X):
    global bomb, oneone, onetwo, onethree, onefour, twoone, twotwo, twothree, twofour, \
       threeone, threetwo, threethree, threefour, fourone, fourtwo, fourthree, fourfour
    b_X = globals()[f'b_{X}']
    if globals()[X] == 1:
        b_X.config(text='💥')
        messagebox.showerror("Attention","You lost!")
        bomb = 1
        sys.exit()
    elif globals()[X] == 0:
        b_X.config(text='🕳')
        b_X.config(state='disabled')
        if X == 'A':
            oneone = 0
        elif X == 'B':
            onetwo = 0
        elif X == 'C':
            onethree = 0
        elif X == 'D':
            onefour = 0
        elif X == 'E':
            twoone = 0
        elif X == 'F':
            twotwo = 0
        elif X == 'G':
            twothree = 0
        elif X == 'H':
            twofour = 0
        elif X == 'I':
            threeone = 0
        elif X == 'J':
            threetwo = 0
        elif X == 'K':
            threethree = 0
        elif X == 'L':
            threefour = 0
        elif X == 'M':
            fourone = 0
        elif X == 'N':
            fourtwo = 0
        elif X == 'O':
            fourthree = 0
        elif X == 'P':
            fourfour = 0
        root.update()
    robot()

def robot():
    rob = random.randint(1, 16)

    global A
    global B
    global C
    global D

    global E
    global F
    global G
    global H

    global I
    global J
    global K
    global L 

    global M
    global N
    global O
    global P

    global oneone
    global onetwo
    global onethree
    global onefour

    global twoone
    global twotwo
    global twothree
    global twofour

    global threeone
    global threetwo
    global threethree
    global threefour

    global fourone
    global fourtwo
    global fourthree
    global fourfour

    global bomb
    
    if rob == 1:
        if A == 1:
            b_A.config(text='💥')
            messagebox.showerror("Attention", "Bot lost!")
            bomb = 1
            sys.exit()
        elif oneone == 0:
            robot()
        elif A == 0:
            oneone = 0
            b_A.config(text='🕳')
            b_A.config(state='disabled')

    elif rob == 2:
        if B == 1:
            b_B.config(text='💥')
            messagebox.showerror("Attention", "Bot lost!")
            bomb = 1
            sys.exit()
        elif onetwo == 0:
            robot()
        elif B == 0:
            onetwo = 0
            b_B.config(text='🕳')
            b_B.config(state='disabled')

    elif rob == 3:
        if C == 1:
            b_C.config(text='💥')
            messagebox.showerror("Attention", "Bot lost!")
            bomb = 1
            sys.exit()
        elif onethree == 0:
            robot()
        elif C == 0:
            onethree = 0
            b_C.config(text='🕳')
            b_C.config(state='disabled')

    elif rob == 4:
        if D == 1:
            b_D.config(text='💥')
            messagebox.showerror("Attention", "Bot lost!")
            bomb = 1
            sys.exit()
        elif onefour == 0:
            robot()
        elif D == 0:
            onefour = 0
            b_D.config(text='🕳')
            b_D.config(state='disabled')

    elif rob == 5:
        if E == 1:
            b_E.config(text='💥')
            messagebox.showerror("Attention", "Bot lost!")
            bomb = 1
            sys.exit()
        elif twoone == 0:
            robot()
        elif E == 0:
            twoone = 0
            b_E.config(text='🕳')
            b_E.config(state='disabled')

    elif rob == 6:
        if F == 1:
            b_F.config(text='💥')
            messagebox.showerror("Attention", "Bot lost!")
            bomb = 1
            sys.exit()
        elif twotwo == 0:
            robot()
        elif F == 0:
            twotwo = 0
            b_F.config(text='🕳')
            b_F.config(state='disabled')

    elif rob == 7:
        if G == 1:
            b_G.config(text='💥')
            messagebox.showerror("Attention", "Bot lost!")
            bomb = 1
            sys.exit()
        elif twothree == 0:
            robot()
        elif G == 0:
            twothree = 0
            b_G.config(text='🕳')
            b_G.config(state='disabled')

    elif rob == 8:
        if H == 1:
            b_H.config(text='💥')
            messagebox.showerror("Attention", "Bot lost!")
            bomb = 1
            sys.exit()
        elif twofour == 0:
            robot()
        elif H == 0:
            twofour = 0
            b_H.config(text='🕳')
            b_H.config(state='disabled')

    elif rob == 9:
        if I == 1:
            b_I.config(text='💥')
            messagebox.showerror("Attention", "Bot lost!")
            bomb = 1
            sys.exit()
        elif threeone == 0:
            robot()
        elif I == 0:
            threeone = 0
            b_I.config(text='🕳')
            b_I.config(state='disabled')

    elif rob == 10:
        if J == 1:
            b_J.config(text='💥')
            messagebox.showerror("Attention", "Bot lost!")
            bomb = 1
            sys.exit()
        elif threetwo == 0:
            robot()
        elif J == 0:
            threetwo = 0
            b_J.config(text='🕳')
            b_J.config(state='disabled')

    elif rob == 11:
        if K == 1:
            b_K.config(text='💥')
            messagebox.showerror("Attention", "Bot lost!")
            bomb = 1
            sys.exit()
        elif threethree == 0:
            robot()
        elif K == 0:
            threethree = 0
            b_K.config(text='🕳')
            b_K.config(state='disabled')

    elif rob == 12:
        if L == 1:
            b_L.config(text='💥')
            messagebox.showerror("Attention", "Bot lost!")
            bomb = 1
            sys.exit()
        elif threefour == 0:
            robot()
        elif L == 0:
            threefour = 0
            b_L.config(text='🕳')
            b_L.config(state='disabled')

    elif rob == 13:
        if M == 1:
            b_M.config(text='💥')
            messagebox.showerror("Attention", "Bot lost!")
            bomb = 1
            sys.exit()
        elif fourone == 0:
            robot()
        elif M == 0:
            fourone = 0
            b_M.config(text='🕳')
            b_M.config(state='disabled')

    elif rob == 14:
        if N == 1:
            b_N.config(text='💥')
            messagebox.showerror("Attention", "Bot lost!")
            bomb = 1
            sys.exit()
        elif fourtwo == 0:
            robot()
        elif N == 0:
            fourtwo = 0
            b_N.config(text='🕳')
            b_N.config(state='disabled')

    elif rob == 15:
        if O == 1:
            b_O.config(text='💥')
            messagebox.showerror("Attention", "Bot lost!")
            bomb = 1
            sys.exit()
        elif fourthree == 0:
            robot()
        elif O == 0:
            fourthree = 0
            b_O.config(text='🕳')
            b_O.config(state='disabled')

    elif rob == 16:
        if P == 1:
            b_P.config(text='💥')
            messagebox.showerror("Attention", "Bot lost!")
            bomb = 1
            sys.exit()
        elif fourfour == 0:
            robot()
        elif P == 0:
            fourfour = 0
            b_P.config(text='🕳')
            b_P.config(state='disabled')

def manual():
    remove()
    heading_manual.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    manual_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    button_main.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

def start_window():
    remove()
    DS_text.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    button_new_game.grid(row=2, column=0, padx=10, pady=10)
    button_manual.grid(row=2, column=1, padx=10, pady=10)

DS_text = tk.Text(root, wrap=tk.NONE, height=7, width=17)
DS_text.insert(tk.END, """
██████╗  ███████╗
██╔══██╗ ██╔════╝ 
██║  ██║ ███████╗
██║  ██║ ╚════██║
██████╔╝ ███████║ 
╚═════╝  ╚══════╝ """)
DS_text.config(state=tk.DISABLED)
button_new_game = tk.Button(root, text = 'New Game', command= new_game)
button_manual = tk.Button(root, text = 'Game Rules and Instructions', command= manual)    
heading_manual = tk.Label(root, text = 'Game Rules:')
manual_text = tk.Text(root, wrap=tk.NONE, height=5, width=75)
manual_text.insert(tk.END, """At the beginning of the game, the program asks you for the cell where you will place the bomb.
Write in English layout, in uppercase (capital) letters.
The bot also selects a cell for the bomb.
Then you take turns selecting a cell to check if there is a bomb there.
Enjoy the game!""")
manual_text.config(state=tk.DISABLED)
button_main = tk.Button(root, text = 'Main Menu', command= start_window)

b_A = tk.Button(root, text= 'A', command=lambda: press('A'))
b_B = tk.Button(root, text= 'B', command=lambda: press('B'))
b_C = tk.Button(root, text= 'C', command=lambda: press('C'))
b_D = tk.Button(root, text= 'D', command=lambda: press('D'))
b_E = tk.Button(root, text= 'E', command=lambda: press('E'))
b_F = tk.Button(root, text= 'F', command=lambda: press('F'))
b_G = tk.Button(root, text= 'G', command=lambda: press('G'))
b_H = tk.Button(root, text= 'H', command=lambda: press('H'))
b_I = tk.Button(root, text= 'I', command=lambda: press('I'))
b_J = tk.Button(root, text= 'J', command=lambda: press('J'))
b_K = tk.Button(root, text= 'K', command=lambda: press('K'))
b_L = tk.Button(root, text= 'L', command=lambda: press('L'))
b_M = tk.Button(root, text= 'M', command=lambda: press('M'))
b_N = tk.Button(root, text= 'N', command=lambda: press('N'))
b_O = tk.Button(root, text= 'O', command=lambda: press('O'))
b_P = tk.Button(root, text= 'P', command=lambda: press('P'))

b_A.config(width=5, height=2)
b_B.config(width=5, height=2)
b_C.config(width=5, height=2)
b_D.config(width=5, height=2)
b_E.config(width=5, height=2)
b_F.config(width=5, height=2)
b_G.config(width=5, height=2)
b_H.config(width=5, height=2)
b_I.config(width=5, height=2)
b_J.config(width=5, height=2)
b_K.config(width=5, height=2)
b_L.config(width=5, height=2)
b_M.config(width=5, height=2)
b_N.config(width=5, height=2)
b_O.config(width=5, height=2)
b_P.config(width=5, height=2)


label_bomb = tk.Label(root, text="Enter the location for the bomb:")
entry_bomb = tk.Entry(root)
laying_label = tk.Label(root, text = 'ABCD\nEFGH\nI J K L\nMNOP')
laying_button = tk.Button(root, text='Choose', command=opt_user)

start_window()

root.mainloop()