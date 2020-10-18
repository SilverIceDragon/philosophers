#!/usr/bin/python
# -*- coding:utf-8 -*-
import threading
import time
from random import randint


class Thread(threading.Thread):
    def __init__(self, thread_name, thread_id):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.thread_id = thread_id

    def run(self):
            print(str(self.thread_name) + " has joined the table")


def main():
    n = 5
    philosophers = []
    chopsticks = []
    states = ["thinking", "hungry", "eating"]

    '''
    create same amount of philosophers and chopsticks
    Semaphore(1): every chopstick may only be accessed by one philosopher
    '''
    for i in range(n):
        chopsticks.append(threading.Semaphore(1))
        philosophers.append(Thread("Philosopher "+str(i), i))
        philosophers[i].start()
        print("Philosopher " + str(philosophers[i].thread_id) + " is " + states[0])

    #while True:
     #   print(randint(1, 5))



#T = threading.Timer (Delay Duration, function, args = None, kwargs = None)

if __name__ == '__main__':
    main()

    #anfangs alle in denkend versetzen
    #while true -> jedes mal ein time Objekt verstreichen lassen (random)
    #wenn verstrichen, agiert jedes mal random ein philo

    #sem = threading.Semaphore()
    #obj.acquire()
    #obj.release

    #thread1 = Thread("Philo1", 1000)
    #thread2 = Thread("Philo2", 2000)

    #thread1.start()
    #thread2.start()