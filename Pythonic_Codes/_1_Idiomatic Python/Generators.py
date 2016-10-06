def ex1():

    def square(list):
        for i in list:
            yield i*i #return gibi ama fonksiyon sonlanmıyor, veriyi yönlendiriyor
                      # yield ile nested looplar yapabilirsin
    x=range(21)
    for i in square(x):
        print(i)
#ex1()

#yada böyle liste yapıp toplu da gönderebilirsin:
def ex2():

    def square(list):
        return [i*i for i in list]

    x=range(21)
    for i in square(x):
        print(i)
ex2()

