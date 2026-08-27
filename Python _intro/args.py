def my_args(*args):
    print("________________")
    print(f"Args type of args{type(args)}")
    print(args)

    my_args(30,67,97,100)
    my_args("Hello",True,34)

def area_rectangle(length,width):
    area=length*width
    print("_____________")
    print(f"For rectangle with length {length} and width {width} area is {area}")

area_rectangle(20,10)

def sum(*args):
    ans=0
    for n in args:
        print(f"n is {n}")
        ans=ans+n
    print(f"Sum is {ans}")

sum(29,49,34,40,69,98)