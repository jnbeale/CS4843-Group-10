from mpi4py import MPI
#import numpy as np
f = open("data.txt", "r").read().split("\n")
if rank == 0:
    #f = open("data.txt", "r").read().split("\n")
    #print(f)
    #nvalues = 40000/size
    #i = rank*nvalues
    #print(i)
    for i in arr[0:10000]:
        if i == "11":
            for r in range(1,size):
                comm.isend(0, dest=r, tag=11)
            print("I am process %d and I found 11" % (i, rank))
            myfound = 1

        if(req.Test() == True):
                print("received message")
if rank == 1:
    for i in arr[10000:20000]:
        if i == "11":
            for r in range(1,size):
                comm.isend(0, dest=r, tag=11)
            print("I am process %d and I found 11" % (i, rank))
        if (req.Test() == True):
            print("received message")
if rank == 2:
    for i in arr[20000:30000]:
        if i == "11":
            for r in range(1,size):
                comm.isend(0, dest=r, tag=11)
            print("I am process %d and I found 11" %(i, rank))
        if (req.Test() == True):
            print("received message")
if rank == 3:
    for i in arr[30000:40000]:
        if i == "11":
            for r in range(1,size):
                comm.isend(0, dest=r, tag=11)
            print("I am process %d and I found 11" % (i, rank))
        if (req.Test() == True):
            print("received message")

