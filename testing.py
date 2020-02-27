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


class BaseTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)

    def setUp(self):
        self.oS = orderSandwich.orderSandwich()
        pass

    def tearDown(self):
        pass


class sandwichTests(BaseTest):

    def __init__(self, *args, **kwargs):
        BaseTest.__init__(self, *args, **kwargs)
        self.controller = orderSandwich.orderSandwich()

    def test_time_formatting(self):
        result = self.oS.calculateTime()
        self.assertTrue(type(result) == str)

    def test_make_time(self):
        initial_time = self.oS.schedule_time
        self.oS.makeSandwich()
        self.assertEqual(initial_time+60, self.oS.schedule_time)

    def test_serve_time(self):
        initial_time = self.oS.schedule_time
        self.oS.serveSandwich()
        self.assertEqual(initial_time+30, self.oS.schedule_time)

    def test_break_time(self):
        initial_time = self.oS.schedule_time
        self.oS.takeBreak()
        self.assertEqual(initial_time+60, self.oS.schedule_time)

    def test_make_sequence_number(self):
        initial_number = self.oS.sequence_number
        self.oS.makeSandwich()
        self.assertEqual(initial_number+1, self.oS.sequence_number)

    def test_serve_sequence_number(self):
        initial_number = self.oS.sequence_number
        self.oS.serveSandwich()
        self.assertEqual(initial_number+1, self.oS.sequence_number)

    def test_break_sequence_number(self):
        initial_number = self.oS.sequence_number
        self.oS.takeBreak()
        self.assertEqual(initial_number+1, self.oS.sequence_number)


if __name__ == '__main__':
    unittest.main()
