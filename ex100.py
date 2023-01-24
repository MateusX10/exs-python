from time import sleep


numbers = list()
summ = 0

def DrawsNumbers():
    from random import randint

    return [randint(0,10), randint(0,10), randint(0,10),
           randint(0,10), randint(0,10)]

def SumEven(lst):
    sum_even = 0
    print(f'Summing up the even values of the list:  {lst}, ', end='')
    for v in lst:
        if v % 2 == 0:
            sum_even += v

    print(f"we have {sum_even}")


print(f"Drawing 5 numbers from the list: ", end='')
numbers = DrawsNumbers()

for v in numbers:
    print(f"{v} ", end='', flush=True)
    sleep(0.4)
print("DONE!\n")

summ = SumEven(numbers)