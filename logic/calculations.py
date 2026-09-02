# calculation functions that happen in the main file
import time
import json
import database

#id = 1

currentLog = database.loadData()

def addNewLog(jump):

        if jump <= 0.00:
            print("\nYou cant jump negative meters.")
            return False

        #global id

        

        jumps = currentLog["jumps"]
        
        highest_id = max(
            (jumpElement["id"] for jumpElement in jumps),
            default=0
        )

        new_id = highest_id + 1
        
        currentLog["jumps"].append({
            "id": new_id,
            "height": jump,
            "date": time.strftime("%Y-%m-%d - %I:%M %p", time.localtime())
        })

        database.saveData(currentLog)

def calcPB():
    pb = 0
    pbDate = ""
    # since we zip the height and date lists together when we find the pb we use the same index 
    # and assign it to be the date of the pb
    for jump, date in zip(log["height"], log["date"]):
        if jump > pb:
            pb = jump
            pbDate = date
    print(f"Your Personal Best jump is {pb:.2f}m and it was logged on {pbDate}\n")


def calcAvgHJ():
    index = 0
    averageHeight = 0
    for jump in log["height"]: 
        averageHeight += jump
        index += 1
    averageHeight = averageHeight/index
    print(f"Your average jump height is... {averageHeight:.2f} meters!\n")

def calcGoal(userPB, goal):
    userProgress = round(userPB/goal, 2) * 100
    print(f"\nCurrent PB: {userPB:.2f}m")
    print(f"Goal: {goal:.2f}m")
    print(f"Progress: {userProgress}%")

def exitToMainMenu():
    while True:
        userExit = input("click e to exit: ")
        if userExit == "e":
            break

def showHJLog():
    index = 1
    print(currentLog)
    """
    print("Here is your training log:\n")
    for jump, date in zip(log["height"], log["date"]):
        print(f"Jump #{index}: {jump:.2f}m. logged on {date}\n")
        index += 1 
    """

def deleteAllLogs():

    currentLog["jumps"] = []

    database.saveData(currentLog)

    """    
    log["height"] = []
    log["date"] = []
    print("High jump log cleared")
    time.sleep(2)
    """

def deleteLog(jump):

    del currentLog["jumps"][int(jump) - 1]

    database.saveData(currentLog)

    """
    jump = int(jump)
    lastDeletedJump = log["height"][jump -1]
    del log["height"][jump - 1]
    del log["date"][jump - 1]
    print(f"\nJump {jump} ({lastDeletedJump:.2f}m) has been deleted.\n")
    time.sleep(2)
    """

def goalCalculation(goal, pb):
    if goal <= 0.00:
        print("\nYou cant jump negative meters dude.")
        time.sleep(3)
        #continue
    elif goal <= pb:
        print("\nYou have already achieved that high of a jump\n")
        time.sleep(3)
        #continue
    elif pb / goal >= 0.95:
        calcGoal(pb, goal)
        print("This goal is within reach")
    elif pb / goal >= 0.90:
        calcGoal(pb, goal)
        print("This goal is will be hard but you can do it!")
    elif pb / goal >= 0.85:
        calcGoal(pb, goal)
        print("This goal is going to be challenging")
    elif pb / goal >= 0.80:
        calcGoal(pb, goal)
        print("This goal is going to be pretty hard")
    else:
        print("This goal is basically impossible")


def convertFtToM(feet, inches):
    result = (feet * 0.3048) + (inches * 0.0254)
    return result
    