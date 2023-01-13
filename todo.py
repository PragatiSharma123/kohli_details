import json
from datetime import date

newDoc = False

#f = open("todoDB.json", "r")
task = {}

while True:
 with open("todoDB.json", "r") as f:
    #reading the todoDB.json

    todoData = json.load(f)
    #f = open("todoDB.json.load", "r")
    #todoData = json.load(f)
    #print(todoData, type(todoData))

    keys = list(todoData.keys())
    currentData = date.today()
    #checking whether the user ia a new user or not
    if len(todoData) == 0:
        emptyDoc = True
        username = input("\nHi there!! welcome to TodoCLI.please enter your username: ")

        
        todoData["name"] = username
        todoData["Date"] = str(currentData)
        print(f"Hey {username}! I hope you had a good start of the day,let's plan your day together\nyou can create your first task by typing create task or add task")

        cmd = input(">>")
        todoData["today"] = []

        if cmd == "create task" or cmd == "add task":
            print("\nplease provide details about your task as per the cli instructions")
            print("\nAdd time in military format i.e. if it's 9AM write 0900 or it's 9PM write 2100")

            #take the task description as input
            task_description = input("please enter your task description: ")
            scheduled_time = input("please enter the scheduled time: ")

            task ={
                "description": task_description,
                "scheduled_time": scheduled_time
            }
            todoData["today"].append(task)
            with open("todoDB.json","w") as f:
                json.dump(todoData,f, indent=4)
        
        elif cmd == "break" or cmd == "exit":
                break

    elif "today"  in list(todoData.keys()):
        tasks = todoData["today"]
        username = todoData["name"]


        print(f"\nToday is{currentData}")
        #show the user all the existing tasks
        print(f"\nHey {username}, here are the tasks for your day")
        for task in tasks:
            print(f"\nTask {tasks.index(task) + 1}")
            print(f"\nTask description:",task["description"])
            print(f"scheduled time:",task["scheduled_time"])

        print("\n add more task for the day")
        cmd = input(">>")

        if cmd == "create task" or cmd == "add task":
            task_description = input("\nEnter your task description:")
            scheduled_time = input("\nEnter your scheduled time:")

            task = {
                "description": task_description,
                "scheduled_time": scheduled_time
            }

            todoData["today"].append(task)

            with open("todoDB.json", "r+") as f:
               f.seek(0)
               json.dump(todoData, f, indent=4) 

            print("\Task created successfully")
            print("\nType <create Task> or <add task> to add more tasks")
            print("\ntype <done> or <exit> to exit from the app")
            continue

        
        
        elif cmd == "Delete  all tasks":
            todoData[ "today" ] = []
            with open("todoDB.json", "r+") as f:
                f.seek(0)
                json.dump(todoData, f, indent=4)
                print("\nTasks deleted successfully")
        elif cmd == "Delete user":
            todoData = {}
            with open("todoDB.json", "W") as f:
                json.dump(todoData, f, indent=4)
                print("\nUser deleted successfully")
               
               
        elif cmd == "done" or cmd == "exit":
         break


        
import json
from datetime import date

emptyDoc = False

task_count = 0
while True:
    with open("todoDB.json", "r") as f:
        todoData = json.load(f)
    # f = open("todoDB.json", "r")
    # todoData = json.load(f)
    # print(todoData, type(todoData))

    currentDate = date.today()

    if len(todoData) == 0:
         emptyDoc = True
         username = input("\nHi there!! Welcome to TodoCLI. Please enter your username: ")
         todoData["name"] = username
         todoData["date"] = str(currentDate)

         print(f"Hey {username}! I hope you had a good start of the day, let's plan your day together\nYou can create your first task by typing create task or add task\n")
         cmd = input(">>")

         print("\nCreate a task by weriting <create task> or <add task>")
         todoData["today"] = []

         if cmd == "create task" or cmd == "add task":
            task_description = input("\nEnter your task description: ")
            scheduled_time = input("\nEnter scheduled time for the task: ")

            task = {
                "task_id": task_count,
                "description": task_description,
                "scheduled_time": scheduled_time,
                "status": "TBD"
            }

            todoData["today"].append(task)

            with open("todoDB.json", "w") as f:
                json.dump(todoData, f, indent=4)
            task_count = task_count + 1
         elif cmd == "break" or cmd == "exit":
            break
    
    elif "today" in list(todoData.keys()):
        tasks = todoData["today"]
        username = todoData["name"]
        print(f"\nToday is {currentDate}")
        #show the user all the existing tasks
        print(f"\nHey {username}, here are the tasks for your day")
        for task in tasks:
            print(f"\nTask {tasks.index(task) + 1}")
            print("\nTask description: ", task["description"])
            print("\nScheduled time: ", task["scheduled_time"])

        print("\n add more tasks for the day")

        cmd = input(">>")

        if cmd == "create task" or cmd == "add task":
            task_description = input("\nEnter your task description: ")
            scheduled_time = input("\nEnter your scheduled time: ")

            task = {
                "task_id": task_count,
                "description": task_description,
                "scheduled_time": scheduled_time,
                "status": "TBD"
            }

            todoData["today"].append(task)

            with open("todoDB.json", "r+") as f:
                f.seek(0)
                json.dump(todoData, f, indent=4)
            task_count = task_count + 1
            print("\Task created successfully")
            print("\ntype <create task> or <add task> to add more tasks")
            print("\ntype <done> or <exit> to exit from the app")
            continue
        elif cmd == "delete all tasks":
            todoData["today"] = []
            with open("todoDB.json", "r+") as f:
                f.seek(0)
                json.dump(todoData, f, indent=4)
            print("\nTasks deleted successfully")

        elif cmd == "delete user":
            todoData = {}
            with open("todoDB.json", "w") as f:
                json.dump(todoData, f, indent=4)
            print("\nUser deleted successfully")

        elif cmd == "done" or cmd == "exit":
            break
        elif cmd == "mark task as done":
            tasks = todoData["today"]
            username = todoData["name"]
            print(f"\nToday is {currentDate}")
            #show the user all the existing tasks
            print(f"\nHey {username}, here are the tasks for your day")
            for task in tasks:
                print(f"\nTask {tasks.index(task) + 1}")
                print("\nTask description: ", task["description"])
                print("\nScheduled time: ", task["scheduled_time"])
                print("\nStatus: ", task["status"])
            
            # status_cmd = input("\ntask>> ")
            task_id = int(input("\n Enter task id: "))
            
            for task in tasks:
                if task["task_id"] == task_id:
                    todoData["today"][tasks.index(task)]["status"] = "DONE"
                else:
                    continue

            with open("todoDB.json", "r+") as f:
                json.dump(todoData, f, indent=4)
            continue
        
            


