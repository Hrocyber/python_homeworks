import itertools
import random

combinations = [combination for combination in itertools.product(["stone", "paper", "scissors"], repeat=2)]
history = dict.fromkeys(combinations, 0)
def guess_randomly():
    predicted_number = random.choice(["stone", "paper", "scissors"])
    return predicted_number
def guess_shannon(prev, attempt, user_input):
    if attempt < 5:
        predicted_number = guess_randomly()
    else:
        if history[(prev, "stone")] > history[(prev, "paper")] > history[(prev, "scissors")]:
            predicted_number = "paper"
        elif history[(prev, "stone")] < history[(prev, "paper")] < history[(prev, "scissors")]:
            predicted_number = "stone"
        else:
            predicted_number = "scissors"
    """Save history"""
    history[(prev, user_input)] += 1
    return predicted_number
machin_scores = 0
user_scores = 0
prev = "stone"
attempt = 0
while True:
    user_input = input("select  stone or paper  or scissors\n")
    if user_input != "paper" and user_input != "stone" and user_input != "scissors":
        continue
    predicted_number = guess_shannon(prev, attempt, user_input)
    print("machine predicted ", predicted_number)
    if user_input == predicted_number:
        print("account is \n machin ={}, user = {}".format(machin_scores, user_scores))
    elif (user_input == "stone" and predicted_number == "scissors") or\
            (user_input == "paper" and predicted_number == "stone") or \
            (user_input == "scissors" and predicted_number == "paper"):
        user_scores += 1
        print("you won ")
    else:
        machin_scores += 1
        print("you lose ")
        prev = user_input
    print("machin scores =", machin_scores, "\n user_scores = ", user_scores, "\n")