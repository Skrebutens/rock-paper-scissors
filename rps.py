#
# ROCK, PAPER, SCISSORS - Iterācija 1
# 
# 1. Spēle prasa ievadīt ciparu no 1 līdz 3 (izmanto input, https://www.w3schools.com/python/python_user_input.asp)
# 2. Dators iedomājas ciparu no 1 līdz 3  (izmanto random, https://www.w3schools.com/python/ref_random_randint.asp)
# 3. Atkarībā no ievadītajiem cipariem un datora, izdrukā paziņojumu par zaudējumu, uzvaru, vai neizšķirtu (izmanto if, else https://www.w3schools.com/python/python_conditions.asp)
#

ROCK = "1"
SCISSOR = "2"
PAPER = "3"

print("Welcome to Rock, Paper, Scissors!")
print("Its your turn to make your move")
Move = input("Make your choice:")
print("You chose: " + Move)

if Move == ROCK:
    print("Akmens")
if Move == SCISSOR:
    print("Šķēres")
if Move == PAPER:
    print("Papīrs")

import random
result = str(random.randint(1, 3))
print("Computer chose:" + result)

if result == ROCK:
    print("Akmens")
if result == SCISSOR:
    print("Šķēres")
if result == PAPER:
    print("Papīrs")

if Move == result:
    print("DRAW")
elif Move == ROCK and result == SCISSOR:
    print("Computer chose SCISSORS, you WON!")
elif Move == SCISSOR and result == PAPER:
    print("Computer chose PAPER, you WON!")
elif Move == PAPER and result == ROCK:
    print("Computer chose ROCK, you WON!")
elif Move == PAPER and result == SCISSOR:
    print("Computer chose SCISSORS, you LOSE!")
elif Move == SCISSOR and result == ROCK:
    print("Computer chose ROCK, you LOSE!")
elif Move == ROCK and result == PAPER:
    print("Computer chose PAPER, you LOSE!")
