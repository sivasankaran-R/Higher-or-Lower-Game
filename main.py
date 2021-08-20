import art
import game_data
import random
from replit import clear


def data_format(data):
  data_name = data["name"]
  data_description = data["description"]
  data_country = data["country"]
  return(f"Name is {data_name}, {data_description} and from {data_country}")

def check_answer(guess,data1_count,data2_count):
  if data1_count > data2_count:
    return guess == "a" 
  else:
    return guess == "b"
  

#printing logo of a game
print(art.logo)
score = 0
game_over = False

data2 = random.choice(game_data.data)

while not game_over:
  #picking random from a dict
  data1 = data2
  data2 = random.choice(game_data.data)
  if data1 == data2:
    data2 = random.choice(game_data.data)

  #print it as name,description and country
  print(f"Compare : {data_format(data1)} ")
  print(art.vs)
  print(f"Against : {data_format(data2)} ")

  data1_count = data1["follower_count"]
  data2_count = data2["follower_count"]

  #guess of a User
  guess = input("choose : 'A' or 'B' ").lower()

  #call fuction with new variable
  is_correct = check_answer(guess,data1_count,data2_count)

  clear()
  print(art.logo)

  #print if answer is check or wrong
  if is_correct:
    score += 1
    print(f"you are correct and youe score is {score} \n")
  else:
    game_over = True
    print(f"sorry, you are wrong and Your Final score is {score}")






