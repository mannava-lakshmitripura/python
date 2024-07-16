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
except ZeroDivisionError as e:
    print("number cannot be divisible by 0",{e}) 
except ValueError:
    print("invalid value entered")                   

