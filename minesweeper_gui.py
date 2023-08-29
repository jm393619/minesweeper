import tkinter as tk
from tkinter import messagebox, ttk
from game import Game


root = tk.Tk()
geo_root = "300x300+450+50"
root.geometry(geo_root)
root.title("Minesweeper")
root.config(bg='#a9dec1')


def _quit():
    root.destroy()


def _game():
    global geo_root

    game_difficulty = {0: (8, 10), 1: (16, 40), 2: (20, 100)}

    game = Game(*game_difficulty[opt_var.get()])

    def beg():
        game_root.destroy()
        Game.pos_of_mines.clear()
        _game()

    geo = (root.winfo_x(), root.winfo_y())

    game_root = tk.Toplevel(root)
    game_root.geometry(f"+{geo[0]}+{geo[1]}")
    root.withdraw()
    img1 = tk.PhotoImage(file=r"sun.png")
    sun_button = tk.Button(game_root, image=img1, command=beg)
    sun_button.image = img1
    sun_button.pack(pady=(20, 0))

    def _return():
        geo = game_root.winfo_x(), game_root.winfo_y()
        Game.pos_of_mines = []
        game_root.destroy()
        root.geometry(f"300x300+{geo[0]}+{geo[1]}")
        root.deiconify()

    menu = tk.Menu(game_root)
    options = tk.Menu(game_root)
    game_root.config(menu=menu)
    menu.add_cascade(label='options', menu=options)
    options.add_command(label='Go back to main menu', command=_return)

    game.put_mines()
    game.check_what_number()

    # Create frame with board fields
    frame = tk.Frame(game_root, borderwidth=2, relief=tk.SOLID)
    frame.pack(pady=15, padx=30)

    # Create board fields as labels
    fields_labels = {}  # Dictionary containing board fields - keys: labels, values: position
    for i, l in enumerate(game.board, 1):
        for j, k in enumerate(l, 1):
            fields_labels[
                tk.Label(frame, text=f'  ', bg='#a9dec1', width='2', fg='black', borderwidth=2, relief=tk.SOLID,
                         font=(None, 15))] = f"{i}-{j}"

    fields_position = {x: y for y, x in fields_labels.items()}

    for i, j in fields_labels.items():
        q = j.split('-')
        i.grid(row=int(q[0]), column=int(q[1]))

    def fun(e):

        try:
            if e.widget['text'] == 'F':
                return None
            if e.widget['text'] != '  ':
                return None
        except tk.TclError:
            return None

        q = fields_labels[e.widget].split('-')

        a, b = int(q[0]) - 1, int(q[1]) - 1

        if game.board[a][b] == 'M':

            game_root.unbind('<Button-1>', bind1)
            game_root.unbind('<Button-3>', bind2)
            for i, j in game.pos_of_mines:
                fields_position[f"{i + 1}-{j + 1}"].configure(text='M', bg='red')

        else:
            game.fun(a, b)

            for i, j in enumerate(game.board1):
                for k, l in enumerate(j):
                    if game.board1[i][k] != '-':
                        fields_position[f"{i + 1}-{k + 1}"].configure(text=game.board1[i][k])

        if game.check_how_many(game.board1) <= game.n_mines:
            game_root.unbind('<Button-1>', bind1)
            game_root.unbind('<Button-3>', bind2)
            for i, j in game.pos_of_mines:
                fields_position[f"{i + 1}-{j + 1}"].configure(text='M', bg='green')
            messagebox.showinfo(title='Game Over', message='You have won')

    def fun1(e):
        d_aux = {'  ': 'F', 'F': "  "}
        try:
            e.widget.config(text=d_aux[e.widget['text']])
        except KeyError:
            return None

    bind1 = game_root.bind('<Button-1>', fun)
    bind2 = game_root.bind('<Button-3>', fun1)

    def fun():
        game_root.destroy()
        root.destroy()

    game_root.protocol('WM_DELETE_WINDOW', fun)


def _settings():

    geo = root.winfo_geometry()
    setting_root = tk.Toplevel(root)
    setting_root.geometry(geo)
    root.withdraw()

    def _return():
        geo = setting_root.winfo_geometry()
        setting_root.destroy()
        root.geometry(geo)
        root.deiconify()



    def fun():
        setting_root.destroy()
        root.destroy()

    setting_root.protocol('WM_DELETE_WINDOW', fun)

    label_frame = tk.LabelFrame(setting_root, text='Difficulty level')
    label_frame.pack(pady=(40, 20))

    ttk.Radiobutton(label_frame, text='Beginner', variable=opt_var, value=0).pack(anchor=tk.W, padx=(0, 40))
    ttk.Radiobutton(label_frame, text='Intermediate', variable=opt_var, value=1).pack(anchor=tk.W)
    ttk.Radiobutton(label_frame, text='Expert', variable=opt_var, value=2).pack(anchor=tk.W)

    button_q = tk.Button(setting_root, text='Quit', font=(None, 15), width=10, command=_return)
    button_q.pack(pady=(20, 0))


# variable which stores difficulty levels (radio buttons in setting frame)
opt_var = tk.IntVar(value=0)

button1 = tk.Button(root, text='New Game', font=(None, 15), width=10, command=_game)
button1.pack(pady=(40, 0))

button2 = tk.Button(root, text='Settings', font=(None, 15), width=10, command=_settings)
button2.pack(pady=(20, 0))

button3 = tk.Button(root, text='Quit', font=(None, 15), width=10, command=_quit)
button3.pack(pady=(20, 0))

root.mainloop()
