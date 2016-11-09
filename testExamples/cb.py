from functools import wraps
from datetime import datetime, timedelta


class CircuitBreaker(object):
    def __init__(self, name=None, expected_exception=Exception, max_failure_to_open=3, reset_timeout=10):
        """
        DO NOT ALTER FUNCTION ARGUMENTS AND THEIR DEFAULT VALUES!
        """
        self._name = name
        self._expected_exception = expected_exception
        self._max_failure_to_open = max_failure_to_open
        self._reset_timeout = reset_timeout
        # Set the initial state
        self.close()

    def close(self):
        """
        Your solution must work with this '_is_closed' boolean flag variable only.
        DO NOT SET ANYTHING OTHER THAN True OR False, OR YOU WILL GET ZERO!
        """
        self._is_closed = True
        self._failure_count = 0

    def open(self):
        self._is_closed = False
        self._opened_since = datetime.utcnow()

    def __call__(self, func):
        if self._name is None:
            self._name = func.__name__

        @wraps(func)
        def with_circuitbreaker(*args, **kwargs):
            return self.call(func, *args, **kwargs)

        return with_circuitbreaker

    def _handlefailure(self):
        self._failure_count += 1
        if(self._failure_count >= self._max_failure_to_open):
            self.open()

    def __handlesuccess(self):
        self.close()

    @property
    def open_until(self):
        return self._opened_since + timedelta(seconds=self._reset_timeout)

    @property
    def open_remaining(self):
        return (self.open_until - datetime.utcnow()).total_seconds()

    def call(self, func, *args, **kwargs):
        """
        Steps:
        1. If the cricuitbreaker is NOT in the executable state, then
           throw an Exception with this error message format -
            'CircuitBreaker[%s] is OPEN until %s (%d failures, %d sec remaining)'
                          {name}             {open_until} {failure_count}  {open_remaining}
        2. Call the given 'func' and handle the 'expected_exception'.
        """
        if(not self._is_closed and not self.open_remaining <= 0):
            raise Exception('CircuitBreaker[%s] is OPEN until %s (%d failures, %d sec remaining)'% (self._name,self.open_until,self._failure_count,self.open_remaining))

        try:
            result = func(*args, **kwargs)
        except self._expected_exception:
            self._handlefailure()
            raise

        self.__handlesuccess()
        return result

