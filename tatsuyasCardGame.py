import random
import json
import sys

class Card:
    def __init__(self,name,cost,damage,permanence,effect):
        self.name       = str(name)
        self.cost       = int(cost)
        self.permanence = int(permanence)
        self.damage     = int(damage)
        self.effect     = str(effect)
     
    def prettyPrint(self):
    # Prints a nicely formatted string of the card's values
        print(
          "name:        " + self.name               + "\n" +
          "cost:        " + str(self.cost)          + "\n" +
          "permanence:  " + str(self.permanence)    + "\n" +
          "damage:      " + str(self.damage)        + "\n" +
          "effect:      " + self.effect             + "\n"
        )
# Default values for command line flags
cardFileName = "cards.json"
# Read command line flags
for i in range(len(sys.argv)):
    if(sys.argv[i] == "-cards"):
        cardFileName = sys.argv[i+1]
# Initialize values
DECK_SIZE = 30
cardFile = open(cardFileName, 'r')
cards = json.load(cardFile)
cardFile.close()
ListOfCards = []
for card in cards:
    ListOfCards.append(Card(card["name"],card["cost"],
                            card["damage"],card["permanence"],
                            card["effect"]))
# Create random deck from list of cards
Deck = []
for i in range(DECK_SIZE):
    Deck.append(ListOfCards[random.randint(0, len(ListOfCards)-1)])
# Print out random deck
print("DECK:")
for card in Deck:
    card.prettyPrint()
# Begin game
Hand = []
Graveyard = []
while(True):
    inp = input("Enter command: ")
    if(inp == "hand"):
        for card in Hand:
            card.prettyPrint()
    if(inp == "draw"):
        Hand.append(Deck.pop())
    if(inp == "damage"):
        inp = input("Take how much damage: ")
        for i in range(int(inp)):
            Graveyard.append(Deck.pop())
    if(inp == "deck"):
        print("You have ", len(Deck), " cards left in your deck")
    if(inp == "play"):
        inp = input("Enter card name to play: ")
        foundCard = False
        for card in Hand:
            if(card.name == inp):
                Graveyard.append(card)
                Hand.remove(card)
                foundCard = True
                break
        if(not foundCard):
            print("Card ", inp, " is not in your hand.")
    if(inp == "graveyard"):
        for card in Graveyard:
            card.prettyPrint()
    if(inp == "help"):
        print("Commands:")
        print("  hand: View hand")
        print("  draw: Draw a card")
        print("  damage: Will ask for a number, then you take that much damage")
        print("  deck: The number of cards left in your deck")
        print("  play: Will ask you for a card name to play from your hand")
        print("  graveyard: View graveyard")
        print("  help: Shows this message")