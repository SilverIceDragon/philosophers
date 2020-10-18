#!/usr/bin/python
# -*- coding:utf-8 -*-
import threading
import time
import random


class Thread(threading.Thread):
    def __init__(self, thread_name, thread_id):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.thread_id = thread_id

    def run(self):
        print(str(self.thread_name) + " has joined the table")


def pick_up(chop1, chop2):
    print("test")
    #chop1.acquire()
    #print(chop1._value)
    #chop1.release()
    #print(chop1._value)
    #wenn Fehlschlag, muss Thread auf wait gesetzt werden


def main():
    n = 5
    philosophers = []
    chopsticks = []
    states = ["thinking", "hungry", "eating"]
    situations = {}

    '''
    create same amount of philosophers and chopsticks
    Semaphore(1): every chopstick may only be accessed by one philosopher
    '''
    for i in range(n):
        chopsticks.append(threading.Semaphore(1))
        philosophers.append(Thread("Philosopher " + str(i), i))
        philosophers[i].start()
        situations.update({philosophers[i]: states[0]})
        print("Philosopher " + str(philosophers[i].thread_id) + " is " + states[0])

    while True:
        time.sleep(random.randint(1, 3))
        current_p = random.choice(philosophers)
        '''
        if a philosopher is hungry, he*she tries to pick up the two adjacent chopsticks
        '''
        if situations.get(current_p) == states[0]:
            print(current_p.thread_name + " is hungry")
            #change state to 1 -> hungry
            pick_up(chopsticks[i], chopsticks[(i + 1) % n])


if __name__ == '__main__':
    main()