import random


class Game:

    def __init__(self, n, n_mines):
        self.n = n  # Dimension of a board
        self.n_mines = n_mines  # Number of mines
        self.board = []
        self.board1 = []

        for i in range(n):
            self.board.append(['-'] * n)
            self.board1.append(['-'] * n)

        # w list is used to store places in which there are zeros (used in fun function).
        self.w = []
        # self.counter = 0

    pos_of_mines = []

    @staticmethod
    def get_board(board):
        for i in board:
            print('   ' + ' '.join(i))

    @staticmethod
    def change_position(board, a, b, sgn):
        board[a][b] = sgn

    def put_mines(self):
        n = 0
        while n < self.n_mines:
            a, b = random.randint(0, self.n - 1), random.randint(0, self.n - 1)
            if self.board[a][b] != 'M':
                self.change_position(self.board, a, b, 'M')
                self.pos_of_mines.append((a, b))
                n += 1

    def check_what_number(self):
        for i, j in enumerate(self.board):
            for k, l in enumerate(j):

                aux_dict = {
                    i == 0 and k == 0: "[self.board[0][1], self.board[1][0], self.board[1][1]].count('M')",
                    i == 0 and 0 < k < len(self.board[0]) - 1: """[self.board[i][k - 1], self.board[i][k + 1],
                                                                self.board[i + 1][k - 1], self.board[i + 1][k],
                                                                self.board[i + 1][k + 1]].count('M')""",
                    i == 0 and k == len(self.board[0]) - 1: """[self.board[0][-2], self.board[1][-1],
                                                             self.board[1][-2]].count('M')""",
                    (len(self.board) - 1) > i > 0 == k: """[self.board[i - 1][k], self.board[i - 1][k + 1],
                                                         self.board[i][k + 1], self.board[i + 1][k + 1],
                                                         self.board[i + 1][k]].count('M')""",
                    0 < i < (len(self.board) - 1)
                    and 0 < k < len(self.board[0]) - 1: """[self.board[i - 1][k - 1], self.board[i - 1][k],
                                                          self.board[i - 1][k + 1], self.board[i][k - 1],
                                                          self.board[i + 1][k], self.board[i + 1][k + 1],
                                                          self.board[i + 1][k - 1], self.board[i][k + 1]].count('M')""",
                    0 < i < (len(self.board) - 1)
                    and k == len(self.board[0]) - 1: """[self.board[i - 1][k], self.board[i - 1][k - 1],
                                                        self.board[i][k - 1], self.board[i + 1][k - 1], 
                                                        self.board[i + 1][k]].count('M')""",
                    i == (len(self.board) - 1) and k == 0: """[self.board[i - 1][k], self.board[i - 1][k + 1],
                                                            self.board[i][k + 1]].count('M')""",
                    i == (len(self.board) - 1)
                    and 0 < k < len(self.board[0]) - 1: """[self.board[i][k - 1], self.board[i][k + 1],
                                                            self.board[i - 1][k - 1], self.board[i - 1][k], 
                                                            self.board[i - 1][k + 1]].count('M')""",
                    i == (len(self.board) - 1) and
                    k == len(self.board[0]) - 1: """[self.board[i][k - 1], self.board[i - 1][k],
                                                     self.board[i - 1][k - 1]].count('M')"""}

                if self.board[i][k] == 'M':
                    continue
                else:
                    d = eval(aux_dict[True])
                    self.change_position(self.board, i, k, str(d))

    def fun(self, n1, n2):

        if self.board[n1][n2] != '0':
            self.board1[n1][n2] = self.board[n1][n2]
            return None
        else:
            self.board1[n1][n2] = '0'
            self.w.append((n1, n2))

            c0, c1, c2 = (n1 - 1, n2 - 1), (n1 - 1, n2), (n1 - 1, n2 + 1)
            c7, c3 = (n1, n2 - 1), (n1, n2 + 1)
            c6, c5, c4 = (n1 + 1, n2 - 1), (n1 + 1, n2), (n1 + 1, n2 + 1)

            if n1 == 0:
                if n2 == 0:
                    aux_l_with_pos = []
                    if c3 not in self.w:
                        aux_l_with_pos.append(c3)
                    if c5 not in self.w:
                        aux_l_with_pos.append(c5)
                    if c4 not in self.w:
                        aux_l_with_pos.append(c4)

                elif n2 < len(self.board[0]) - 1:
                    aux_l_with_pos = []
                    if c7 not in self.w:
                        aux_l_with_pos.append(c7)
                    if c3 not in self.w:
                        aux_l_with_pos.append(c3)
                    if c6 not in self.w:
                        aux_l_with_pos.append(c6)
                    if c5 not in self.w:
                        aux_l_with_pos.append(c5)
                    if c4 not in self.w:
                        aux_l_with_pos.append(c4)

                else:
                    aux_l_with_pos = []
                    if c7 not in self.w:
                        aux_l_with_pos.append(c7)
                    if c6 not in self.w:
                        aux_l_with_pos.append(c6)
                    if c5 not in self.w:
                        aux_l_with_pos.append(c5)

                aux_l_with_fun = []

                for q in aux_l_with_pos:
                    aux_l_with_fun.append(self.fun(*q))
                return aux_l_with_fun

            elif n1 < len(self.board) - 1:
                if n2 == 0:
                    aux_l_with_pos = []
                    if c1 not in self.w:
                        aux_l_with_pos.append(c1)
                    if c2 not in self.w:
                        aux_l_with_pos.append(c2)
                    if c3 not in self.w:
                        aux_l_with_pos.append(c3)
                    if c5 not in self.w:
                        aux_l_with_pos.append(c5)
                    if c4 not in self.w:
                        aux_l_with_pos.append(c4)

                    aux_l_with_fun = []

                    for q in aux_l_with_pos:
                        aux_l_with_fun.append(self.fun(*q))
                    return aux_l_with_fun

                elif n2 == len(self.board[0]) - 1:
                    aux_l_with_pos = []
                    if c0 not in self.w:
                        aux_l_with_pos.append(c0)
                    if c1 not in self.w:
                        aux_l_with_pos.append(c1)
                    if c7 not in self.w:
                        aux_l_with_pos.append(c7)
                    if c6 not in self.w:
                        aux_l_with_pos.append(c6)
                    if c5 not in self.w:
                        aux_l_with_pos.append(c5)

                    aux_l_with_fun = []

                    for q in aux_l_with_pos:
                        aux_l_with_fun.append(self.fun(*q))
                    return aux_l_with_fun
            else:
                if n2 == 0:
                    aux_l_with_pos = []
                    if c1 not in self.w:
                        aux_l_with_pos.append(c1)
                    if c2 not in self.w:
                        aux_l_with_pos.append(c2)
                    if c3 not in self.w:
                        aux_l_with_pos.append(c3)

                elif n2 < len(self.board[0]) - 1:
                    aux_l_with_pos = []
                    if c0 not in self.w:
                        aux_l_with_pos.append(c0)
                    if c1 not in self.w:
                        aux_l_with_pos.append(c1)
                    if c2 not in self.w:
                        aux_l_with_pos.append(c2)
                    if c7 not in self.w:
                        aux_l_with_pos.append(c7)
                    if c3 not in self.w:
                        aux_l_with_pos.append(c3)

                else:
                    aux_l_with_pos = []
                    if c0 not in self.w:
                        aux_l_with_pos.append(c0)
                    if c1 not in self.w:
                        aux_l_with_pos.append(c1)
                    if c7 not in self.w:
                        aux_l_with_pos.append(c7)

                aux_l_with_fun = []

                for q in aux_l_with_pos:
                    aux_l_with_fun.append(self.fun(*q))
                return aux_l_with_fun

            if c0 == (0, 0):
                b1, b2 = c0
                self.board1[b1][b2] = self.board[b1][b2]

            if c1[0] == 0:
                b1, b2 = c1
                self.board1[b1][b2] = self.board[b1][b2]

            if c2 == (0, len(self.board[0]) - 1):
                b1, b2 = c2
                self.board1[b1][b2] = self.board[b1][b2]

            if c7[1] == 0:
                b1, b2 = c7
                self.board1[b1][b2] = self.board[b1][b2]

            if c3[1] == len(self.board[0]) - 1:
                b1, b2 = c3
                self.board1[b1][b2] = self.board[b1][b2]

            if c6 == (len(self.board) - 1, 0):
                b1, b2 = c6
                self.board1[b1][b2] = self.board[b1][b2]

            if c5[0] == len(self.board) - 1:
                b1, b2 = c5
                self.board1[b1][b2] = self.board[b1][b2]

            if c4 == (len(self.board) - 1, len(self.board[0]) - 1):
                b1, b2 = c4
                self.board1[b1][b2] = self.board[b1][b2]

            aux_l_with_pos = []

            for i in range(8):
                exec(f"if c{i} not in self.w: aux_l_with_pos.append(c{i})")

            aux_l_with_fun = []

            for q in aux_l_with_pos:
                aux_l_with_fun.append(self.fun(*q))
            return aux_l_with_fun

    @staticmethod
    def check_how_many(board):
        counter = 0

        for i in board:
            counter += i.count('-')

        return counter
