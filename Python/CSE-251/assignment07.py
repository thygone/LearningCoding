"""
Course: CSE 251
Lesson Week: 07
File: assignment.py
Author: Dane Selch
Purpose: Processing Plant
Instructions:
- Implement the classes to allow gifts to be created.
"""

from asyncio.windows_utils import pipe
import random
import multiprocessing as mp
import os.path
import time
import datetime

# Include cse 251 common Python files - Don't change
from cse251 import *

CONTROL_FILENAME = 'settings.txt'
BOXES_FILENAME   = 'boxes.txt'

# Settings consts
MARBLE_COUNT = 'marble-count'
CREATOR_DELAY = 'creator-delay'
BAG_COUNT = 'bag-count'
BAGGER_DELAY = 'bagger-delay'
ASSEMBLER_DELAY = 'assembler-delay'
WRAPPER_DELAY = 'wrapper-delay'

# No Global variables

class Bag():
    """ bag of marbles - Don't change """

    def __init__(self):
        self.items = []

    def add(self, marble):
        self.items.append(marble)

    def get_size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


class Gift():
    """ Gift of a large marble and a bag of marbles - Don't change """

    def __init__(self, large_marble, marbles):
        self.large_marble = large_marble
        self.marbles = marbles

    def __str__(self):
        marbles = str(self.marbles)
        marbles = marbles.replace("'", "")
        return f'Large marble: {self.large_marble}, marbles: {marbles[1:-1]}'


class Marble_Creator(mp.Process):
    """ This class "creates" marbles and sends them to the bagger """

    colors = ('Gold', 'Orange Peel', 'Purple Plum', 'Blue', 'Neon Silver', 
        'Tuscan Brown', 'La Salle Green', 'Spanish Orange', 'Pale Goldenrod', 'Orange Soda', 
        'Maximum Purple', 'Neon Pink', 'Light Orchid', 'Russian Violet', 'Sheen Green', 
        'Isabelline', 'Ruby', 'Emerald', 'Middle Red Purple', 'Royal Orange', 'Big Dip O’ruby', 
        'Dark Fuchsia', 'Slate Blue', 'Neon Dark Green', 'Sage', 'Pale Taupe', 'Silver Pink', 
        'Stop Red', 'Eerie Black', 'Indigo', 'Ivory', 'Granny Smith Apple', 
        'Maximum Blue', 'Pale Cerulean', 'Vegas Gold', 'Mulberry', 'Mango Tango', 
        'Fiery Rose', 'Mode Beige', 'Platinum', 'Lilac Luster', 'Duke Blue', 'Candy Pink', 
        'Maximum Violet', 'Spanish Carmine', 'Antique Brass', 'Pale Plum', 'Dark Moss Green', 
        'Mint Cream', 'Shandy', 'Cotton Candy', 'Beaver', 'Rose Quartz', 'Purple', 
        'Almond', 'Zomp', 'Middle Green Yellow', 'Auburn', 'Chinese Red', 'Cobalt Blue', 
        'Lumber', 'Honeydew', 'Icterine', 'Golden Yellow', 'Silver Chalice', 'Lavender Blue', 
        'Outrageous Orange', 'Spanish Pink', 'Liver Chestnut', 'Mimi Pink', 'Royal Red', 'Arylide Yellow', 
        'Rose Dust', 'Terra Cotta', 'Lemon Lime', 'Bistre Brown', 'Venetian Red', 'Brink Pink', 
        'Russian Green', 'Blue Bell', 'Green', 'Black Coral', 'Thulian Pink', 
        'Safety Yellow', 'White Smoke', 'Pastel Gray', 'Orange Soda', 'Lavender Purple',
        'Brown', 'Gold', 'Blue-Green', 'Antique Bronze', 'Mint Green', 'Royal Blue', 
        'Light Orange', 'Pastel Blue', 'Middle Green')

    def __init__(self, pipe, max, delay):
        mp.Process.__init__(self)
        # TODO Add any arguments and variables here
        self.marble_count = 0
        self.pipe = pipe
        self.marble_max = 14
        self.DELAY = delay

    def run(self):
        '''
        for each marble:
            send the marble (one at a time) to the bagger
              - A marble is a random name from the colors list above
            sleep the required amount
        Let the bagger know there are no more marbles
        ''' 
        i = 0
        while self.marble_count < self.marble_max:
            i +=1
            print(f'maker {i}')
            self.pipe.send(random.choice(self.colors))              # send random color down the pipe
            self.marble_count += 1              # incrament by one to the next marble
            time.sleep(self.DELAY)
        # the closing tag will transfer from here all the way to the wrapper


class Bagger(mp.Process):
    """ Receives marbles from the marble creator, then there are enough
        marbles, the bag of marbles are sent to the assembler """
    def __init__(self, R_pipe, S_pipe,count_max, delay):
        mp.Process.__init__(self)
        # TODO Add any arguments and variables here
        self.R_pipe = R_pipe    # pipe to recieve from
        self.S_pipe = S_pipe    # pipe to send to
        self.DELAY = delay
        self.bag_count = count_max

    def run(self):
        '''
        while there are marbles to process
            collect enough marbles for a bag
            send the bag to the assembler
            sleep the required amount
        tell the assembler that there are no more bags
        '''
        i = 0
        Gift_bag = Bag() 
        while i < 14:
            i+=1
            print(f'bagger {i}')
            # turn thin into a loop that will quite when told to stop
                                   # get a bag
            marble = self.R_pipe.recv()          # get marble
            Gift_bag.add(marble)                 # put marble in bag
            if Gift_bag.get_size() == self.bag_count:    # if the bag is as full as the file wants it to be
                self.S_pipe.send(Gift_bag)          # send it to assembler
            # when this ends send the terminate command to Assembler
            
            #delay
            time.sleep(self.DELAY)



