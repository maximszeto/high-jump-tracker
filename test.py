
myList = [2, 3, 4, 5, 3, 1, 0.5, 9]
greatestNum = 0

for i in myList:
    if i > greatestNum:
        greatestNum = i

print(greatestNum)



myList = [2,3,4,5]

print(myList)

for i in myList:
    if i < i+1:
        print(i)