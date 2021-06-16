import  time
import threading
def cube(n):
    print(n*n*n)

def square(n):
    print(n*n)


if __name__=="__main__":
 t = time.time()
 t1 = threading.Thread(target=cube,args=(5,))
 t2 =threading.Thread(target=square,args=(5,))
 t1.start()
 t2.start()
 t1.join()
 t2.join()
 print("I am threading Taking {}".format(time.time() - t))