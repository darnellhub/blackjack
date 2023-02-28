import random
from art import logo
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def dealer():
  deal_cards = random.choice(cards)
  return deal_cards

def calculate_score(card):
  if sum(card) == 21 and len(card) == 2:
    return 0
    game_finished = True
  if sum(card) >= 21:
    game_finished = True  
  if 11 in card and sum(card) > 21:
    card.remove(11)
    card.append(1)
  card_score = sum(card)
  return card_score


def compare(player_score,computer_score):
  if player_score == computer_score:
    print("It's a Draw")
  elif player_score > 21 or computer_score == 0:
    print("Dealer Wins")
  elif computer_score > 21 or player_score == 0:
    print ("You Win. Blackjack!")
  elif player_score > computer_score:
    print("You Win Blackjack!")
  else:
    print("Dealer Wins")
    


def game_time():
  print(logo)
  player_hand= []
  computer_hand= []
  player_score = ""
  computer_score=""
  for _ in range (2):
    player_hand.append (dealer())
    computer_hand.append (dealer())
    game_finished = False
  while not game_finished:
    player_score = calculate_score(player_hand)
    computer_score = calculate_score(computer_hand)
    print(f"Your cards: {player_hand}, current score: {player_score}")
    print(f"Computer's first card: {computer_hand[0]}")
    if player_score == 0 or computer_hand == 0 or player_score > 21:
      game_finished = True     
    else:
     deal_again = input("Do you want another card? ").lower()
     if deal_again == "yes":
       player_hand.append(dealer())
     else:
       while computer_score < 17 and computer_score != 0:
         computer_hand.append(dealer())
         computer_score = calculate_score(computer_hand)
       game_finished = True
  if game_finished == True:
    compare(player_score,computer_score)
    #play_again = input("Do you want to play again? ").lower()
    
 
while input("Do you want to start the game? Yes/No? ").lower() == "yes":
  game_finished = False
  clear()
  game_time()
# if player_start == "no":
#   print("OK, Goodbye.")
else:
  print("OK, Goodbye.")
  
