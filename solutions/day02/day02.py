# ADVENT OF CODE 2021
# Challenge #02
# Ethan Kessel

SAMPLE_INPUT = """\
A Y
B X
C Z\
"""

PT1_SAMPLE_ANS = 15

def pt1(input: str):
    input = input.splitlines()

    score_map = {
        'A': 1,
        'B': 2,
        'C': 3,
        'X': 1,
        'Y': 2,
        'Z': 3,
    }
    win_map = {
        1: 3,
        2: 1,
        3: 2,
    }
    LOSS = 0
    TIE = 3
    WIN = 6

    score = 0
    for round in input:
        opponent = score_map[round[0]]
        you = score_map[round[2]]

        score += you
        if win_map[you] == opponent:
            score += WIN
        elif you == opponent:
            score += TIE
        else:
            score += LOSS

    return score

PT2_SAMPLE_ANS = 12

def pt2(input: str):
    input = input.splitlines()

    score_map = {
        'A': 1,
        'B': 2,
        'C': 3,
        'X': 1,
        'Y': 2,
        'Z': 3,
    }
    win_map = {
        1: 3,
        2: 1,
        3: 2,
    }
    lose_map = {
        1: 2,
        2: 3,
        3: 1,
    }
    LOSS = 0
    TIE = 3
    WIN = 6

    score = 0
    for round in input:
        opponent = score_map[round[0]]
        you_play = round[2]

        match you_play:
            case 'X': # Lose
                you = win_map[opponent]
                # print(you, "L")
                score += LOSS + you
            case 'Y': # Tie
                you = opponent
                # print(you, "T")
                score += TIE + you
            case 'Z': # Win
                you = lose_map[opponent]
                # print(you, "W")
                score += WIN + you
            case _:
                print("uh oh")

    return score

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
    print("Challenge #02")
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
