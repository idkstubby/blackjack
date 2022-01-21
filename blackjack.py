import random
count = 0
random_number = 0

## This is the code which makes the blackjack actually work ##

user_answer = input("Take a card y/n: ")
while user_answer:
  while count < 22:
    if user_answer == "y":
        random_number = random.randrange(1, 10)
        count = count + random_number
        print("Your score is",count)
        if count > 21:
          print("You lost! Your final score was",count)
          user_answer = None
        if count == 21:
          print("You won! You reached 21!")
          user_answer = Noney
        if user_answer != None:
          user_answer = input("Take a card y/n: ")
    if user_answer == "n":
      random_number = random.randrange(1, 10)
      correct = count + random_number
      if random_number + count == 21:
         print("You made the wrong decision! Your final score was",count,"but it could have been 21!")
      if random_number + count >= 22:
        print("You made the right decision! Your score is",count,"but if you took another card it would've been",correct)
      if random_number + count <= 20:
        print("You made the wrong decision, your score was",count,"but it could have been",correct,"if you took another card")
        user_answer = None
        
        
close = input("You finished the game, in order to play it again close and repon this program. ")
##----------------------------------------------------------##
