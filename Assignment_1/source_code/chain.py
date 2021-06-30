from mpi4py import MPI
#define world
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
#num = []
number = int(input('Enter a positive number, negative to stop: '))
while True:
    if number < 0:
        break
    #num.append(numbers)
    else:
        if rank == 0:
            comm.isend(number, dest=rank+1)
        else:
            comm.irecv(number, source=rank-1)
            if rank < size-1:
                comm.isend(number, dest=rank + 1)
        print("Process %d got %d\n" % (rank, number))


