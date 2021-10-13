import sys
firstArgument = sys.argv[1]
secondArgument = sys.argv[2]
try:
    firstArgument = int(firstArgument)
    secondArgument = int(secondArgument)
except ValueError:
    pass

if isinstance(firstArgument, int) & isinstance(secondArgument, int):
    sumOfArguments = firstArgument + secondArgument
else:
    print("enter integers next time please")
    sys.exit()

if int(sumOfArguments) <= 0:
    print("You have chosen the path of destitution")
elif (int(sumOfArguments) >= 1) & (int(sumOfArguments) <= 100):
    print("You have chosen the path of plenty")
else:
    print("You have chosen the path of excess")




