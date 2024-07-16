tasks=[]
def add_task(task):
    tasks.append({"task":task,"done":False})
def mark_done(task_index):
    if 0<=task_index<len(tasks):
        tasks[task_index]["done"]=True
    else:
        print("Invalid task index")    
def delete_task(task_index):
    if 0<=task_index<len(tasks):
        tasks.pop(task_index)
    else:
        print("invalid task index")
def show_tasks():
    for i,task in enumerate(tasks):
        status="Done" if task["done"] else "Not Done"
        print(f"{i}.{task['task']}-{status}")         
def main():
    while True:
        print("\\nTo-Do List Application")
        print("1.Add Task")
        print("2.mark Task as Done")
        print("3.Delete Task")
        print("4.Show tasks")
        print("5.Exit") 
        choice=input("enter ur choice")
        if choice == "1":
            task=input("enter task")
            add_task(task)
        elif choice == "2":
            task_index=int(input("enter task index to mark its done"))
            mark_done(task_index)
        elif choice == "3":
            task_index=int(input("enter task index to delete"))
            delete_task(task_index)
        elif choice == "4":
            show_tasks()
        elif choice == "5":
            break
        else:
            print("invalid Choice")        
main                                      
