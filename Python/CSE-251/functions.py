"""
Course: CSE 251, week 12
File: common.py
Author: Dane Selch

Instructions:

Depth First Search
https://www.youtube.com/watch?v=9RHO6jU--GU

Breadth First Search
https://www.youtube.com/watch?v=86g8jAQug04


Requesting a family from the server:
family = Request_thread(f'{TOP_API_URL}/family/{id}')

Requesting an individual from the server:
person = Request_thread(f'{TOP_API_URL}/person/{id}')


You will lose 10% if you don't detail your part 1 
and part 2 code below

Describe how to speed up part 1

I could speed this up by finding a way to make all of my requests at once. 
This would take away the time I am waiting between the requests as there will not be a
need to stop and get information in the middle of the threads. 

I could have my initial thread made in the same place as the other threads to 
improve the way the code looks. idk if this would have an effect on the time though


Describe how to speed up part 2

I could try and find a way to minimize the number of times I request a person from the server so as to reduce waiting time on responses as well as 
make it so that a function only needs to grab one lock instead of two. if I could add the parents and children the same time then there wont be a need to 
grab, release and repeat.

10% Bonus to speed up part 3

the threads are all started at the same time, and it is fairly simmilar to the one above it. the best way I could think to maybe get it to be faster would
be to make a single thread go through the father's side the entire time that will spawn off threads for the mother's side, this would reduce the number of threads 
made as I would not make a new one for each parent, and at the same time keep the parallelism of the 2nd part of the project

"""
from common import *
import queue
global itter
itter = 0
#add one family at a time
global fam_lock 
fam_lock = threading.Lock()
#add one person at a time
global person_lock
person_lock = threading.Lock()
global thread_count
thread_count = 0
# -----------------------------------------------------------------------------
'''
Part 1
The function depth_fs_pedigree() will retrieve the family tree using a recursive algorithm.
-Your task is to use threads to make this function faster. There is no limit on the number of threads you can use.
-You must build the pedigree tree starting with the starting family id. You must write your program to handle different family information from the server (ie., number of families, number of children, etc.). A family might be missing a parent and the number of children is random.
-You must retrieve all individuals in a family and add them to the tree object. (ie., husband, wife and children)
Suggestion: get the function to work without using threads first.
Your goal is to execute part 1 in under 10 seconds for 6 generations'''
def depth_fs_pedigree(family_id, tree: Tree):
    # TODO - implement Depth first retrieval
    #tree lock
    global itter
    itter +=1
    if itter < 6:
        # no need to repeat a family already done.
        if not tree.does_family_exist(family_id):
            t = threading.Thread(target=build_tree_DFS, args=(family_id, tree))
            t.start()
            t.join()
    
    
#################################
# threaded function to build a tree
#   takes: id, tree, tree_lock
#   purpose: will add things to the tree class.  
#           family. response returns 
#               {'id': 5003732248, 'husband_id': 5003732248,
#                'wife_id': 5007473939, 'children': [#,#,#,#...]}   
#   going from child to parent

# check parent, request parent person, get family, repeat
def build_tree_DFS(id,tree:Tree):
    #get the lock
    global fam_lock
    global person_lock
    # threads for future use
    threads = []
    #get info on the family
    fam = get_family(id)
    fam_lock.acquire()    
    tree.add_family(fam)
    fam_lock.release()
    #get the parents.
    husband = get_person(fam.husband)
    wife = get_person(fam.wife)
    #add parents to tree
    person_lock.acquire()
    if not tree.does_person_exist(husband.id):
        print(f'adding father {husband.name}')
        tree.add_person(husband)
    if not tree.does_person_exist(wife.id):
        print(f'adding mother {wife.name}')
        tree.add_person(wife)
    person_lock.release()

    new_family_lines(husband.parents,wife.parents, tree)
    



    #add the children to the family
    person_lock.acquire()
    for c in fam.children:
        #no repeating children
        if not tree.does_person_exist(c):
            child = get_person(c)
            print(f'adding child {child.name}')
            tree.add_person(child)
    person_lock.release()
    
