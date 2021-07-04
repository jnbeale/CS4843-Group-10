from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


f = open("data.txt", "r").read().split("\n")
req = comm.irecv(source=MPI.ANY_SOURCE, tag=11)
if rank == 0:
    for i in f[0:10000]:
        if(req.Test() == True):
            index = f.index(i)
            print("Master process has received message at index %d" % (index))
            break
        if i == "11":
            for r in range(1, size):
                comm.isend(0, dest=r, tag=11)
            index = f.index(i)
            print("I am master process and I found 11 at index %d" % (index))
if rank == 1:
    for i in f[10000:20000]:
        if(req.Test() == True):
            index = f.index(i)
            print("Process 1 has received message at index %d" % (index))
            break
        if i == "11":
            for r in range(1, size):
                comm.isend(0, dest=r, tag=11)
            index = f.index(i)
            print("I am process %d and I found 11 at index %d" % (rank, index))
if rank == 2:
    for i in f[20000:30000]:
        if(req.Test() == True):
            index = f.index(i)
            print("Process 2 has received message at index %d" % (index))
            break
        if i == "11":
            for r in range(1, size):
                comm.isend(0, dest=r, tag=11)
            index = f.index(i)
            print("I am process %d and I found 11 at index %d" % (rank, index))
if rank == 3:
    for i in f[30000:40000]:
        if(req.Test() == True):
            index = f.index(i)
            print("Process 3 has received message at index %d" % (index))
            break
        if i == "11":
            for r in range(1, size):
                comm.isend(0, dest=r, tag=11)
            index = f.index(i)
            print("I am process %d and I found 11 at index %d" % (rank, index))
