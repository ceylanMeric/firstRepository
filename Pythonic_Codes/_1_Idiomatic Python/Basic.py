# For loop indexli
z=range(5)
for i, data in enumerate(z):
    print(i, data)

#Dosya satırı okuma
for line in open("example.txt"):
    print(line)

#Swapping
a=5
b=6
a,b = b,a
print(a,b)

#List e başka bir list in değerlerini ekleme
x=[]
y=[1,2,3,4]
x.append(5)
x.extend(y)
print(x)

#List seriyi tersten okuma
x.reverse()
print(x)

#Sorting
z=[("aaa",5), ("ccc",4), ("bbb",3)]
z.sort()
print(z)

#Dictionary veri ekleme, iki yöntem var
d={}
d['a']=5
d['b']=6

d=dict(a=5, b=4, c=6)
print(d)

# Text deki verileri parse edip dict e atma
d={}
for line in open("example.txt"):
    val1, val2, val3 = line.split()
    d[val2]= val1 + val3
print(d)

