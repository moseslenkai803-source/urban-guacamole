def myKwargs(**kwargs):
    print("Kwargs is ",type(kwargs))
    print(kwargs)

myKwargs(a=23,b=30)

myKwargs(name="Samson",email="Sam@sam.com",dict={"a":"a"})