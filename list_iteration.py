import sys

counterIndex = 0
for element in sys.argv:

    if element == sys.argv[0]:
        pass
    else:
       print(f"{counterIndex}. {element}")


    counterIndex = counterIndex + 1




