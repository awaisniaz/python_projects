def divided(x,y):
    print(x/y)

def outer_dv(func):
    print(func)
    def inner(x,y):
        if x < y :
            x,y = y,x
            return func(x,y)
    return inner

divided1 = outer_dv(divided)
divided1(2,4)
