import module

try:
    a=int(input("enter a"))
    b=int(input("enter b"))
    c=input("enter '+' or '-' or '*' or '/'")
    if c=="+":
        module.sum(a,b)
    elif c=="-":
        module.subtract(a,b)
    elif c=="*":
        module.multiply(a,b)
    elif c=="/":
        module.divide(a,b)
    else:
        print("invalid response")    
except ZeroDivisionError:
    print("number cannot be divisible by 0") 
except ValueError:
    print("invalid value entered")                   

