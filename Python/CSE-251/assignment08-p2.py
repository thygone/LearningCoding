"""
Course: CSE 251 
Lesson Week: 09
File: assignment09-p2.py 
Author: Dane Selch

Purpose: Part 2 of assignment 09, finding the end position in the maze

Instructions:
- Do not create classes for this assignment, just functions
- Do not use any other Python modules other than the ones included
- Each thread requires a different color by calling get_color()


This code is not interested in finding a path to the end position,
However, once you have completed this program, describe how you could 
change the program to display the found path to the exit position.

What would be your strategy?  
I would a global path object. each thread would localy record their own path (including any part of the path that is made
 by it's parent thread), once the end point is reached only that single thread would give it's path to the global variable.

Why would it work?
  This would work for a few reasons. first all dead end paths would never make it to the variable as it would all be dropped 
  along with the thread itself. This means that the only thread accessing this variable is the successful one. Additoinally
  the winning thread would not have to travers the whole maze as it will be given the missing parts from it's parent threads.


"""
import math
import threading 
from screen import Screen
from maze import Maze
import sys
import cv2

# Include cse 251 common Python files - Dont change
from cse251 import *

SCREEN_SIZE = 800
COLOR = (0, 0, 255)
COLORS = (
    (0,0,255),
    (0,255,0),
    (255,0,0),
    (255,255,0),
    (0,255,255),
    (255,0,255),
    (128,0,0),
    (128,128,0),
    (0,128,0),
    (128,0,128),
    (0,128,128),
    (0,0,128),
    (72,61,139),
    (143,143,188),
    (226,138,43),
    (128,114,250)
)

# Globals
current_color_index = 0
thread_count = 0
stop = False

def get_color():
    """ Returns a different color when called """
    global current_color_index
    if current_color_index >= len(COLORS):
        current_color_index = 0
    color = COLORS[current_color_index]
    current_color_index += 1
    return color


def solve_find_end(maze,start,path,threads):
    """ finds the end position using threads.  Nothing is returned """
    #self.start_pos = (0, 1)
    #reset globals
    global current_color_index 
    global thread_count 
    global stop 
    current_color_index = 0
    thread_count = 0    
    stop = False
    color = get_color()
    path = []
    #color first squar
    maze.move(start[0],start[1], color)
    solve_find_end_helper(maze,start[0],start[1],path, color)
    
    
def solve_find_end_helper(maze: Maze, x,y,path, color):
    #check if finished.
    global thread_count
    global stop
    # list to hold all threads
    threads = []
    # check if maze has finished.
    if maze.at_end(x,y):
        stop = True
    if stop:
        return False

    #get all paths
    potential_paths = maze.get_possible_moves(x,y)

    # do you have one path
    if len(potential_paths) == 0:
        return False
    #list of all possible moves in a double arrey    [[x1,y1],[x2,y2]]
    moves = []
    #check each path if it is usable
    for row, col in potential_paths:
        # save only the available options
        if maze.can_move_here(row,col): 
            moves.append([row, col]) 


    #always move forward if you can
    if len(moves) > 0:
        #move forward
        maze.move(moves[0][0],moves[0][1], color)
        solve_find_end_helper(maze, moves[0][0],moves[0][1], path, color)
        #make a thread for any other options available
        for i in moves:     
            #make thread as long as you can still move there
            if maze.can_move_here(i[0],i[1]):
                new_color = get_color()
                # make thread
                t = threading.Thread(target=solve_find_end_helper, args=(maze, i[0],i[1], path, new_color))
                #add to path
                maze.move(i[0],i[1], new_color)
                path.append((i[0],i[1])) # add position to path
                threads.append(t)
        for t in threads:
            #start threads
            t.start()
            thread_count += 1
        for t in threads:
            #wait for thread to finish
            t.join()
        if solve_find_end_helper(maze,row,col, path, color): return True 
        
    

          


def find_end(log, filename, delay):
    """ Do not change this function """

    global thread_count

    # create a Screen Object that will contain all of the drawing commands
    screen = Screen(SCREEN_SIZE, SCREEN_SIZE)
    screen.background((255, 255, 0))

    maze = Maze(screen, SCREEN_SIZE, SCREEN_SIZE, filename, delay=delay)
    visited = []
    solve_find_end(maze,maze.start_pos, visited, 0)

    log.write(f'Number of drawing commands = {screen.get_command_count()}')
    log.write(f'Number of threads created  = {thread_count}')

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



def find_ends(log):
    """ Do not change this function """

    files = (
        ('verysmall.bmp', True),
        ('verysmall-loops.bmp', True),
        ('small.bmp', True),
        ('small-loops.bmp', True),
        ('small-odd.bmp', True),
        ('small-open.bmp', False),
        ('large.bmp', False),
        ('large-loops.bmp', False)
    )

    log.write('*' * 40)
    log.write('Part 2')
    for filename, delay in files:
        log.write()
        log.write(f'File: {filename}')
        find_end(log, filename, delay)
    log.write('*' * 40)


def main():
    """ Do not change this function """
    sys.setrecursionlimit(5000)
    log = Log(show_terminal=True)
    find_ends(log)



if __name__ == "__main__":
    main()