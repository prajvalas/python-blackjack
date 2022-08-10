# python-blackjack

This is the Black Jack game.

Your goal --> Beat The Dealer

How do you beat the dealer?
    - By drawing a hand value that is higher than the dealer’s hand value but less than 21
    - By the dealer drawing a hand value that goes over 21, while you stand at one lower than 21
    - By drawing a hand value of 21 on your first two cards(Black Jack), when the dealer does not

How do you lose to the dealer? 
    - Your hand value exceeds 21.
    - The dealers hand has a greater value than yours at the end of the round
 
How Do You Find a Hand’s Total Value?
  Blackjack is played with multiple(upto 6) decks of 52 playing cards and suits don’t matter.
  - 2 through 10 count at face value, i.e. a 2 counts as two, a 9 counts as nine.
  - Face cards (J,Q,K) count as 10.
  - Ace can count as a 1 or an 11 depending on which value helps the hand the most.
  
How does the game work step by step?
    ** PLAYER **
  - Both the dealer and player get two random cards
  - The player can see both of their cards and hence calculate their hand value
  - The player can see only one of the dealer's cards
  - Player decides if he wants to draw another card or stand(pass) with what he has
  - If the player decides to draw another card and if his new hand value exceeds 21, he loses without even checking the dealer cards
  - However, if the player decides to stand with a hand value of less than or equal to 21, the dealer plays
  
  ** DEALER **
  - The dealer can see both the player's as well as his own cards
  - He must keep drawing cards till his hand value is less than or equal to 16
  - He must stand(pass) with his cards once his hand value is greater than or equal to 17
  
  ** OUTCOME **
  - If at the end of dealer's play the players hand value is greater than that of the dealer's hand value, the player wins, or vice versa
  - If both the player's and dealer's hand value equals, it is considered a DRAW
  - If the dealer exceeds 21 while player is below or equal to 21, the player wins.
  
  
![blackjack](https://user-images.githubusercontent.com/68190956/183972601-05e49c10-a231-4adb-87bd-8d8f78da8a51.jpeg)
