import datetime
import time
from functools import wraps

OPEN_STATE ='Open'
HALF_OPEN_STATE = 'Half-Open'
CLOSE_STATE = 'Closed'

class circuitBreaker(object):

    def __init__(self, fthreshold, sthreshold, timer):
        self.failure_counter = 0
        self.failure_threshold = fthreshold
        self.success_counter = 0
        self.success_threshold = sthreshold
        self.timeout_timer = timer
        self.current_state = CLOSE_STATE
        self.timerStarted = False
        self.param1 = 0;
        print "inside init"

    def __call__(self, f):
        print "inside call"
        @wraps(f)
        def func_wrapper(index):
            print "performing wrppr func"
            self.param1 = index
            if(self.current_state == CLOSE_STATE):
                self.performClose(f)
                print " current state is %s " %self.getCurrentState()
                print " failures : %d" %self.getFailureCount()
            elif(self.current_state == OPEN_STATE):
                self.performOpen(f)
                print " current state is %s " % self.getCurrentState()
            elif(self.current_state == HALF_OPEN_STATE):
                self.performHalfOpen(f)
                print " current state is %s " % self.getCurrentState()
        return func_wrapper

    def performClose(self,f):
            try:
                f(self.param1)
                #call function
                #return result
                self.failure_counter =0; #sucees reset the failure count to zero
            except:
                self.failure_counter +=1
                if(self.failure_counter == self.failure_threshold):
                    self.open();
                    self.performOpen(f)



    def performOpen(self,f):

        if(not self.isTimerOver(f)):
            print " Ciruit breaker is opened"


    def performHalfOpen(self,f):

        try:
            #call operation
            f(self.param1)
            self.success_counter +=1
            if(self.success_counter == self.success_threshold):
                self.close()
                self.performClose(f)
            #return result
        except:
            self.open()
            self.performOpen(f)
            print " Circuit breaker switched to opened from half opened because again found failure"

    def isTimerOver(self, f):
        if (not self.timerStarted):
            self.openStartTime = datetime.datetime.utcnow() + datetime.timedelta(seconds=self.timeout_timer)
            print self.openStartTime
            remianingTime = (self.openStartTime - datetime.datetime.utcnow()).total_seconds()
            print remianingTime
            self.timerStarted = True
            return False
        else:
            print self.openStartTime
            remianingTime = (self.openStartTime - datetime.datetime.utcnow()).total_seconds()
            print remianingTime
            if(remianingTime > 0):
                return False
            else:
                self.timerStarted = False
                self.halfOpen()
                self.performHalfOpen(f)
                return True



    def isTimerStarted(self):
        return self.timerStarted

    def close(self):
        self.current_state = CLOSE_STATE
        self.failure_counter = 0


    def open(self):
        self.current_state = OPEN_STATE


    def halfOpen(self):
        self.current_state = HALF_OPEN_STATE
        self.success_counter = 0;


    def getCurrentState(self):
        return self.current_state

    def getFailureCount(self):
        return self.failure_counter


