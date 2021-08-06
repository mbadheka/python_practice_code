# decorator funcation 
# calculating time

from functools import wraps
import time

def calculate_time(func):
    @wraps(func)
    def wrap_funcation(*args,**kwargs):
        t1 = time.time()
        returned_values = func(*args,**kwargs)
        t2 = time.time()
        print(f"it takes {t2-t1} seconds to run funcation")
        return returned_values
    return wrap_funcation


@calculate_time
def func1(n):
    return [i**2 for i in range (1,n+1)]

func1(1000)

