#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sam Reeves
samtreeves@gmail.com
10/02/2020

Some basic unit tests for orderSandwich.py

"""
import orderSandwich
import unittest

class SandwichTests(unittest.TestCase):
    def test_time_formatting(self):
        result = calculateTime()
        self.assertTrue(type(result) == str)
        
    def test_make_time(self):
        initial_time = schedule_time
        makeSandwich()
        self.assertEqual(initial_time+60, schedule_time)
        
    def test_serve_time(self):
        initial_time = schedule_time
        serveSandwich()
        self.assertEqual(initial_time+30, schedule_time)
        
    def test_break_time(self):
        initial_time = schedule_time
        takeBreak()
        self.assertEqual(initial_time+60, schedule_time)
        
    def test_make_sequence_number(self):
        initial_number = sequence_number
        makeSandwich()
        self.assertEqual(initial_number+1, sequence_number)
        
    def test_serve_sequence_number(self):
        initial_number = sequence_number
        serveSandwich()
        self.assertEqual(initial_number+1, sequence_number)
        
    def test_break_sequence_number(self):
        initial_number = sequence_number
        takeBreak()
        self.assertEqual(initial_number+1, sequence_number)

if __name__ == '__main__':
    unittest.main()