class Assembler(mp.Process):
    """ Take the set of marbles and create a gift from them.
        Sends the completed gift to the wrapper """
    marble_names = ('Lucky', 'Spinner', 'Sure Shot', 'The Boss', 'Winner', '5-Star', 'Hercules', 'Apollo', 'Zeus')

    def __init__(self, R_pipe, S_pipe, delay):
        mp.Process.__init__(self)
        # TODO Add any arguments and variables here
        self.R_pipe = R_pipe
        self.S_pipe = S_pipe
        self.DELAY = delay

    def run(self):
        '''
        while there are bags to process
            create a gift with a large marble (random from the name list) and the bag of marbles
            send the gift to the wrapper
            sleep the required amount
        tell the wrapper that there are no more gifts
        '''
        i = 0
        while True:
            i+=1
            print(f'assembler {i}')
            Gift_bag = self.R_pipe.recv()        # get bag from bagger
            print(Gift_bag)
            Big_marble = random.choice(self.marble_names)  #get Big marble
            Full_gift = Gift(Big_marble, Gift_bag)  #make gift
            #self.S_pipe.send(Full_gift)             #send gift to next Wrapper
            
            #delay
            time.sleep(self.DELAY)
# when this ends send the terminate command to Wrapper

        
        


class Wrapper(mp.Process):
    """ Takes created gifts and wraps them by placing them in the boxes file """
    def __init__(self, Pipe, FileName, delay):
        mp.Process.__init__(self)
        # TODO Add any arguments and variables here
        self.Gift_count = 0     # keep track of all made gifts
        self.Pipe = Pipe        # pipe to recieve the gift
        self.FileName = FileName
        self.DELAY = delay
    def run(self):
        '''
        open file for writing
        while there are gifts to process
            save gift to the file with the current time
            sleep the required amount
        '''
        pass
        i = 0
        if os.path.exists(self.FileName):
                f= open(self.FileName, 'w')
        else:
                f= open(self.FileName, 'x')
        while True:
            i+=1
            f= open(self.FileName, 'w')
            print(f'wrapper {i}')
                #is there a box file already present?
            
            Full_gift = self.Pipe.recv()         #get gift
            #write gift to file.
            f.write(Full_gift.__str__())
            self.Gift_count += 1                    # the gift count increases with each gift.
            
            #delay
            time.sleep(self.DELAY)
            f.close()

def display_final_boxes(filename, log):
    """ Display the final boxes file to the log file -  Don't change """
    if os.path.exists(filename):
        log.write(f'Contents of {filename}')
        with open(filename) as boxes_file:
            for line in boxes_file:
                log.write(line.strip())
    else:
        log.write_error(f'The file {filename} doesn\'t exist.  No boxes were created.')



def main():
    """ Main function """

    log = Log(show_terminal=True)

    log.start_timer()

    # Load settings file
    settings = load_json_file(CONTROL_FILENAME)
    if settings == {}:
        log.write_error(f'Problem reading in settings file: {CONTROL_FILENAME}')
        return

    log.write(f'Marble count                = {settings[MARBLE_COUNT]}')
    log.write(f'settings["creator-delay"]   = {settings[CREATOR_DELAY]}')
    log.write(f'settings["bag-count"]       = {settings[BAG_COUNT]}') 
    log.write(f'settings["bagger-delay"]    = {settings[BAGGER_DELAY]}')
    log.write(f'settings["assembler-delay"] = {settings[ASSEMBLER_DELAY]}')
    log.write(f'settings["wrapper-delay"]   = {settings[WRAPPER_DELAY]}')

    # TODO: create Pipes between creator -> bagger -> assembler -> wrapper
    Maker, Bagger1 = mp.Pipe()
    Bagger2, AssemblerR = mp.Pipe() 
    AssemblerS, Wrapper1 = mp.Pipe() 
    # TODO create variable to be used to count the number of gifts

    # delete final boxes file
    if os.path.exists(BOXES_FILENAME):
        os.remove(BOXES_FILENAME)

    log.write('Create the processes')

    # TODO Create the processes (ie., classes above)
    #creat marbles
    Factory = Marble_Creator(Maker, 10,settings[CREATOR_DELAY])
    #create bagger    
    Bagman = Bagger(Bagger1,Bagger2,settings[BAG_COUNT],settings[BAGGER_DELAY])
    #create asselmbler
    Avenger_assemble = Assembler(AssemblerR, AssemblerS,settings[ASSEMBLER_DELAY])
    #create Wrapper
    Boxer = Wrapper(Wrapper1, BOXES_FILENAME,settings[WRAPPER_DELAY])
    
    # add all to a list
    Processes = [Factory,Bagman,Avenger_assemble,Boxer]
    log.write('Starting the processes')
    # TODO add code here
    
    for i in Processes:
        i.start()
    log.write('Waiting for processes to finish')
    # TODO add code here
    for i in Processes:
        i.join()
    display_final_boxes(BOXES_FILENAME, log)

    # TODO Log the number of gifts created.
    log.write(Boxer.Gift_count)


if __name__ == '__main__':
    main()

