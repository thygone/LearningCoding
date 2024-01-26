"""
Course: CSE 251
Lesson Week: 10
File: Assignment.py
answeres: Dane Selch
"""

import time
import random
import multiprocessing as mp

# number of cleaning staff and hotel guests
CLEANING_STAFF = 2
HOTEL_GUESTS = 5
PARTIES_HELD_TOTAL = 0
#for adaption to multiple rooms later
ROOM_COUNT = 1
# Run program for this number of seconds
TIME = 60

#the room that will be used.
class Hotel_Room():
    def __init__(self) -> None:
        self.cleaned_count = 0
        self.praties_held_in_room = 0 # party count
        #is the room empty
        self.empty = True 
        # is the light on 
        self.lightsON = False
        self.occupancy = 0
    
    def turnOn(self):
        self.lightsON = True
        print(STARTING_PARTY_MESSAGE)

    def turnOFF(self):
        self.lightsON = False

    def leave_room(self):
        self.occupancy -=1
        if self.occupancy == 0:
            self.empty = True
            self.end_party()
    
    def end_party(self):
        print(STOPPING_PARTY_MESSAGE)
        self.praties_held_in_room += 1
        print(f'parties held {self.praties_held_in_room}')
        self.turnOFF()

    def fill_room(self):
        self.occupancy +=1
        self.empty = False

    def get_cleaned_count(self):
        return self.cleaned_count

    def get_party_count(self):
        return self.praties_held_in_room    

STARTING_PARTY_MESSAGE =  'Turning on the lights for the party vvvvvvvvvvvvvv'
STOPPING_PARTY_MESSAGE  = 'Turning off the lights  ^^^^^^^^^^^^^^^^^^^^^^^^^^'

STARTING_CLEANING_MESSAGE =  'Starting to clean the room >>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
STOPPING_CLEANING_MESSAGE  = 'Finish cleaning the room <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'

def cleaner_waiting():
    time.sleep(random.uniform(0, 2))

def cleaner_cleaning(id):
    print(f'Cleaner {id}')
    time.sleep(random.uniform(0, 2))

def guest_waiting():
    time.sleep(random.uniform(0, 2))

def guest_partying(id):
    print(f'Guest {id}')
    time.sleep(random.uniform(0, 1))

class cleaner(mp.Process):
    """
    do the following for TIME seconds
        cleaner will wait to try to clean the room (cleaner_waiting())
        get access to the room
        display message STARTING_CLEANING_MESSAGE
        Take some time cleaning (cleaner_cleaning())
        display message STOPPING_CLEANING_MESSAGE
    """
    def __init__(self, room : Hotel_Room, id, start_time, lock : mp.Lock) -> None:
        self.starting = start_time
        #set initial time
        time_taken = 0
        while time_taken < 60:
            #update the time that has been taken to clean.
            time_taken = time.time() - self.starting
            if room.empty == False:
                #if others are already inside the room wait a moment
                cleaner_waiting()
            else:
                #only let one cleaner in the room
                lock.acquire()
                print(STARTING_CLEANING_MESSAGE)
                cleaner_cleaning(id)
                print(STOPPING_CLEANING_MESSAGE)
                room.cleaned_count +=1
                print(f'times room was cleaned{room.cleaned_count}')
                #others can now enter the room
                lock.release()
                

class guest(mp.Process):
    """
    do the following for TIME seconds
        guest will wait to try to get access to the room (guest_waiting())
        get access to the room
        display message STARTING_PARTY_MESSAGE if this guest is the first one in the room
        Take some time partying (guest_partying())
        display message STOPPING_PARTY_MESSAGE if the guest is the last one leaving in the room
    """
    def __init__(self,room : Hotel_Room, id,start_time) -> None:
        self.starting = start_time
        time_taken = 0
        while time_taken < 60:
            time_taken = time.time() - self.starting
            guest_waiting()
            if room.empty == True: # first guest turn on lights
                room.turnOn()
   
            room.fill_room()
            guest_partying(id)
            

                
        room.leave_room()



def main():
    # Start time of the running of the program. 
    start_time = time.time()

    # TODO - add any variables, data structures, processes you need
    global PARTIES_HELD_TOTAL
    rooms = [] # to use in cause of multiple rooms later
    room = Hotel_Room()  
    Juanitors = [] # the cleaning staff
    party_goers = [] # the guests
    lock = mp.Lock()
    
    
    # TODO - add any arguments to cleaner() and guest() that you need
#making staff with id
    for x in range(CLEANING_STAFF):
        
        id = x+1
        janitor = mp.Process(target=cleaner, args=(room, id,start_time,lock))
        Juanitors.append(janitor)
    #making guests
    for x in range(HOTEL_GUESTS):
        id = x+1
        guests = mp.Process(target=guest, args=(room, id,start_time))
        party_goers.append(guests)


    
    #for multiple rooms
    #for r in rooms:
    #    PARTIES_HELD_TOTAL += r.praties_held_in_room
    
    #start the threads
    for c in Juanitors:
        c.start()
    for g in party_goers:
        g.start()
    for c in Juanitors:
        c.join()
    for g in party_goers:
        g.join() 
    cleaned_count = room.get_cleaned_count()
    party_count = room.get_party_count()
    print(f'Room was cleaned {cleaned_count} times, there were {party_count} parties')


if __name__ == '__main__':
    main()

