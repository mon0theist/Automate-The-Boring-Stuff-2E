#! /usr/bin/python
#
# ATBS2E - Chapter 4 - Coin Flip Streaks
#
# For this exercise, we’ll try doing an experiment. If you flip a coin 100 times
# and write down an “H” for each heads and “T” for each tails, you’ll create a
# list that looks like “T T T T H H H H T T.” If you ask a human to make up 100
# random coin flips, you’ll probably end up with alternating head-tail results
# like “H T H T H H T H T T,” which looks random (to humans), but isn’t mathematically
# random. A human will almost never write down a streak of six heads or six tails
# in a row, even though it is highly likely to happen in truly random coin flips.
# Humans are predictably bad at being random.
#
# Write a program to find out how often a streak of six heads or a streak of six
# tails comes up in a randomly generated list of heads and tails.
#
# Your program breaks up the experiment into two parts:
# the first part generates a list of randomly selected 'heads' and 'tails' values,
# and the second part checks if there is a streak in it.
#
# Put all of this code in a loop that repeats the experiment
# 10,000 times so we can find out what percentage of the coin flips contains a
# streak of six heads or tails in a row. As a hint, the function call random.randint(0, 1)
# will return a 0 value 50% of the time and a 1 value the other 50% of the time.
#
# Of course, this is only an estimate, but 10,000 is a decent sample size. Some
# knowledge of mathematics could give you the exact answer and save you the
# trouble of writing a program, but programmers are notoriously bad at math.

import random

number_of_streaks = 0

for experiment_number in range(10):
    # Code that creates a list of 100 'heads' or 'tails' values.
    flips_list = []
    for i in range(100):
        flip = random.randint(0, 1)
        if flip == 0:
            flips_list.append('T')
        elif flip == 1:
            flips_list.append('H')
    # print(flips)

    # Code that checks if there is a streak of 6 heads or tails in a row.
    # iterate through flips list
    counter = 1
    for i in range(len(flips_list)):
        if flips_list[i] == flips_list[x + 1]:
            # increase counter by 1
            counter += 1
            if counter == 6:
                # 6 count is a streak
                number_of_streaks += 1
                # reset counter after streak
                counter = 1
        elif flips_list[i] != flips_list[x + 1]:
            # reset counter
            counter = 1

print('Chance of streak: %s%%' % (numberOfStreaks / 100))
