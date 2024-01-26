'''
Author: Dane Selch

Disclaimer: this is an assignment given to me, Dane Selch,
All I have done is the answers to the todo sections. any code inside
a "do not change" section belongs by an employee of Brigham Young University - Idaho

'''

# TODO import the appropriate threading and thread modules
import threading
from cse251 import Log

# TODO create a global counter
sum_global = 0
# TODO create a summing function that to target using the threading module.
def summin(name,a):
    global sum_global
    sum_global += a
    if a > 0:
        print(f"{name}, x = {a}, sum_golbal = {sum_global}")
        summin(name,(a-1))
    else:
        return(0)
    

# TODO create a class that extends the Thread class (make sure you use a constructor and have a run function)
class myThread(threading.Thread):
    def __init__(self,number):
        threading.Thread.__init__(self)
        self.sum = 0
        self.number = number
        print(f'{self.name} created\n')

    def summing(self):
        a = self.number-1
        if a > 0:
            self.sum += a
            print(f"x = {a}, sum = {self.sum}")
            self.number -= 1
            self.summing()
        else:
            print(f"x = {a}, total sum = {self.sum}")
    
    def run(self):
        print(self.summing())

# Note: don't change the name of this function or the unit test won't work
def create_threads(number, log):
    ''' number = the range to sum over, so if numbers equals 10, 
        then the sum will be 1 + 2 + ... + 9 + 10 = 45 
    '''
    log.write(f'number={number}')
    t1 = myThread(number)
    t2 = threading.Thread(target=summin, args=("thread2",(number-1),))
    t1.start()
    t1.join()
    global sum_global
    sum_global = 0
    t2.start()
    t2.join()
    # Two ways to create a thread:
    # 1) Create a class that extends Thread and then instantiate that class
    # 2) Instantiate Thread and give it a target and arguments
    sum_numbers_object = myThread(number)
    sum_numbers_object.start()
    
    sum_numbers_object.join()
    # LEAVE THIS so that your code can be tested against the unit test
    # (you can change the name of these variables)
    return sum_numbers_object.sum, sum_global

# Leave this so that you can run your code without needed to run the unit test.
# Once you believe it is working, run the unit test (challenge01_test.py) to 
# verify that it works against more numbers than 10.
if __name__ == '__main__':
    log = Log(show_terminal=True)
    create_threads(10, log)
