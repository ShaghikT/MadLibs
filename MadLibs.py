from ast import Try, While
import random
from webbrowser import get

def get_number_input(prompt):
    user_input = input(prompt).strip()
    while user_input == "" or not user_input.isdigit():
        print("Please enter a valid number.")
        user_input = input(prompt).strip()
    return user_input


def get_word_input(prompt):
    user_input = input(prompt).strip()
    while user_input == "" or not all(char.isalpha() or char.isspace() for char in user_input):
        print("Invalid input. Please enter a word.")
        user_input = input(prompt).strip()
    return user_input

GameModeOn = True

while GameModeOn:

  print("Welcome to Mad Libs!")
  print("Choose a template by entering 1:Hospital 2:Camping 3:Castle :")
  templateChoice = input("Enter 1, 2, 3, or type R for random choice: ")


  while templateChoice not in ["1", "2", "3","r", "R"]:
    print("Invalid choice. Try again.")
    templateChoice = input("Enter 1, 2, 3, or type R for random choice: ")

  if templateChoice.lower() == "r":
      templateChoice = random.choice(["1", "2", "3"])
      print(f"Randomly selected template: {templateChoice}")

   
  if templateChoice == "1":
     number1 = get_number_input("Type a number: ")
     measure_time = get_word_input("Type a measure of time: ")
     transportation = get_word_input("Type a mode of transportation: ")
     adjective1 = get_word_input("Type an adjective: ")
     adjective2 = get_word_input("Type another adjective: ")
     noun1 = get_word_input("Type a noun: ")
     color = get_word_input("Type a color: ")
     body_part1 = get_word_input("Type a body part: ")
     verb1 = get_word_input("Type a verb: ")
     number2 = get_number_input("Type a number: ")
     noun2 = get_word_input("Type a noun: ")
     noun3 = get_word_input("Type a noun: ")
     body_part2 = get_word_input("Type another body part: ")
     verb2 = get_word_input("Type another verb: ")
     noun4 = get_word_input("Type a noun: ")
     adjective3 = get_word_input("Type another adjective: ")
     silly_word = get_word_input("Type a silly word: ")
     noun5 = get_word_input("Type a noun: ")

     print (f""" It was about {number1} {measure_time} ago when I arrived at the hospital in a {transportation}. 
      The hospital is a {adjective1} place, there are a lot of {adjective2} {noun1} here.  There are nurses 
      here who have {color} {body_part1}. If someone wants to come into my room I told them that they have to 
      {verb1} first. I’ve decorated my room with {number2} {noun2}.  Today I talked to a doctor and they were 
      wearing a {noun3} on their {body_part2}. I heard that all  doctors {verb2} {noun4} every day for breakfast. 
      The most {adjective3} thing about being in the 
      hospital is the {silly_word} {noun5}!""")

  elif templateChoice == "2":
    name = get_word_input("Type a person's name: ")
    noun1 = get_word_input("Type a noun: ")
    feeling1 = get_word_input("Type a feeling (adjective): ")
    verb1 = get_word_input("Type a verb: ")
    feeling2 = get_word_input("Type another feeling (adjective): ")
    animal1 = get_word_input("Type an animal: ")
    verb2 = get_word_input("Type another verb: ")
    color1 = get_word_input("Type a color: ")
    verb_ing = get_word_input("Type a verb ending in 'ing': ")
    adverb = input("Type an adverb ending in 'ly': ")
    number1 = get_number_input("Type a number: ")
    measure_time = get_word_input("Type a measure of time: ")
    color2 = get_word_input("Type another color: ")
    animal2 = get_word_input("Type another animal: ")
    number2 = get_number_input("Type another number: ")
    silly_word = get_word_input("Type a silly word: ")
    noun2 = get_word_input("Type another noun: ")


    print(f""" This weekend I am going camping with {name}.I packed my lantern, sleeping bag, 
    and {noun1}. I am {feeling2} we might see a(n) {animal1}, I hear they’re kind of dangerous.
    While we’re camping, we are going to hike, fish, and {verb2}. I have heard that the {color1} 
    lake is great for {verb_ing}. Then we will {adverb} hike through the forest for {number1} 
    {measure_time}. If I see a {color2} {animal2} while hiking, I am going to bring it home as a pet!
    At night we will tell {number2} {silly_word} stories and roast {noun2} around the campfire!!""")

  elif templateChoice == "3":
    name = get_word_input("Type a person's name: ")
    adjective1 = get_word_input("Type an adjective: ")
    color = get_word_input("Type a color: ")
    animal = get_word_input("Type an animal: ")
    place = get_word_input("Type a place: ")
    adjective2 = get_word_input("Type another adjective: ")
    creature1 = get_word_input("Type a magical creature (plural): ")
    adjective3 = get_word_input("Type another adjective: ")
    creature2 = get_word_input("Type another magical creature (plural): ")
    room = get_word_input("Type a room in a house: ")
    noun1 = get_word_input("Type a noun: ")
    noun2 = get_word_input("Type a noun: ")
    noun3= get_word_input("Type another noun: ")
    adjective4 = get_word_input("Type another adjective: ")
    noun4 = get_word_input("Type another noun: ")
    number = get_number_input("Type a number: ")
    measure_time = get_word_input("Type a measure of time: ")
    verb = get_word_input("Type a verb: ")
    adjective5 = get_word_input("Type another adjective: ")
    noun5 = get_word_input("Type another noun: ")


    print(f"""Dear {name}, I am writing to you from a {adjective1} castle in an enchanted forest.
    I found myself here one day after going for a ride on a {color} {animal} in {place}. There are 
    {adjective2} {creature1} and {adjective3} {creature2} here! In the {room} there is a pool full 
    of {noun1}. I fall asleep each night on a {noun2} of {noun3} and dream of {adjective4} 
    {noun4}. It feels as though I have lived here for {number} {measure_time}. I hope one day 
    you can visit, although the only way to get here now is {verb} on a {adjective5} {noun5}!!""")

  continue_game = input("Do you want to play again? (yes/no): ").strip().lower()

  if continue_game == "yes":
    GameModeOn = True

  elif continue_game == "no":
       print("Bye, see you later.")
       GameModeOn = False
  else:
    print("Invalid input. Exiting the game.")
    GameModeOn = False