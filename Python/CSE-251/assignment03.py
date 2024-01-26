"""
Assignment done by Dane Selch
Course: CSE 251 
Lesson Week: 03
File: assignment.py 
Author: Brother Comeau

Purpose: Retrieve Star Wars details from a server

Instructions:

- Each API call must only retrieve one piece of information
- You are not allowed to use any other modules/packages except for the ones used
  in this assignment.
- Run the server.py program from a terminal/console program.  Simply type
  "python server.py"
- The only "fixed" or hard coded URL that you can use is TOP_API_URL.  Use this
  URL to retrieve other URLs that you can use to retrieve information from the
  server.
- You need to match the output outlined in the decription of the assignment.
  Note that the names are sorted.
- You are requied to use a threaded class (inherited from threading.Thread) for
  this assignment.  This object will make the API calls to the server. You can
  define your class within this Python file (ie., no need to have a seperate
  file for the class)
- Do not add any global variables except for the ones included in this program.

The call to TOP_API_URL will return the following Dictionary(JSON).  Do NOT have
this dictionary hard coded - use the API call to get this.  Then you can use
this dictionary to make other API calls for data.

{
   "people": "http://127.0.0.1:8790/people/", 
   "planets": "http://127.0.0.1:8790/planets/", 
   "films": "http://127.0.0.1:8790/films/",
   "species": "http://127.0.0.1:8790/species/", 
   "vehicles": "http://127.0.0.1:8790/vehicles/", 
   "starships": "http://127.0.0.1:8790/starships/"
}
"""

from contextlib import nullcontext
from ctypes import sizeof
from datetime import datetime, timedelta

import requests
import json
import threading

# Include cse 251 common Python files
from cse251 import *

# Const Values
TOP_API_URL = 'http://127.0.0.1:8790'

# Global Variables
call_count = 0


# TODO Add your threaded class definition here
class request_thread(threading.Thread):
  def __init__(self,url):
    threading.Thread.__init__(self)
    self.url = url
    self.response = {}

  def run(self):
    response = requests.get(self.url)
    if response.status_code == 200:
      self.response = response.json()
      
    else:
      print(f'your response came as {response.status_code}')


#function to get the different parts of the link
def getData(link):
  Data =  request_thread(fr'{link}')
  Data.start()
  Data.join()
  return (Data.response['name'])


class film:
  def __init__(self,URL,movie):
    self.movie = movie
    self.URL = f'{URL}6'
    #each section that I need to get.
    self.title = ''
    self.director =''
    self.producer =''
    self.release = ''
    self.people = []
    self.planets = []
    self.starships =[]
    self.vehicles = []
    self.species = []

  def getfilm(self):
    url = self.URL
    request = request_thread(fr'{url}')
    request.start()
    request.join()
    #if the response is not empty
    if request.response != {}:
      req = request.response

      self.title = req['title']
      self.director = req['director']
      self.producer = req['producer']
      self.release = req['release_date']
      #fill up all the data for the film
      for i in req['characters']:
        self.people.append(getData(i))
      for i in req['planets']:
        self.planets.append(getData(i))
      for i in req['species']:
        self.species.append(getData(i))
      for i in req['starships']:
        self.starships.append(getData(i))
      for i in req['vehicles']:
        self.vehicles.append(getData(i))
      return req
      ''' produces this mess
      'characters': ['http://127.0.0.1:8790/people/1/',
        'http://127.0.0.1:8790/people/2/', 'http://127.0.0.1:8790/people/3/',
        'http://127.0.0.1:8790/people/4/', 'http://127.0.0.1:8790/people/5/', 'http://127.0.0.1:8790/people/6/', 'http://127.0.0.1:8790/people/7/', 'http://127.0.0.1:8790/people/10/', 'http://127.0.0.1:8790/people/11/', 'http://127.0.0.1:8790/people/12/', 'http://127.0.0.1:8790/people/13/', 'http://127.0.0.1:8790/people/20/', 'http://127.0.0.1:8790/people/21/', 'http://127.0.0.1:8790/people/33/', 'http://127.0.0.1:8790/people/35/', 'http://127.0.0.1:8790/people/46/', 'http://127.0.0.1:8790/people/51/', 'http://127.0.0.1:8790/people/52/', 'http://127.0.0.1:8790/people/53/', 'http://127.0.0.1:8790/people/54/', 'http://127.0.0.1:8790/people/55/', 'http://127.0.0.1:8790/people/56/', 'http://127.0.0.1:8790/people/58/', 'http://127.0.0.1:8790/people/63/', 'http://127.0.0.1:8790/people/64/', 'http://127.0.0.1:8790/people/67/', 'http://127.0.0.1:8790/people/68/', 'http://127.0.0.1:8790/people/75/',
        'http://127.0.0.1:8790/people/78/', 'http://127.0.0.1:8790/people/79/', 'http://127.0.0.1:8790/people/80/', 'http://127.0.0.1:8790/people/81/', 'http://127.0.0.1:8790/people/82/', 'http://127.0.0.1:8790/people/83/']
        'planets': ['http://127.0.0.1:8790/planets/1/',
      ....
      '''
    else:
        return ''
  
  #make a thread to get the characherts in the movie

    req = request_thread(fr'{link}')
    print(f'\n{req.response}\n')  

  



# TODO Add any functions you need here

#write all the data to the log 
def writelog(log,name,li):
  count = len(li)
  log.write(f'  ')
  log.write(f'{name}  : {count}')
  st = ''
  for i in li:
    if i == li[0]:
      st = i
    else:
      st = st +', ' + i
  log.write(f'{st}')

#write the first four lines to the log, because they will be different
def writelog2(log,name,li):
  log.write(f'{name}  :{li}')
  
def main():
  log = Log(show_terminal=True)
  log.start_timer('Starting to retrieve data from the server')

  # TODO Retrieve Top API urls
  global TOP_API_URL
  starwars =requests.get(TOP_API_URL)
  if starwars.status_code ==200:
    URLS = starwars.json()
    '''
    {'people': 'http://127.0.0.1:8790/people/',
    'planets': 'http://127.0.0.1:8790/planets/',
    'films': 'http://127.0.0.1:8790/films/',
    'species': 'http://127.0.0.1:8790/species/',
    'vehicles': 'http://127.0.0.1:8790/vehicles/',
    'starships': 'http://127.0.0.1:8790/starships/'}
    '''
  # TODO Retireve Details on film 6
  url_film = URLS['films']
  print(f'{url_film}6')
  movie = film(url_film,5)
  movie.getfilm()
  # TODO Display results
  log.write(f'---------------------------------------------------------------------')
  writelog2(log,'Title',movie.title)
  writelog2(log,'Director',movie.director)
  writelog2(log,'Producer',movie.producer)
  writelog2(log,'Released',movie.release)
  writelog(log,'Characters',movie.people)
  writelog(log,'Planets',movie.planets)
  writelog(log,'Starships',movie.starships)
  writelog(log,'Vehicles',movie.vehicles)
  writelog(log,'Species',movie.species)
  

  
  log.write(f'---------------------------------------------------------------------')
  log.stop_timer('Total Time To complete')
  log.write(f'There were {call_count} calls to the server')
 
if __name__ == "__main__":
    main()
