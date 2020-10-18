#!/usr/bin/python
# -*- coding:utf-8 -*-
import numpy
import secrets
import threading
import time
import random


class Thread(threading.Thread):
    def __init__(self, thread_name, thread_id):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.thread_id = thread_id


def put_down(chop1, chop2):
    if chop1.locked():
        chop1.release()
        print("release first")
    if chop2.locked():
        chop2.release()
        print("release second") #release wird noch nicht vernünftig übernommen, evtl chopsticks-array als objekt definieren und dort eine update-methode einbauen


def pick_up(chop1, chop2):
    if not chop1.locked() and not chop2.locked():
        chop1.acquire()
        chop2.acquire()
        return True
    else:
        return False
        #wenn beide erfolgreich aufgehoben -> state in eating setzen, sonst auf hungry (wait lassen)

    #chop1.release()

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
        chopsticks.append(threading.Lock()) # is equal to threading.Semaphore(1)
        philosophers.append(Thread("Philosopher " + str(i), i))
        philosophers[i].start()
        situations.update({philosophers[i]: states[0]})
        print("Philosopher " + str(philosophers[i].thread_id) + " is " + str(situations.get(philosophers[i])))
    time.sleep(3)

    while True:
        time.sleep(random.randint(1, 5))
        current_p = numpy.random.choice(philosophers)
        print(str(current_p.thread_name) + " is " + str(situations.get(current_p)))
        '''
        if a philosopher is hungry, he*she tries to pick up the two adjacent chopsticks
        '''

        if situations.get(current_p) == states[0]:
            situations[current_p] = states[1]
        elif situations.get(current_p) == states[1]:
            if pick_up(chopsticks[current_p.thread_id], chopsticks[(current_p.thread_id + 1) % n]):
                situations[current_p] = states[2]
                print(str(current_p.thread_name) + " has taken chopstick " + str(current_p.thread_id) + " and " + str((current_p.thread_id + 1) % n))
                print(str(current_p.thread_name) + " is " + str(situations[current_p]))
            else:
                print(str(current_p.thread_name) + " needs " + str(current_p.thread_id) + " and " + str((current_p.thread_id + 1) % n) + " to eat")
        else:
            put_down(chopsticks[philosophers[i].thread_id], chopsticks[(philosophers[i].thread_id + 1) % n])
            print(str(current_p.thread_name) + " has put down the sticks")
            situations[current_p] = states[0]


if __name__ == '__main__':
    main()