# request the family from the server, returns the response
def get_family(id):
    req = Request_thread(f'{TOP_API_URL}/family/{id}')
    req.start()
    req.join()
    return(Family(id,req.response))
    
# requst a person from the server and return the response
def get_person(id):
    
    req = Request_thread(f'{TOP_API_URL}/person/{id}')
    req.start()
    req.join()
    return (Person(req.response))

# transitional function to the new family the new family
def get_grandparents(p_id, tree: Tree):
    if p_id != None:
        g_parent = get_person(p_id)
        if g_parent.family != None :
            family = get_family(p_id)
            depth_fs_pedigree(family.id,tree)

# this function will make new threads for family lines
def new_family_lines(h_parent,w_parent, tree):
    #threads for each family line
    threads = []
    if h_parent != None:
        t = threading.Thread(target=get_grandparents, args=(h_parent, tree))
        threads.append(t)
    if w_parent != None:
        t = threading.Thread(target=get_grandparents, args=(w_parent, tree))
        threads.append(t)

    #start threads
    for i in threads:
        i.start()
    #join them
    for j in threads:
        j.join()
# -----------------------------------------------------------------------------
def breadth_fs_pedigree(family_id, tree2):
    # TODO - implement breadth first retrieval
    #get the starting person
    global thread_count
    person = Request_thread(f'{TOP_API_URL}/person/{id}')
    print('WARNING: BFS function not written')
    q = queue.Queue()
    q.put(family_id)
    threads = []
    while True:
        family_id = q.get()
        if family_id == None:
           break
        t = threading.Thread(target=create_family, args=(family_id,q,tree2))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()
        thread_count -= 1

def get_grandparents2(p_id,q):
    if p_id != None:
        g_parent = get_person(p_id)
        if g_parent.family != None :
            family = get_family(p_id)
            return(family.id)

def new_family_lines2(h_parent,w_parent, q):
    #threads for each family line
    ###########################3
    # end your program when both mom and dad have None for parents.
    #    lock this so only one thread can right to the queue at a time
    #####################
    if h_parent != None and w_parent != None:
        q.put(None)
    elif h_parent != None:
        q.put(get_grandparents2(h_parent,q))
        
    elif w_parent != None:
        q.put(get_grandparents2(w_parent,q))
        

def create_family(family_id, q, tree: Tree):
    #get the lock
    global fam_lock
    global person_lock
    #get info on the family
    fam_lock.acquire()
    fam = get_family(family_id)    
    tree.add_family(fam)
    fam_lock.release()
    
    #add the children to the family tree first
    person_lock.acquire()
    for c in fam.children:
        #no repeating children
        if not tree.does_person_exist(c):
            
            # ASSUMING WE DO NOT CARE ABOUT COUSINS!!!
            # IF YOU DO ADD IN THREADS HERE FOR THEM AS WELL
            child = get_person(c)
            print(f'adding child {child.name}')
            tree.add_person(child)
    person_lock.release()
    
    #get the parents second.
    husband = get_person(fam.husband)
    wife = get_person(fam.wife)
    #add parents to tree
    person_lock.acquire()
    if not tree.does_person_exist(husband.id):
        print(f'adding father {husband.name}')
        tree.add_person(husband)
    if not tree.does_person_exist(wife.id):
        print(f'adding mother {wife.name}')
        tree.add_person(wife)
    person_lock.release()
    #new family threads
    new_family_lines2(husband.parents,wife.parents, q)
    





# -----------------------------------------------------------------------------
def breadth_fs_pedigree_limit5(family_id, tree):
    # TODO - implement breadth first retrieval
    #      - Limit number of concurrent connections to the FS server to 5
    global thread_count
    person = Request_thread(f'{TOP_API_URL}/person/{id}')
    print('WARNING: BFS function not written')
    q = queue.Queue()
    q.put(family_id)
    threads = []
    while True:
        family_id = q.get()
        if family_id == None:
           break
        t = threading.Thread(target=create_family, args=(family_id,q,tree))
        t.start()
        threads.append(t)
        thread_count+=1
        while thread_count > 5:
            time.sleep(.2)
    
    for t in threads: t.join()