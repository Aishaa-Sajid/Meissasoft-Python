def decorator1(func):
    def wrapper():
        print("Good morning")
        func()
        print("Thankyou")
    return wrapper

def decorator2(func):
    def wrapper(*args, **kwargs):
        print("Before function")
        result=func(*args,**kwargs)
        print(result)
        print("After function")
        return result
    return wrapper
 
@decorator1
@decorator2
def hello():
    print("Hello!")

hello()



@decorator2
def add(a,b):
      return a+b
       

a=int(input("Enter 1st value : "))
b=int(input("Enter 2nd value : "))
add(a,b)