# To do list


print("----- TO DO LIST ----")



add = ""
tasks = []
i_no = 1

quit = ""

while(quit.lower() != "q"):
    
    print("\n Would you like to:")
    print("1. Add a Task")
    print("2. Done? , Remove the task")
    choice = int(input("Choose an option: "))
    
    
    if(choice == 1):
        

            
        print("Adding Tasks")
        start_Statement = input("Start Adding? (Yes to start)(Q to quit): ")
        add = ""    
        while((start_Statement != "q") and (start_Statement != "Q") and (add != "q") and (add != "Q") ):
            
            add = input(f"Enter task {i_no}: ")
            if add.lower() == "q":
                break;
            
            tasks.append(add)
            
            i_no += 1
        print("\nYour To-do list > ")
        count = 1    
        for task in tasks:
            print(f"{count}. {task}")
            count += 1
            
    elif(choice == 2):
        print("\nYour current TO-Do list: ")
        
        count = 1    
        for task in tasks:
            print(f"{count}. {task}")
            count += 1
        
        itemToRem = int(input("\nEnter the task No. which you are done with.."))
        removed = tasks.pop(itemToRem - 1)
        
        print(f"{removed} has been removed")
        print("\nYour Updated TO-Do list: ")
        
        count = 1    
        for task in tasks:
            print(f"{count}. {task}")
            count += 1
            
    quit = input("\nQuit NOW? , (r = restart and Update the list)(Q to quit): ")
    
    if (quit.lower() == "q"):
        break; 
    

print("\n------ THANK YOU! ------")