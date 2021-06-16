

def outer_dv(func):
    print(func)
    def inner(x,y):
        if x < y :
            x,y = y,x
            return func(x,y)
    return inner

@outer_dv
def divided(x,y):
    print(x/y)

divided(2,4)

