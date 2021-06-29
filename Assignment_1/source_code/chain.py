from mpi4py import MPI
#define world
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
#num = []
number = input('Enter a positive number, negative to stop: ')
while True:
    if number < 0:
        break
    #num.append(numbers)
    while number >= 0:
        if rank == 0:
            comm.isend(number, dest=rank+1)
        else:
            number = comm.irecv(number, source=rank-1)
            if rank < size-1:
                comm.isend(number, dest=rank + 1)
        print("Process %d got %d\n" % (rank, number))


