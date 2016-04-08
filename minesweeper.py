import random


class Board():
    def __init__(self, size, num_mines):
        self.size = size
        self.num_mines = num_mines
        self.board = [[False for x in range(size)] for y in range(size)]

    def add_mines(self):
        point_list = self.get_mines()
        for point in point_list:
            self.board[point[0]][point[1]] = True

    def get_mines(self):
        point_list = []
        for x in range(self.num_mines):
            point = get_random_point(self.size)

            while point in point_list:
                point = get_random_point(self.size)

            point_list.append(point)

        return point_list

    def print_board(self):
        for row in self.board:
            print ' '.join(str(val) for val in row)


def main():
    board = Board(size=3, num_mines=2)
    board.add_mines()
    board.print_board()


def get_random_point(size):
    x = random.randint(0, size - 1)
    y = random.randint(0, size - 1)

    return (x, y)

if __name__ == "__main__":
    main()
