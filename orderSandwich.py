#!usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sam Reeves
samtreeves@gmail.com
10/02/2020

This code is a challenge from a recruiter.  It is supposed to simulate a
fast food scenario with some specifications.

The script must be able to:
    * Take orders for sandwiches
    * Sequence and schedule the orders (1 minute to make, 30s to serve)
    * Output the schedule
    * Output an updated scheduel when an order is taken

Each item in the schedule must contain:
    * Sequence number
    * Time (in minutes, seconds)
    * Task
    * Order number
    
sample input:
    order(2)
    
sample output:
    1. 0:00 make sandwich 1
    2. 1:00 serve sandwich 1
    3. 1:30 make sandwich 2
    4. 2:30 serve sandwich 2
    
"""

schedule = []
sequence_number = 1
order_number = 1
schedule_time = 0


def calculateTime():
    global schedule_time
    
    # reset minutes and seconds every hour
    if schedule_time >= 3600:
        schedule_time -= 3600
    
    # calculate minutes and seconds
    minutes = schedule_time // 60
    seconds = schedule_time % 60

    # create output padding
    min_string = str(minutes).zfill(2)
    sec_string = str(seconds).zfill(2)
    
    return min_string + ":" + sec_string
    
def makeSandwich():
    global schedule_time, order_number, sequence_number
    
    # add the item to the schedule
    item = str(sequence_number) + ". " + calculateTime() + " make sandwich " + str(order_number)
    schedule.append(item)
    
    # update values for next item
    schedule_time += 60
    order_number += 1
    sequence_number += 1
    
def serveSandwich():
    global schedule_time, order_number, sequence_number
    
    # add item to the schedule
    item = str(sequence_number) + ". " + calculateTime() + " serve sandwich " + str(order_number)
    schedule.append(item)
    
    # update values for next item
    schedule_time += 30
    sequence_number += 1

def takeBreak():
    global schedule_time, order_number, sequence_number
    
    # record break time
    item = str(sequence_number) + ". " + calculateTime() + " take a well-earned break!"
    schedule.append(item)
    
    # update values for next item
    schedule_time += 60
    sequence_number += 1
    
def outputSchedule():
    for item in schedule:
        print(item)
    
def order(n=1):
    for sandwich in range(n):
        makeSandwich()
        serveSandwich()
    takeBreak()
    outputSchedule()
    