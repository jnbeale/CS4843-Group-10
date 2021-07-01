from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

f = open("data.txt", "r").read().split("\n")
req = comm.irecv(source=MPI.ANY_SOURCE, tag=11)
if rank == 0:
    for i in f[0:10000]:
        if i == "11":
            for r in range(1,size):
                comm.isend(0, dest=r, tag=11)
            print("I am process %d and I found 11" % (rank))
            myfound = 1
    if(req.Test() == True):
      print("Master process has received message")
if rank == 1:
    for i in f[10000:20000]:
        if i == "11":
            for r in range(1,size):
                comm.isend(0, dest=r, tag=11)
            print("I am process %d and I found 11" % (rank))
    if (req.Test() == True):
      print("Process 1 has received message")
if rank == 2:
    for i in f[20000:30000]:
        if i == "11":
            for r in range(1,size):
                comm.isend(0, dest=r, tag=11)
            print("I am process %d and I found 11" %(rank))
    if (req.Test() == True):
      print("Process 2 has received message")
if rank == 3:
    for i in f[30000:40000]:
        if i == "11":
            for r in range(1,size):
                comm.isend(0, dest=r, tag=11)
            print("I am process %d and I found 11" % (rank))
    if(req.Test() == True):
      print("Process 3 has received message")
