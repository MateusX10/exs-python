from random import randint
from time import sleep


def DrawsNumbers(): 
    count = TotalNumbers = 0
    numbers = list()
    TotalNumbers = randint(0,10)
    while count < TotalNumbers:
        numbers.append(randint(0,10))
        count += 1
    return numbers
def bigger(lst):
    maior = 0
    for num in lst:
        print(f"{num} ", end='', flush=True)
        sleep(0.5)
        if num > maior:
            maior = num

    return maior

for v in range(0, 6):
    print('-=' * 40)
    print(f"Analyzing the reported numbers...")
    sleep(1.5)
    numbers_list = DrawsNumbers()

    BiggerNumber = bigger(numbers_list)
    print(f"It was reported that there were {len(numbers_list)} numbers in total")
    print(f"The largest numbers entered was {BiggerNumber}")
