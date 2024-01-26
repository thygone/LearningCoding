"""
Course: CSE 251
Lesson Week: 09
File: assingnment.py
Author: Dane
Purpose: Process Task Files

Instructions:  See I-Learn

TODO

Add you comments here on the pool sizes that you used for your assignment and
why they were the best choices.

there was 4034 tasks made so I though that makeing about 75 each would be a good starting point
and that crashed my my visual studio code. so next I went to 10 each
I stuck with one as that did not crash visual studios code
final test. 

"""

from datetime import datetime, timedelta
import requests
import multiprocessing as mp
from matplotlib.pylab import plt
import numpy as np
import glob
import math 

# Include cse 251 common Python files - Dont change
from cse251 import *

TYPE_PRIME  = 'prime'
TYPE_WORD   = 'word'
TYPE_UPPER  = 'upper'
TYPE_SUM    = 'sum'
TYPE_NAME   = 'name'

# Global lists to collect the task results
result_primes = []
result_words = []
result_upper = []
result_sums = []
result_names = []

# number of processes per pool
Prime_procs = 3 # just makes it faster
Words_procs = 3 # this is slow and is resource bound
Text_procs = 1 # this will be fast
Sums_procs = 2 # this is not a time consuming process
Names_procs = 4 # this is our biggest time consuming process as it has to go to a server
def is_prime(n: int):
    """Primality test using 6k+-1 optimization.
    From: https://en.wikipedia.org/wiki/Primality_test
    """
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
 
def task_prime(value):
    """
    Use the is_prime() above
    Add the following to the global list:
        {value} is prime
            - or -
        {value} is not prime
    """
    #get global
    global result_primes
    #find out if value is prime or not
    if is_prime(value):
        result_primes.append(f'{value} is prime')
    else:
        result_primes.append(f'{value} is not prime')    

def task_word(word):
    """
    search in file 'words.txt'
    Add the following to the global list:
        {word} Found
            - or -
        {word} not found *****
    """
    #get the global
    global result_words
    #bool that returns true only if we find the word
    found = False
    #open file
    f = open('words.txt')
    # read file word by word
    for line in f:
        for wd in line:
            #if any word matches what we have then break loop and 
            #     return true 
            if word == wd:
                found = True 
                break
    #close file
    f.close()
    #check if word was found
    if found:
        result_words.append(f'{word} Found')
    else:
        result_words.append(f'{word} not found *****')
    

def task_upper(text):
    """
    Add the following to the global list:
        {text} ==>  uppercase version of {text}
    """
    #get global
    global result_upper
    #add uppercase version of text to 
    result_upper.append(f'{text} =>> {str.upper(text)}')


def task_sum(start_value, end_value):
    """
    Add the following to the global list:
        sum of {start_value:,} to {end_value:,} = {total:,}
    """
    #get global of sums
    global result_sums
    # add sum of values to results
    result_sums.append(f'sum of {start_value} to {end_value} = {sum(range(start_value,end_value))}')


def task_name(url):
    """
    use requests module
    Add the following to the global list:
        {url} has name <name>
            - or -
        {url} had an error receiving the information
    """
    #get the global
    global result_names
    #request from the URL
    response = requests.get(url)
    # check if response is in a json format
    if response.status_code == 200:
        answer = response.json()
        name = answer['name']
        sting = f'{url} has name {name}' # a string but without the r is a sting
    else:
        sting = f'{url} had an error recieving teh information' 
    # add whatever you get to the Name results list
    result_names.append(sting)    


def main():
    log = Log(show_terminal=True)
    log.start_timer()

    # TODO Create process pools
    
    primin = mp.Pool(processes=Prime_procs)
    wordin = mp.Pool(processes=Words_procs)
    textin = mp.Pool(processes=Text_procs)
    summin = mp.Pool(processes=Sums_procs)
    namein = mp.Pool(processes=Names_procs)

    wordin.apply_async(processes=Prime_procs)
    textin.apply_async(processes=Prime_procs)
    summin.apply_async(processes=Prime_procs)
    namein.apply_async(processes=Prime_procs)

    count = 0
    task_files = glob.glob("*.task")
    for filename in task_files:
        # print()
        # print(filename)
        task = load_json_file(filename)
        print(task)
        count += 1
        task_type = task['task']
        if task_type == TYPE_PRIME:
            primin.apply_async(task_prime, args=(task['Value']))
            
        elif task_type == TYPE_WORD:
            #for a non callback version
            '''
            results_words_future.append(wordin.apply_async(task_word, args=(task['word'])))
            '''
            wordin.apply_async(task_word, args=(task['word']))
        elif task_type == TYPE_UPPER:
            task_upper(task['text'])
        elif task_type == TYPE_SUM:
            task_sum(task['start'], task['end'])
        elif task_type == TYPE_NAME:
            task_name(task['url'])
        else:
            log.write(f'Error: unknown task type {task_type}')

    # TODO start and wait pools   
    primin.close()
    wordin.close()
    textin.close()
    summin.close()
    namein.close()

    primin.join()
    wordin.join()
    textin.join()
    summin.join()
    namein.join()
    # do something like this if you don't want to use a callback function
    '''
    def get_results(results : AsyncResult): #results here is a future 
        return results.get()

    result_primes = list(map(get_results, result_primes_futures))
    reults_words = ...
    ...
    '''
    # Do not change the following code (to the end of the main function)
    def log_list(lst, log):
        for item in lst:
            log.write(item)
        log.write(' ')
    
    log.write('-' * 80)
    log.write(f'Primes: {len(result_primes)}')
    log_list(result_primes, log)

    log.write('-' * 80)
    log.write(f'Words: {len(result_words)}')
    log_list(result_words, log)

    log.write('-' * 80)
    log.write(f'Uppercase: {len(result_upper)}')
    log_list(result_upper, log)

    log.write('-' * 80)
    log.write(f'Sums: {len(result_sums)}')
    log_list(result_sums, log)

    log.write('-' * 80)
    log.write(f'Names: {len(result_names)}')
    log_list(result_names, log)

    log.write(f'Number of Primes tasks: {len(result_primes)}')
    log.write(f'Number of Words tasks: {len(result_words)}')
    log.write(f'Number of Uppercase tasks: {len(result_upper)}')
    log.write(f'Number of Sums tasks: {len(result_sums)}')
    log.write(f'Number of Names tasks: {len(result_names)}')
    log.stop_timer(f'Finished processes {count} tasks')

if __name__ == '__main__':
    main()
