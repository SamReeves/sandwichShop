## SETUP AND USAGE ##

The class orderSandwich.py, found in this folder, is a short script to 
generate a fast food work schedule.  It builds the schedule from the
number of sandwiches ordered, and it outputs the updated schedule.

In order to use this code, you should create an instance of the class,
and use the order function.  This example orders 5 sandwiches:

import orderSandwich
oS = orderSandwich.orderSandwich()
oS.order(5)

Unit testing can be done with testing.py.  Just run the script in a terminal.

------------------------------------------------------------------------------
## FUNCTIONS ##

order(n=1)
    Update the schedule with a new order.  This defaults to 1 sandwich.
    
outputSchedule()
    Print the current complete schedule to terminal without changes.

calculateTime()
    Return a string representing the latest time a task can begin.

makeSandwich()
    Update internal variables related to making a sandwich.
    
serveSandwich()
    Update internal variables related to serving a sandwich.
    
takeBreak()
    Update internal variables related to taking a break.



------------------------------------------------------------------------------
## TESTING ##

First, load the code from orderSandwich.py.  Then, run testing.py in the 
same environment.  All 7 tests should run without error.

Tests include:

1) Is time format returned as a string?
2) Does makeSandwich() update time properly?
3) Does serveSandwich() update time properly?
4) Does takeBreak() update time properly?
5) Does makeSandwich() update sequence number properly?
6) Does serveSandwich() update sequence number properly?
7) Does takeBreak() update sequence number properly?
