from utils import get_input
from itertools import product, combinations

input = get_input("input.txt")

operators = ["+", "*"]
# length = len(operators)


def get_operator_combinations(operators, length):
    operator_combinations = []
    for n in range(length + 1):
        operator_combinations.extend(list(product(operators, repeat=n)))
    return operator_combinations


def eval_eqn(eqn):
    eqn = eqn.split()
    total = int(eqn[0])
    for i in range(1, len(eqn), 2):
        operator = eqn[i]
        number = int(eqn[i + 1])
        if operator == "+":
            total += number
        elif operator == "*":
            total *= number
    return total


def create_and_eval_eqn(numbers, operators):
    eqn = ""
    for i in range(len(numbers)):
        eqn += str(numbers[i])
        if i < len(operators):
            eqn += f" {operators[i]} "
    return eqn, eval_eqn(eqn)


def is_eqn_possible(equation):
    answer, numbers = equation.split(": ")
    answer = int(answer)
    numbers = list(map(int, numbers.split()))
    numbers_length = len(numbers) - 1
    operator_combinations = get_operator_combinations(operators, numbers_length)
    # print(f"Operator combinations: {operator_combinations}")

    for operator_combination in operator_combinations:
        if 0 < len(operator_combination) == numbers_length:
            eqn, eval_answer = create_and_eval_eqn(numbers, operator_combination)
            # import pdb; pdb.set_trace()
            if eval_answer == answer:
                print(f"{eqn} = {eval_answer}: True")
                return True, eval_answer
    return False, 0


total = 0
for equation in input:
    # print(f"Equation: {equation}")
    is_possible, answer = is_eqn_possible(equation)
    if is_possible:
        total += answer
        # print("\n")
print(f"\nTotal: {total}")
