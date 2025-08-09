import random

lucky_messages = [
    "Lucky you! Jackpot vibes today!",
    "The universe is on your side!",
    "You struck gold!",
    "That's a blazing high score!",
    "You're in the lucky zone!"
]

number = random.randint(1, 100)
print(f"Your number is: {number}")

if number > 90:
    print(random.choice(lucky_messages))
