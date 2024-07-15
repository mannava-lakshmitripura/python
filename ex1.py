classesheld=int(input("Enter no.of classes held: "))
classesattended=int(input("Enter no.of classes attended: "))
percentage=(classesattended/classesheld)*100
print(percentage)
if percentage>=75:
    print("The student is allowed to sit in exam")
else:
    print("The student is not aloowed to sit in exam")    