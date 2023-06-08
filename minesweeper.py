from game import Game


class Minesweeper(Game):

    def __init__(self, n, n_mines):
        super().__init__(n, n_mines)

    def make_board(self):

        n = self.n

        board = []

        for raw in range(3 * n + 2):

            board.append([])

            if raw == 0:

                for col in range(n + 1):
                    if col == 0:
                        board[raw].append('   ')
                    else:
                        board[raw].append(f'  {col}   ')

            elif raw == 1:

                for col in range(n + 1):
                    if col == 0:
                        board[raw].append('  ')
                    elif col == 1:
                        board[raw].append('_______')
                    else:
                        board[raw].append('______')

            elif not (raw + 1) % 3:

                for col in range(n + 1):
                    if col == 0:
                        board[raw].append('  ')
                    elif col == 1:
                        board[raw].append('|     |')
                    else:
                        board[raw].append('     |')

            elif not raw % 3:

                for col in range(n + 1):
                    if col == 0:
                        board[raw].append(f'{raw // 3} ')
                    elif col == 1:
                        board[raw].append('|  -  |')
                    else:
                        board[raw].append('  -  |')

            elif not (raw - 1) % 3:

                for col in range(n + 1):
                    if col == 0:
                        board[raw].append('  ')
                    elif col == 1:
                        board[raw].append('|_____|')
                    else:
                        board[raw].append('_____|')

        self.game_board = board
        return self.game_board

    def next_fun(self):

        for k, i in enumerate(self.board1):

            for l, j in enumerate(i):

                if j != '-':
                    self.game_board[3 * (k + 1)][l + 1] = self.game_board[3 * (k + 1)][l + 1].replace('-', j)

    def game(self):

        self.make_board()
        self.put_mines()
        self.check_what_number()

        while g.check_how_many(self.board1) > self.n_mines:

            while True:

                a, b = input('Please, Select row and column number: ').split()
                try:
                    a, b = int(a) - 1, int(b) - 1
                except ValueError:
                    print('Please, select proper numbers.')
                    continue
                if a < len(self.board) and b < len(self.board[0]):
                    break
                else:
                    print(f'You should select numbers smaller than {self.n + 1}')

            if self.board[a][b] == 'M':

                for i, j in self.pos_of_mines:
                    self.change_position(self.board1, i, j, 'M')

                self.next_fun()
                self.get_board(self.game_board)
                print('!' * 50)
                print('YOU LOST!!!!!!')
                break

            else:
                self.fun(a, b)
                self.next_fun()
                self.get_board(self.game_board)
                print('!' * 80)

        else:
            print('YOU WON!!!!!!')

            for i, j in self.pos_of_mines:
                self.change_position(self.board1, i, j, '@')

            self.next_fun()
            self.get_board(self.game_board)


print('* '*21)
print('*' + ' '*39 + '*')
print('*\t\tWelcome to MineSweeper game     *')
print('*' + ' '*39 + '*')
print('* '*21)

print()
print('Possible difficulty levels:')
print('\t Easy (E): 5 mines and 5x5 board')
print('\t Hard (H): 10 mines and 8x8 board (Default Mode)')

while True:
    decision = input('Please select difficulty level: ')
    if decision in ('e', 'E'):
        g = Minesweeper(5, 5)
        break
    elif decision in ('h', 'H'):
        g = Minesweeper(8, 10)
        break
    else:
        print('Wrong input')

g.game()
