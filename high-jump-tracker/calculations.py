# calculation functions that happen in the main file
import time

def addNewLog(jump, log):

        if jump <= 0.00:
            print("\nYou cant jump negative meters.")
            time.sleep(2)
            #continue

            # append each log into the height category of the high jump log
        elif jump <= 1.00:
            log["height"].append(jump)
            print("\nAdded to log")
            print(f"Good start. {jump:.2f} meters is good but you can do better\n")
        elif jump <= 1.50:
            log["height"].append(jump)
            print("\nAdded to log")
            print(f"that is pretty solid. {jump:.2f} meters is solid\n")
        elif jump <= 2.00:
            log["height"].append(jump)
            print("\nAdded to log")
            print(f"dang you jumping. {jump:.2f} meters is good\n")
        elif jump >= 2.00:
            log["height"].append(jump)
            print("\nAdded to log")
            print(f"Wowza. {jump:.2f} meters is amazing\n")
                        
        # at the very end of the adding section we will add a date no matter what the jump was
        log["date"].append(time.strftime("%Y-%m-%d - %I:%M %p", time.localtime()))