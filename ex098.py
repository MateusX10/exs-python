from time import sleep, time


def counter(beginning,ends, increment):
    print('-=' * 40)
    
    print(f"Count from {beginning} to {ends} skipping from {increment} to {increment}")
    if beginning < ends:
        if increment < 0:
            increment = abs(increment)
        for number in range(beginning, ends + 1, increment):
            print(f"{number} ", end='', flush=True)
            sleep(0.5)
    else:
        if increment > 0:
            increment = (increment * (-1))
        for number in range(beginning, ends - 1, increment):
            print(f"{number} ", end='', flush=True)
            sleep(0.5)
    print("end")    
    

counter(1,10, 1)
counter(10,0,2)
print(f"Now it's your turn to customize yout count!")
beginning = int(input("Beginning: "))
ends = int(input("End: "))
increment = int(input("Increment: "))
if increment == 0:
    increment = 1
counter(beginning, ends, increment)

