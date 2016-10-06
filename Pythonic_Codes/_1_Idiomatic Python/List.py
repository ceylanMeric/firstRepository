def ex1():
    z= [ i+2  for i in range(10)]; print(z)
#ex1()

#ex2()
def ex2():
    z= [ i*3 for i in range(10) if i%2==0]
    print(z)


def ex3():
    z= [ int(val) for val in open("Data and Comment.txt") if val[0]!='#']
    print(z)
#ex3()

