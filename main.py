import art 
import os
import random
print(art.logo)

cards = {"Player1": [],"Computer": [],}
cardList = [11,2,3,4,5,6,7,8,9,10,10,10,10]
def dealer():
  return random.choice(cardList)

def start_game():
  player_card1 = dealer()
  player_card2 = dealer()
  cards["Player1"] = [player_card1,player_card2]
  computer_card1 = dealer()
  cards["Computer"] = [computer_card1]
  print(f"Your cards: {cards['Player1']}, current score: {sum(cards['Player1'])}")
  print(f"Computer first card: {cards['Computer']}")

def get_results():
  total_cards_player1 = sum(cards['Player1'])
  total_cards_computer = sum(cards["Computer"])
  if total_cards_computer > 21 and total_cards_player1 <= 21 or total_cards_player1 == 21:
    print(f"You won! 😀")
    return True
  if total_cards_player1 > 21 and total_cards_computer <= 21 or total_cards_computer == 21:
    print(f"You went over. You lose  🥲")
    return True
 
    
  return False
def deal_card():
  new_card_player1 = dealer()
  new_card_computer = dealer()
  cards["Player1"].append(new_card_player1)
  cards["Computer"].append(new_card_computer)
  current_score = sum(cards['Player1'])
  print(f"Your cards: {cards['Player1']}, current score: {current_score}")
  print(f"Computer first card: {cards['Computer']}")
  
def end_game():
  print("Thank you for playing!")
continue_playing = True
play = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")
if(play == 'n'):
  continue_playing = False
  end_game()
if(play == 'y'):
  start_game()
while continue_playing:
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if another_card == 'y':
      deal_card()
      if(get_results()):
        play = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")
        if( play == 'y'):
          start_game()
        else:
          continue_playing = False
          end_game()
        
    if another_card == 'n':
        continue_playing = False
      
      
