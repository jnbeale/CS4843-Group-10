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
#define world
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
#1 got error
number = 10
#number = int(input('Enter a positive number, negative to stop: '))
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

    #3
#number = 0
number = int(input('Enter a number: '))
while number >= 0:
    if rank == 0:
        print("Process %d got %d\n" % (rank, number))
        comm.send(number, dest=rank + 1)
    if rank > 0:
        comm.recv(number, source=rank - 1)
        print("Process %d got %d\n" % (rank, number))
        comm.send(value, dest=rank + 1)
        print("Process %d got %d\n" % (rank, number))
    number = int(input('Enter a number: '))

#4
number = int(input('Enter a number: '))
while number >= 0:
    if rank == 0:
        comm.send(number, dest=rank + 1)
    if rank > 0:
        comm.recv(number, source=rank - 1)
        comm.send(number, dest=rank + 1)

    print("Process %d got %d\n" % (rank, number))
    number = int(input('Enter a number: '))
