# C2.5 ИТОГОВОЕ ПРАКТИЧЕСКОЕ ЗАДАНИЕ

# МОРСКОЙ БОЙ

# Внутренняя логика игры

from random import randint


class BoardOutException(Exception):
    def __str__(self):
        return 'BoardOutException: клетка находится вне поля, выберите другую'


class BoardUsedException(Exception):
    def __str__(self):
        return 'BoardUsedException: Вы уже стреляли в эту клетку'


class BoardWrongShipException(Exception):
    pass


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f'Dot{self.x}, {self.y}'


class Ship:
    def __init__(self, size, bow, direction):
        self.size = size
        self.bow = bow
        self.direction = direction
        self.lives = size

    @property
    def dots(self):
        ship_dots = []
        for i in range(self.size):
            cur_x = self.bow.x
            cur_y = self.bow.y

            if self.direction == 0:
                cur_x += i
            elif self.direction == 1:
                cur_y += i

            ship_dots.append(Dot(cur_x, cur_y))

        return ship_dots

    def shooten(self, shot):
        return shot in self.dots


class Board:
    def __init__(self, hid_parameter=False, size=6):
        self.hid_parameter = hid_parameter
        self.size = size
        self.wrecked_ships = 0
        self.busy_dots = []
        self.ships_on_board = []
        self.field = [['O'] * size for p in range(size)]

    def __str__(self):
        b = ''
        b += '  | 1 | 2 | 3 | 4 | 5 | 6 |'
        for i, row in enumerate(self.field):
            b += f'\n{i + 1} | ' + ' | '.join(row) + ' |'

        if self.hid_parameter:
            b = b.replace('¤', 'O')
        return b

    def add_ship(self, ship):
        for d in ship.dots:
            if self.out(d) or d in self.busy_dots:
                raise BoardWrongShipException()
        for d in ship.dots:
            self.field[d.x][d.y] = '¤'
            self.busy_dots.append(d)

        self.ships_on_board.append(ship)
        self.contour(ship)

    def contour(self, ship, verb=False):
        near = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1), (0, 0), (0, 1),
                (1, -1), (1, 0), (1, 1)]

        for d in ship.dots:
            for dx, dy in near:
                cur = Dot(d.x + dx, d.y + dy)
                if not(self.out(cur)) and cur not in self.busy_dots:
                    if verb:
                        self.field[cur.x][cur.y] = '.'
                    self.busy_dots.append(cur)

    def out(self, d):
        return not ((0 <= d.x < self.size) and (0 <= d.y < self.size))

    def shot(self, d):
        if self.out(d):
            raise BoardOutException()

        if d in self.busy_dots:
            raise BoardUsedException()

        self.busy_dots.append(d)

        for ship in self.ships_on_board:
            if d in ship.dots:
                ship.lives -= 1
                self.field[d.x][d.y] = 'X'
                if ship.lives == 0:
                    self.wrecked_ships += 1
                    self.contour(ship, verb=True)
                    print('Корабль уничтожен')
                    return False
                else:
                    print('Корабль ранен')
                    return True

        self.field[d.x][d.y] = '.'
        print('Мимо!')
        return False

    def begin(self):
        self.busy_dots = []


# Внешняя логика игры


class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    def ask(self):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat
            except Exception as e:
                print(e)


class User(Player):
    def ask(self):
        while True:
            cords = input('Ваш ход: ').split()

            if len(cords) != 2:
                print('Введите две координаты')
                continue

            x, y = cords

            if not(x.isdigit()) or not (y.isdigit()):
                print('Введите числа')
                continue

            x, y = int(x), int(y)

            return Dot(x - 1, y - 1)


class AI(Player):
    def ask(self):
        d = Dot(randint(0, 5), randint(0, 5))
        print(f'Ход компьютера: {d.x + 1} {d.y + 1}')
        return d


class Game:
    def __init__(self, size=6):
        self.size = size
        pl = self.random_board()
        co = self.random_board()
        co.hid_parameter = True

        self.ai = AI(co, pl)
        self.us = User(pl, co)

    def random_board(self):
        board = None
        while board is None:
            board = self.random_place()
        return board

    def random_place(self):
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = Board(size=self.size)
        attempts = 0
        for i in lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(i, Dot(randint(0, self.size), randint(0, self.size)), randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass
        board.begin()
        return board

    def greet(self):
        print('Добро пожаловать в игру морской бой. Введите поле, куда Вы хотите стрелять,'
              '\nпо формату x y, где x номер строки, а y - номер столбца.')

    def loop(self):
        num = 0
        while True:
            print('Доска игрока: ')
            print(self.us.board)
            print()
            print('Доска компьютера: ')
            print(self.ai.board)

            if num % 2 == 0:
                print()
                print('Ходит игрок')
                repeat = self.us.move()
            else:
                print()
                print('Ходит компьютер')
                repeat = self.ai.move()
            if repeat:
                num -= 1
            if self.ai.board.wrecked_ships == 7:
                print()
                print('Игрок выиграл!')
                break
            if self.us.board.wrecked_ships == 7:
                print()
                print('Компьютер выиграл!')
                break
            num += 1

    def start(self):
        self.greet()
        self.loop()


g = Game()
g.start()
