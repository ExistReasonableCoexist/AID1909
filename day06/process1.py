import multiprocessing as mp
from time import sleep
def fun():
    print("***********************************")

    print("------------------------------------")
p =mp.Process(target=fun)
p.start()

print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
p.join()