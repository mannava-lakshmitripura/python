def sum(x,y):
    print(x+y)
def subtract(x,y):
    print(x-y)
def multiply(x,y):
    print(x*y)
def divide(x,y):
    print(x/y) 


a=int(input("enter a"))
b=int(input("enter b"))
c=input("enter '+' or '-' or '*' or '/'")
if c=="+":
    sum(a,b)
elif c=="-":
    subtract(a,b)
elif c=="*":
    multiply(a,b)
elif c=="/":
    divide(a,b)
else:
    print("invalid response")            
