from circuitBreaker import circuitBreaker
import time


cars = [ 'Audi' , 'Toyoto' ,'chevrolet' , 'Fiat']

@circuitBreaker(3,3,5)
def list_traversal(index):
    print index
    if(index >= len(cars)):
        raise Exception
    print cars[index]

#case to check flow of decorator class
def test0():
    try:
        list_traversal(2)
    except Exception as e:
        print e

#case 0 : make all succfull
def test1():
    try:
        list_traversal(1)
        list_traversal(2)
        list_traversal(3)
    except Exception as e:
        print " error : %s" %e

#case 1 : after 3 successfull make 1 fail
def test2():
    try:
        list_traversal(1)
        list_traversal(2)
        list_traversal(3)
        list_traversal(5)
    except Exception as e:
         print " error : %s" %e


#case 2 : atfer 1 failure try one more success when open state is consuming timer
def test3():
    try:
        list_traversal(1)
    except Exception as e:
         print " error : %s" %e

#case 3 : atfer timer is over check half stage for 1 success and 1 failure
def test4():
    time.sleep(15)
    try:
        list_traversal(3)
        list_traversal(5)
    except Exception as e:
         print " error : %s" %e

#case 4 : after timer is over check half stage for 3 success and switch to close
def test5():
    time.sleep(10)
    try:
        list_traversal(1)
        list_traversal(2)
        list_traversal(3)
        list_traversal(0)
    except Exception as e:
         print " error : %s" %e

#case 5: make all 3 fail
def test6():
    try:
        list_traversal(9)
        list_traversal(5)
        list_traversal(7)
    except Exception as e:
         print " error : %s" %e

#case 5: make all 4 fail
def test7():
    try:
        list_traversal(9)
        list_traversal(5)
        list_traversal(7)
        list_traversal(7)
    except Exception as e:
         print " error : %s" %e


test7()
time.sleep(2)
test0()
time.sleep(3)
test0()
