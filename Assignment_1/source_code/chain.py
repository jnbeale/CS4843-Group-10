from mpi4py import MPI
#define world
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
#1 got error
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

#2 new
user_number = 0
while user_number >= 0:
    if rank == 0:
        print("Enter a positive number?")
        user_number = int(input())
        comm.send(user_number, dest=rank + 1)
    else:
        comm.recv(user_number, source=rank - 1)
        if rank < size - 1:
            comm.send(user_number, dest=rank + 1)
    print("Process %d got %d\n" % (rank, user_number))

