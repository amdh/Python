import sys
import os

n = int(raw_input());
sum(n)

def sum(number):
    print number
    sum = 0;
    for i in xrange(number):
        x = int(raw_input())
        if( 1<= x < 10000):
            sum = sum + x
        else:
            print "please enter vlaue > 1 < 10000"


