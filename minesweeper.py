import random

# Example: https://gist.github.com/mohd-akram/3057736


class Board():
    def __init__(self, size, num_mines):
        self.size = size
        self.num_mines = num_mines
        self.board = [[0 for x in range(size)] for y in range(size)]

    def add_mines(self):
        point_list = self.get_mines()
        for x, y in point_list:
            self.board[x][y] = 'X'
        self.add_numbers(point_list)

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

    def add_numbers(self, point_list):
        for i in range(self.size):
            for j in range(self.size):
                if not self.board[i][j] == 'X':
                    adjacent_points = self.get_adjacent_point_list(i, j)
                    count = len(adjacent_points.intersection(set(point_list)))
                    self.board[i][j] = count

    def get_adjacent_point_list(self, x, y):
        adjacent_offsets = [(i, j) for i in (0, 1, -1) for j in (0, 1, -1)
                            if not (j == i == 0)]
        adjacent_points = set((x+i, y+j) for i, j in adjacent_offsets
                              if not (x+i < 0 and x+i >= self.size
                                      and y+i < 0 and y+i >= self.size))
        return adjacent_points


def main():
    board = Board(size=6, num_mines=9)
    board.add_mines()
    board.print_board()


def get_random_point(size):
    x = random.randint(0, size - 1)
    y = random.randint(0, size - 1)

    return (x, y)

if __name__ == "__main__":
    main()
