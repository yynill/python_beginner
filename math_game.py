import random
import time

total_problems = 10
operators = ['+', '-', '*']


def random_number():
    number = random.randint(1, 20)
    return number


def random_operator():
    operator = random.choice(operators)
    return operator


def generate_problem():
    number1 = random_number()
    number2 = random_number()
    operator = random_operator()

    calc = f'{number1} {operator} {number2}'
    solution = eval(calc)
    print(calc)
    while True:
        answer = input('Solution: ')
        if int(answer) == solution:
            print('correct')
            break


input("press enter to start")
print('--------------------')

start_time = time.time()

for problem in range(total_problems):
    print(f'Problem # {problem+1}: ')
    generate_problem()
    print('--------------------')
end_time = time.time()

total_time = end_time - start_time
total_time = round(total_time, 2)


print('--------------------')
print(f'Finished! Time:{total_time} sec')
