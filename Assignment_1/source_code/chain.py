from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

num = 0
while rank < size:
    if rank == 0:
        if num != 0:
            req = comm.irecv(source=size-1)
            num = req.wait()
        num = int(input("Enter a positive number, negative will stop: "))
        if num < 0:
            for r in range(1, size):
                comm.isend(0, dest=r, tag=11)
            comm.Abort()
        comm.isend(num, dest=rank+1)

    if rank > 0 and rank < size-1:
        req = comm.irecv(source=rank-1)
        num = req.wait()
        if num != 0:
            print("Process %d got %d\n" % (rank, num))
        comm.isend(num, dest=rank+1)

    if rank == size-1:
        req = comm.irecv(source=rank-1)
        num = req.wait()
        if num != 0:
            print("Final Process got %d\n" % num)
        comm.isend(num, dest=0)
