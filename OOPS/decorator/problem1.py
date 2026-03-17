#Write a decorator that measures the time as function takes to execute.



import time 


def timer(function):
    def wrapper (*args,**kwargs):
        result = function(*args,**kwargs)
        return result
    
    return wrapper