from random import randint

class SnakeGame:
    def __init__(self, size):
        self.size = size
        self.snake = new LinkedList((0, 0))
        self.board = [[BoardObject.NOTHING for x in range(size)] for y in range(size)]
        self.board = BoardObject.SNAKE
        self.place_food()

    def move(dir):
        # get new snake head

        # if newHead == food
        # add head to snake
        # add to board
        # new food + update food in board

        # else if newHead out of bounds or snake
        # end game

        # else
        # remove tail
        # add head
        # update board

    def place_food():
        while True:
            new_food_x = randint(0, self.size)
            new_food_y = randint(0, self.size))
            if self.board[new_food_x][new_food_y] == BoardObject.NOTHING:
                self.board[new_food_x][new_food_y] = (new_food_x, new_food_y)
                return



class LinkedList:
    def __init__(self, value):
        self.head = new LinkedListNode(value)
        self.tail = self.head

    def add_to_front(value):
        new_node = new LinkedListNode(value, self.head)
        self.head.prev = new_node
        self.head = new_node

    def remove_tail():
        self.tail.prev.next = None
        self.tail = self.tail.prev

class LinkedListNode:
    def __init__(self, value, next=None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev

class Direction:
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    UP = (0, 1)
    DOWN = (0, -1)

class BoardObject:
    NOTHING = 0
    SNAKE = 1
    FOOD = 2
