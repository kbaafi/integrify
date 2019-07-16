from functools import wraps

def double(func):
    @wraps(func)
    def inner(*args, **kwargs):
        out = func(*args, **kwargs)
        return [out, out]
    return inner


@double
def my_function(x, y):
    return x+y


class doubler():
    def __init__(self,func):
        self.func = func

    def __call__(self,*args):
        ret = self.func(*args)
        ret_list = [ret, ret]
        return ret_list

@doubler
def doubler_decoratee(x,y):
    return x+y


def verify(func):
    @wraps(func)
    def inner(**kwargs):
        if 'role' in kwargs and kwargs['role'] == 'admin':
            return func(**kwargs)
        else:
            return 'invalid'
    return inner

@verify
def print_role(**kwargs):
    print(kwargs['role'])

