from game_data import *
from art import *
import random
score = 0
print(logo)
print("Hi! Welcome to Higher-Lower. Select A or B to pick which famous personality has the higher amount of followers", end = '\n\n\n\n')



# select a random individual in the list
def random_person_picker():
  '''return a tuple  (1, 8) two distinct numbers in the set data'''
  a = random.randint(0, len(data))
  b = random.randint(0, len(data))
  while a == b:
    b = random.randint(0, len(data))

  return (a,b)

def unpack(t):

  a = random_person_picker()[t]
  name = data[a]['name']
  description = data[a]['description']
  country = data[a]['country']
  return {'name': name, 'description': description, 'country': country}


for i in range(1):
  print(f"Compare {unpack(0)['name']}, {unpack(0)['description']}, from {unpack(0)['country']} {vs} {unpack(1)['name']}, {unpack(1)['description']}, from {unpack(1)['country']}")

b = random_person_picker()[1]
name = data[b]['name']
description = data[b]['description']
country = data[b]['country']

#print(f"{name} who is a {description} from {country}!")



#needs to compare their follower count. Which is higher
data[a]['follower_count'] > data[b]['follower_count']
# needs to accept the user's A or B
guess = input("Who has more followers? Type 'A' or 'B'").lower()

if data[a]['follower_count'] > data[b]['follower_count']:
  if guess == 'a':
    score +=1
    #introduce a new person
    #redo the question
  else:
    answer = data[a]['name']
    print(f"Sorry, the answer was {answer}. Your score was {score}")
if guess == 'b':
  score +=1
  #introduce a new person


# needs to :conditional: user matches with follower-comparison or no?
#if no, report their score
#if yes, increase their score by 1

#the new person in the previous round becomes the old person
#select a random individual

print(data[1])
print(data[1]['name'] )
random.randint(0, len(data))