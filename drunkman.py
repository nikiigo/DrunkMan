import logging
import random
import sys
from fractions import Fraction

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

n = 10000  # Number of runs
fp = 1 / 3  # step toward fall probability
pos = 2  # initial position (1 is in 1 step to fall)
max_steps = 1000  # Almost infinity

faults = 0
for attempts in range(1, n+1):
    steps = 0
    cur_pos = pos
    while cur_pos > 0 and steps < max_steps:
        steps += 1
        if random.SystemRandom(attempts).random() < fp:
            cur_pos -= 1
        else:
            cur_pos += 1
        # logging.debug(f'current position = {cur_pos}')
        if cur_pos == 0:
            faults += 1
            logging.debug(f'saves ratio = {1 - faults/attempts}, {faults}, {attempts}')
            logging.debug(f'steps required to fall = {steps}')
        elif steps == max_steps:
            logging.debug(f'saves ratio = {1 - faults/attempts}, {faults}, {attempts}')
            logging.debug(f'steps completed = {steps}')
print(f' experimental result: saves ratio = {1 - faults/attempts}.')
print(f' ratio = {Fraction(1 - faults/attempts).limit_denominator()}.')
