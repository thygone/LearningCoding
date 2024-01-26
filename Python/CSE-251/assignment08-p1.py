"""
Course: CSE 251 
Lesson Week: 09
File: assignment09-p1.py 
Author: Dane Selch

Purpose: Part 1 of assignment 09, finding a path to the end position in a maze

Instructions:
- Do not create classes for this assignment, just functions
- Do not use any other Python modules other than the ones included

"""
import math
from screen import Screen
from maze import Maze
import cv2
import sys

# Include cse 251 common Python files - Dont change
from cse251 import *

SCREEN_SIZE = 800
COLOR = (0, 0, 255)


# TODO add any functions



    

###########################
# -solve_path
# -takes the maze and returns a path
# -this is where I will start my threads. 
# It will act as a driver funcion 
# #########################
def solve_path(maze,start, path, color):
    """ Solve the maze and return the path found between the start and end positions.  
        The path is a list of positions, (x, y) """
    #self.start_pos = (0, 1)
    path = []
    solve_path_helper(maze, start[0], start[1], path)
    return path

def solve_path_helper(maze: Maze, x, y, path):
    #check if finished.
    finished = maze.at_end(x,y)
    if finished == True:
        return True
    #get all paths
    potential_paths = maze.get_possible_moves(x,y)
    #check each path if it is usable
    for row, col in potential_paths:
        usable = maze.can_move_here(row,col)
        if usable == True:
            maze.move(row,col, COLOR)
            path.append((row,col)f)
            if solve_path_helper(maze,row,col, path): return True 


def get_path(log, filename):
    """ Do not change this function """

    # create a Screen Object that will contain all of the drawing commands
    screen = Screen(SCREEN_SIZE, SCREEN_SIZE)
    screen.background((255, 255, 0))
    maze = Maze(screen, SCREEN_SIZE, SCREEN_SIZE, filename)
    
    path = solve_path(maze,maze.start_pos, [], 0)

    log.write(f'Number of drawing commands for = {screen.get_command_count()}')

    done = False
    speed = 1
    while not done:
        if screen.play_commands(speed): 
            key = cv2.waitKey(0)
            if key == ord('+'):
                speed = max(0, speed - 1)
            elif key == ord('-'):
                speed += 1
            elif key != ord('p'):
                done = True
        else:
            done = True

    return path


def find_paths(log):
    """ Do not change this function """

    files = ('verysmall.bmp', 'verysmall-loops.bmp', 
            'small.bmp', 'small-loops.bmp', 
            'small-odd.bmp', 'small-open.bmp', 'large.bmp', 'large-loops.bmp')

    log.write('*' * 40)
    log.write('Part 1')
    for filename in files:
        log.write()
        log.write(f'File: {filename}')
        path = get_path(log, filename)
        log.write(f'Found path has length          = {len(path)}')
    log.write('*' * 40)


def main():
    """ Do not change this function """
    sys.setrecursionlimit(5000)
    log = Log(show_terminal=True)
    find_paths(log)


if __name__ == "__main__":
    main()