"""
Course: CSE 251
Lesson Week: 09
File: team2.py

Purpose: team activity - Dining philosophers problem

Problem statement

Five silent philosophers sit at a round table with bowls of spaghetti. Forks
are placed between each pair of adjacent philosophers.

Each philosopher must alternately think and eat. However, a philosopher can
only eat spaghetti when they have both left and right forks. Each fork can be
held by only one philosopher and so a philosopher can use the fork only if it
is not being used by another philosopher. After an individual philosopher
finishes eating, they need to put down both forks so that the forks become
available to others. A philosopher can only take the fork on their right or
the one on their left as they become available and they cannot start eating
before getting both forks.  When a philosopher is finished eating, they think 
for a little while.

Eating is not limited by the remaining amounts of spaghetti or stomach space;
an infinite supply and an infinite demand are assumed.

The problem is how to design a discipline of behavior (a concurrent algorithm)
such that no philosopher will starve

Instructions:

        **************************************************
        ** DO NOT search for a solution on the Internet **
        ** your goal is not to copy a solution, but to  **
        ** work out this problem.                       **
        **************************************************

- This is the same problem as last team activity.  However, you will implement a waiter.  
  When a philosopher wants to eat, it will ask the waiter if it can.  If the waiter 
  indicates that a philosopher can eat, the philosopher will pick up each fork and eat.  
  There must not be a issue picking up the two forks since the waiter is in control of 
  the forks and when philosophers eat.  When a philosopher is finished eating, it will 
  informs the waiter that he/she is finished.  If the waiter indicates to a philosopher
  that they can not eat, the philosopher will wait between 1 to 3 seconds and try again.

- You have Locks and Semaphores that you can use.
- Remember that lock.acquire() has an argument called timeout.
- philosophers need to eat for 1 to 3 seconds when they get both forks.  
  When the number of philosophers has eaten MAX_MEALS times, stop the philosophers
  from trying to eat and any philosophers eating will put down their forks when finished.
- philosophers need to think for 1 to 3 seconds when they are finished eating.  
- When a philosopher is not eating, it will think for 3 to 5 seconds.
- You want as many philosophers to eat and think concurrently.
- Design your program to handle N philosophers and N forks after you get it working for 5.
- Use threads for this problem.
- When you get your program working, how to you prove that no philosopher will starve?
  (Just looking at output from print() statements is not enough)
- Are the philosophers each eating and thinking the same amount?
- Using lists for philosophers and forks will help you in this program.
  for example: philosophers[i] needs forks[i] and forks[i+1] to eat
"""

import time
import threading
import random
PHILOSOPHERS = 5
MAX_MEALS = PHILOSOPHERS * 5


class Waiter():
  meals_served = 0
  eaten1 = 0
  eaten2 = 0
  eaten3 = 0
  eaten4 = 0
  eaten5 = 0 
  lock = threading.Lock()


  def ask_for_meal(self):
    if self.meals_served < MAX_MEALS:
      return True
    else:
      return False 

  def eat_meal(self,id):
    print(f"philosopher{id} eating")
    self.meals_served+=1
    if id == 1:
      self.eaten1 +=1
    elif id == 2:
      self.eaten2 +=1
    elif id == 3:
      self.eaten3 +=1
    elif id == 4:
      self.eaten4 +=1
    elif id == 5:
      self.eaten5 +=1

    time.sleep(random.randint(1,3))
    print(f"philosopher{id} putting down forks")
  
def think(id):
  print(f'\nphilosopher {id} thinking\n')
  time.sleep(random.randint(1,3))

def philosopher(waiter : Waiter,fork_L: threading.Lock(), fork_R:threading.Lock(),id):
  
  wait_time = random.randint(1,3)
  while waiter.ask_for_meal(): # is there a reason to pick up my 
    think(id) #digestion time
    if fork_L.acquire(timeout = 2):
      print(f"philosopher{id} grabing left fork")
      if fork_R.acquire(timeout = 2):
        print(f"philosopher{id} grabing right fork")
        waiter.lock.acquire()#only one person talks to waiter at a time
        if waiter.ask_for_meal(): #double check that there is food to eat
          waiter.eat_meal(id)
        waiter.lock.release()
        fork_R.release()
      fork_L.release()
  

def main():
  # TODO - create the waiter (A class would be best here)
  waiter = Waiter()
  # TODO - create the forks
  forks = []
  for fork in range(5):
    l = threading.Lock()
    forks.append(l)
  # TODO - create PHILOSOPHERS philosophers
  philo = [] # empty list to hold all philosophers. 
  for p in range(PHILOSOPHERS):
    person = threading.Thread(target=philosopher, args=(waiter,forks[p%5], forks[(p+1)%5], (p+1)))
    philo.append(person)
  # TODO - Start them eating and thinking
  for p in philo:
    p.start()
  for p in philo:
    p.join()
      
  print(f'philosopher 1 has eaten {waiter.eaten1} meals')
  print(f'philosopher 2 has eaten {waiter.eaten2} meals')
  print(f'philosopher 3 has eaten {waiter.eaten3} meals')
  print(f'philosopher 4 has eaten {waiter.eaten4} meals')
  print(f'philosopher 5 has eaten {waiter.eaten5} meals')

if __name__ == '__main__':
    main()
