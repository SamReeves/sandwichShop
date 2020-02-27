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


class orderSandwich(object):

    def __init__(self):
        self.schedule = []
        self.sequence_number = 1
        self.order_number = 1
        self.schedule_time = 0

    def calculateTime(self):

        # reset minutes and seconds every hour
        if self.schedule_time >= 3600:
            self.schedule_time -= 3600

        # calculate minutes and seconds
        minutes = self.schedule_time // 60
        seconds = self.schedule_time % 60

        # create output padding
        min_string = str(minutes).zfill(2)
        sec_string = str(seconds).zfill(2)

        return min_string + ":" + sec_string

    def makeSandwich(self):

        # add the item to the schedule
        item = str(self.sequence_number) + ". " + self.calculateTime()\
            + " make sandwich " + str(self.order_number)
        self.schedule.append(item)

        # update values for next item
        self.schedule_time += 60
        self.order_number += 1
        self.sequence_number += 1

    def serveSandwich(self):

        # add item to the schedule
        item = str(self.sequence_number) + ". " + self.calculateTime()\
            + " serve sandwich " + str(self.order_number)
        self.schedule.append(item)

        # update values for next item
        self.schedule_time += 30
        self.sequence_number += 1

    def takeBreak(self):

        # record break time
        item = str(self.sequence_number) + ". " + self.calculateTime()\
            + " take a well-earned break!"
        self.schedule.append(item)

        # update values for next item
        self.schedule_time += 60
        self.sequence_number += 1

    def outputSchedule(self):
        for item in self.schedule:
            print(item)

    def order(self, n=1):
        for sandwich in range(n):
            self.makeSandwich()
            self.serveSandwich()
        self.takeBreak()
        self.outputSchedule()
