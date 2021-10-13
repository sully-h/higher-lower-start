from game_data import data
from art import logo
import random
print(logo)
print("Hi! Welcome to Higher-Lower. Select A or B to pick which famous personality has the higher amount of followers", end = '\n\n\n\n')



def game_play():
  score = 0
  a = random.choice(data)
  b = random.choice(data)
  while a == b:
    b = random.choice(data)

  while True:
    print("Compare: ")
    print(f"{a['name']} who is a {a['description']} from {a['country']}!")
    print(f"{b['name']} who is a {b['description']} from {b['country']}!")

    guess = input("\nWho has more followers? Type 'A' or 'B' (Type q to quit): ").lower()

    if guess == "q":
      print("Thank you for playing!, bye.")
      break
    else:
      if guess == "a":
        if a["follower_count"] > b["follower_count"]:
          score += 1
          print(f"You got it right!, you score is {score}")
        else:
          print(f"Sorry worng answer!, your score is {score}")
      if guess == "b":
        if b["follower_count"] > a["follower_count"]:
          score += 1 
          print(f"You got it right!, you score is {score}")
        else:
          print(f"Sorry worng answer!, your score is {score}")

    a = b
    b = random.choice(data)
    while a == b:
      b = random.choice(data)
    print('\n\n')

if __name__ == "__main__":
  game_play()
