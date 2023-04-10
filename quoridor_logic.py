import numpy as np
import matplotlib.pyplot as plt
import time

class Quoridor():

    def __init__(self) -> None:
        self.board = np.zeros([17, 17])
        self.white_pos = [8,0]
        self.init_black_pos = [8,16]
        self.black_pos = [8,0]
        self.board[self.white_pos[0], self.white_pos[1]] = 4
        self.board[self.init_black_pos[0], self.init_black_pos[1]] = 2
        self.walls = [[]]
        self.white_wall_num = 10
        self.black_wall_num = 10
        self.win = None
        self.running = True
        self.move_num = 0

    def is_won(self):
        if self.white_pos[1] == 16:
            self.win = 'white'
        
        elif self.black_pos[1] == 16:
            self.win = 'black'

        else: pass

    def flip_board(self):
        self.board = np.flipud(self.board)
        self.board = np.fliplr(self.board)
    
    def white_valid_move(self, move, wall_orient=None, wall_pos=None):
        valid = True
        if move == 'up':
            if self.white_pos[1] >= 16 or self.board[self.white_pos[0], self.white_pos[1] + 1] == 1:
                valid = False
                print('Move is not valid!')
                return valid
        elif move == 'down':
            if self.white_pos[1] <= 0 or self.board[self.white_pos[0], self.white_pos[1] - 1] == 1:
                valid = False
                print('Move is not valid!')
                return valid
        elif move == 'right':
            if self.white_pos[0] >= 16 or self.board[self.white_pos[0] + 1, self.white_pos[1]] == 1:
                valid = False
                print('Move is not valid!')
                return valid
        elif move == 'left':
            if self.white_pos[0] <= 0  or self.board[self.white_pos[0] - 1, self.white_pos[1]] == 1:
                valid = False
                print('Move is not valid!')
                return valid

        if move == 'wall':
            if wall_orient == 0:
                if wall_pos[0] >= 14 or wall_pos[0] <= 0:
                    valid = False
                    print('Wall is not valid!')
                    return valid

                for i in range(3):
                    if self.board[wall_pos[0] + i, wall_pos[1]] == 1:
                        valid = False
                        print('Wall is not valid!')
                        return valid
                    
            elif wall_orient == 1:
                if wall_pos[0] >= 14 and wall_pos[0] <= 0:
                    valid = False
                    print('Wall is not valid!')
                    return valid
                
                for i in range(3):
                    if self.board[wall_pos[0], wall_pos[1] + i] == 1:
                        valid = False
                        print('Wall is not valid!')
                        return valid
            
            if wall_pos[0] % 2 ==  wall_pos[1] % 2:
                valid = False
                print('Wall is not valid!')
                return valid
        self.move_num = self.move_num + 1
        return valid
    
    def black_valid_move(self, move, wall_orient=None, wall_pos=None):

        valid = True
        if move == 'up':
            if self.black_pos[1] >= 16 or self.board[self.black_pos[0], self.black_pos[1] + 1] == 1:
                if self.move_num <= 1:
                    valid = True
                    return True
                valid = False
                print('Move is not valid!')
                return valid
        elif move == 'down':
            if self.black_pos[1] <= 0 or self.board[self.black_pos[0], self.black_pos[1] - 1] == 1:
                valid = False
                print('Move is not valid!')
                return valid
        elif move == 'right':
            if self.black_pos[0] >= 16 or self.board[self.black_pos[0] + 1, self.black_pos[1]] == 1:
                valid = False
                print('Move is not valid!')
                return valid
        elif move == 'left':
            if self.black_pos[0] <= 0  or self.board[self.black_pos[0] - 1, self.black_pos[1]] == 1:
                valid = False
                print('Move is not valid!')
                return valid

        if move == 'wall':
            if wall_orient == 0:
                if wall_pos[0] >= 14 or wall_pos[0] <= 0:
                    valid = False
                    print('Wall is not valid!')
                    return valid

                for i in range(3):
                    if self.board[wall_pos[0] + i, wall_pos[1]] == 1:
                        valid = False
                        print('Wall is not valid!')
                        return valid
                    
            elif wall_orient == 1:
                if wall_pos[0] >= 14 and wall_pos[0] <= 0:
                    valid = False
                    print('Wall is not valid!')
                    return valid
                
                for i in range(3):
                    if self.board[wall_pos[0], wall_pos[1] + i] == 1:
                        valid = False
                        print('Wall is not valid!')
                        return valid
            
            if wall_pos[0] % 2 ==  wall_pos[1] % 2:
                valid = False
                print('Wall is not valid!')
                return valid
            
        self.move_num = self.move_num + 1
        return valid


    def white_move(self, move, wall_orient=None, wall_pos=None):

        if self.white_valid_move(move, wall_orient, wall_pos):

            self.board[self.white_pos[0], self.white_pos[1]] = 0

            if move == 'w':
                self.white_pos[1] += 2
            elif move == 's':
                self.white_pos[1] -= 2
            elif move == 'a':
                self.white_pos[0] -= 2
            elif move == 'd':
                self.white_pos[0] += 2
            elif move == 'b':
                if wall_orient == 0:
                    for i in range(3):
                        self.board[wall_pos[0] + i, wall_pos[1]] = 1
                if wall_orient == 1:
                    for i in range(3):
                        self.board[wall_pos[0], wall_pos[1] + i] = 1
                self.white_wall_num -= 1

            self.board[self.white_pos[0], self.white_pos[1]] = 4
            self.is_won()

    def black_move(self, move, wall_orient=None, wall_pos=None):

        self.flip_board()

        if self.black_valid_move(move, wall_orient, wall_pos):

            self.board[self.black_pos[0], self.black_pos[1]] = 0
            
            if move == 'w':
                self.black_pos[1] += 2
            elif move == 's':
                self.black_pos[1] -= 2 
            elif move == 'a':
                self.black_pos[0] -= 2 
            elif move == 'd':
                self.black_pos[0] += 2
            elif move == 'b':
                if wall_orient == 0:
                    for i in range(3):
                        self.board[wall_pos[0] + i, wall_pos[1]] = 1
                if wall_orient == 1:
                    for i in range(3):
                        self.board[wall_pos[0], wall_pos[1] + i] = 1
                self.black_wall_num -= 1

            self.board[self.black_pos[0], self.black_pos[1]] = 2
            self.is_won()

        self.flip_board()

    def print_board(self):
        fig, ax = plt.subplots(1,1)
        ax.imshow(self.board)
        plt.show()
        time.sleep(3.0)
        plt.close('all')

    def state(self):
        return self.board

    def main(self):
        while self.running == True:
            print('Game running')
            if self.move_num % 2 == 0:
                self.print_board()
                move = str(input('Choose white move:  '))
                if move == 'b':
                    wall_or = str(input('Choose wall orientation:   '))
                    wall_x = int(input('Wall x:   '))
                    wall_y = int(input('Wall y:   '))
                    self.white_move(move, wall_or, [wall_x, wall_y])
                else:
                    self.white_move(move)

            else:
                self.print_board()
                move = str(input('Choose black move:  '))
                if move == 'b':
                    wall_or = str(input('Choose wall orientation'))
                    wall_x = int(input('Wall x:   '))
                    wall_y = int(input('Wall y:   '))
                    self.black_move(move, wall_or, [wall_x, wall_y])
                else:
                    self.black_move(move)

            if self.win != None:
                print(f'{self.win} won the game!')
                self.running = False
                break

        return self.win
            

game = Quoridor()
game.main()





