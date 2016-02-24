



def  StairCase(n):
    '''a = []
    for i in range(n):
        for j in range(0,n-1):
            a.append(' ')
            for each in a:
                print each,
                print '#'
        n-=1
'''
    while n>0:
        for i in range(0,-n):
            print ' ',
            print '#'
            n-=1

#StairCase(5)


def  sumOfIntegers( arr):
    nmbr = raw_input()
    arr = []
    for i in range(0,nmbr):
        nmbrs = int(raw_input())
        arr.append(nmbrs)
    print sum(arr)
a = [1,2,3]
sumOfIntegers(a)
