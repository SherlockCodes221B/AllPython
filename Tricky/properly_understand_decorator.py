def dec(passed_func_i_e_f):
    def wrapper(*args,**kwargs):
        print("Start")
        val = passed_func_i_e_f(*args, **kwargs)
        print("End")
        return val
    return wrapper




@dec
def f():
    print("Ahaoi!")
f()

@dec
def summer(a,b):
    return a + b
print(summer(9,10))

