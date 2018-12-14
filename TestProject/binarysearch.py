import math
def binarysearch(A,q,i,j):
    if A[math.ceil((i+j)/2)]== q:
        return math.ceil((i+j)/2)+1, q
    if j-i < 2 :
        return 'Not found!'
    if A[math.ceil((i+j)/2)] < q:
        return binarysearch(A, q , math.ceil((i+j)/2), j)
    if A[math.ceil((i+j)/2)] > q:
        return binarysearch(A, q, i , math.ceil((i+j)/2))



def Main():

    while 1:

        x=input("Enter the number enteries by space: ")
        list=[int (i) for i in x.split(" ")]

        q= int(input("Enter the query entry: "))

        print(binarysearch(list,q , 0 , len(list)))

        b = input("Would you like to try again, y/n?")
        if b == 'n':
            break


if __name__=='__main__':
    Main()

