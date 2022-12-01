# ADVENT OF CODE 2021
# Challenge #01
# Ethan Kessel

SAMPLE_INPUT = """\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000\
"""

PT1_SAMPLE_ANS = 24000

def pt1(input: str):
    input = input.splitlines()

    cals = []
    curr_cals = 0
    for entry in input:
        if entry != '':
            curr_cals += int(entry)
        else:
            cals.append(curr_cals)
            curr_cals = 0

    max_cals = max(cals)

    return max_cals

PT2_SAMPLE_ANS = 45000

def pt2(input: str):
    input = input.splitlines()
    
    cals = []
    curr_cals = 0
    for entry in input:
        if entry != '':
            curr_cals += int(entry)
        else:
            cals.append(curr_cals)
            curr_cals = 0

    if curr_cals > 0:
        cals.append(curr_cals) 

    cals_sorted = sorted(cals)

    top_3 = sum(cals_sorted[-3:])

    return top_3

# ==============================================================================

from typing import Tuple, Callable, Any
from time import perf_counter_ns
from os import path
from colorama import init as colr_init, Fore, Back, Style

# Runs the given solution with the input
def run_with_input(func: Callable[[str], Any], input: str) -> Tuple[Any, float]:
    start_time__ns = perf_counter_ns()
    result = func(input)
    end_time__ns = perf_counter_ns()
    exec_time__us = (end_time__ns - start_time__ns) / 1000.0
    return result, exec_time__us

# Check result and ignore any errors with truth value of numpy arrays
def check_result(result: Any, expected: int):
    try:
        return bool(result == expected)
    except:
        return False

if __name__ == "__main__":
    colr_init()
    print(f"{Back.WHITE}{Fore.BLACK} -* Advent of Code 2021 *- {Style.RESET_ALL}")
    print("Challenge #01")
    print("Ethan Kessel")
    print(Style.DIM + "-" * 24 + Style.RESET_ALL)

    pwd = path.dirname(__file__)
    with open(path.join(pwd, "input.txt")) as input_file:
        prob_input = input_file.read()
        print(f"{Style.DIM}Loaded input file\n{input_file.name}{Style.NORMAL}")
        print(Style.DIM + "-" * 24 + Style.RESET_ALL)

        for part, soln_func, sample_result in zip((1,2), (pt1, pt2), (PT1_SAMPLE_ANS, PT2_SAMPLE_ANS)):
            print(f"\nRunning part {part}...")

            # Run and check sample
            result, exec_time__us = run_with_input(soln_func, SAMPLE_INPUT)
            print(f"Part {part} sample (exec time {exec_time__us:.1f}us): ", end="")
            # Type comparison to short-circuit before invalid equality comparison
            if check_result(result, sample_result):
                print(f"{Back.GREEN}{Fore.BLACK} PASSED {Style.RESET_ALL}")

                # Run full input
                result, exec_time__us = run_with_input(soln_func, prob_input)
                print(f"Part {part} (exec time {exec_time__us:.1f}us) result: {Style.BRIGHT}{result}{Style.RESET_ALL}")
            else:
                print(f"{Back.RED}{Fore.BLACK} FAILED {Style.RESET_ALL}")
                print(f"Expected {sample_result}, produced:\n{Style.BRIGHT}{result}{Style.RESET_ALL}")
