import random
class Card:
    def __init__(self,name,cost,health,attack,effect):
        self.name   = name
        self.cost   = cost
        self.health = health
        self.attack = attack
        self.effect = effect

ListOfCards = [
#Spells
    Card("Lightning Bolt", 2, 0, 0, 
         "Focused. Deal 2 damage to any permanent"),
    Card("Restoring Touch", 1, 0, 0,
         "Focused. Heal HP of target permanent by 2."),
    Card("Thought Break", 3, 0, 5, 
         "N/A"),
    Card("Destructive Touch", 3, 0, 0, 
         "Focused. Destroy target permanent."),
    Card("Field Wipe", 4, 0, 0,
         "Destroy all permanents on the field"),
    Card("Confusing Chatter", 3, 0, 2,
         "Target player discards two cards."),
    Card("Organize Thoughts", 3, 0, 0, 
         "Focused. Draw 3 cards, and put two cards into your graveyard from your hand"),
    Card("Divination", 3, 0, 0,
         "Focused. Draw 2 cards"),
    Card("Double Trouble", 3, 0, 1, 
         "Channel twice. You may choose different channels."),
    Card("Pierce", 2, 0, 1, 
         "Pierce"),
    Card("Exhaust", 4, 0, 1,
         "Pierce. All cards dealt damage with this card may not intercept spells this turn."),
    Card("Twist", 4, 0, 1,
         "Opponent puts a card from their hand on top of their deck before damage"),
    Card("Unsummon", 2, 0, 1, 
         "Permanent damaged with this card is put back into players hand. If this card is not intercepted, you may pick any target permanent on channelled row."),
    Card("Rampant Growth", 2, 0, 0, 
         "Focused. Move one of your mana stones."),
    Card("Forgotten Memory", 6, 0, 2,
         "You may play this card from your graveyard."),
    Card("Explosive Gamble", 5, 0, 10,
         "Trample. Deal 5 damage to yourself"),
    Card("Confuse", 4, 0, 4,
         "Return opponent's mana stone in a pool back to reserve."),
    Card("Trade Pact", 2, 0, 0, 
         "Focused. Deal 4 damage to yourself. You may draw 3 cards."),
    Card("Mind Warp", 5, 0, 5,
         "All players discard their hand. Each player draws cards equal to the number of discarded cards."),
    Card("Heal", 6, 0, 0, 
         "Focused. Put 3 cards from your graveyard onto the bottom of your deck"),
    Card("Deny", 4, 0, 3,
         "Opponents channel cannot be used for a turn."),
    Card("Eye for an eye", 3, 0, 0,
         "Sacrifice a permanent. Deal that permanent's damage to target permanent."),
    Card("Fireball", 5, 0, 6,
         "Trample"),
    #Permanents
    Card("Lightning Totem", 1, 1, 1, 
         "N/A"),
    Card("Philosophers Stone", 3, 2, 0, 
         "Start of turn, put top card of your graveyard on the bottom of your deck."),
    Card("Explosive Totem", 2, 2, 2, 
         "If this card is intercepted while channeling, deal damage to all adjacent cards in the row of the intercepting card."),
    Card("Arcane Shot", 3, 2, 2, 
         "When channeling, attacking player may damaage opponent card currently being interacted with. If so, stop channeling."),
    Card("Grimoire", 2, 1, 0, 
         "Once per turn, discard a card, then draw a card."),
    Card("Cancel", 3, 1, 0, 
         "If a permanent damages this card, destroy that permanent."),
    Card("Teleporter", 4, 3, 1,
         "Swap locations of two cards on your field."),
    Card("Forcefield", 4, 6, 1, 
         "N/A"),
    Card("Sacrificial Altar", 1, 3, 0, 
         "Once per turn, you may sacrifice any number of permanents. Add temporary mana stones to your pool equal to the number of permanents sacrificed in this way."),
    Card("Annoying Stairs", 3, 3, 1, 
         "Target player discards a card."),
    Card("Thought Totem", 3, 3, 1, 
         "Draw a card"),
    Card("Black Widower", 3, 1, 3, 
         "Return a card from your graveyard to your hand."),
    Card("Wall", 5, 5, 1, 
         "Can intercept any channel"),
    Card("Pierce Guy 2000", 4, 1, 1, 
         "Pierce"),
    Card("Slime", 6, 3, 3, 
         "Move an opponents mana stone."),
    Card("Power Upper 1999", 4, 2, 2, 
         "All permanents on your channel gain +1 damage."),
    Card("Spikes", 3, 4, 2, 
         "If this card intercepts, deal this card's damage to intercepted card."),
    Card("That card", 7, 1, 0, 
         "All permanents you control cannot be intercepted."),
    Card("Reassembling Skeleton", 2, 1, 1, 
         "May be played from your graveyard."),
    Card("Giant Ball of Eternal Fire", 7, 6, 7, 
         "Trample"),
    Card("Fatty", 6, 6, 6, 
         "N/A"),
    Card("Truce Factory", 3, 1, 1, 
         "Sacrifice this permanent. Opponent may not perform channeling with permanents on the field until your next turn"),
    Card("Ping Factory", 3, 2, 0, 
         "Once per turn, deal 1 damage to target permanent.")
]

Deck = []
for i in range(30):
    Deck.append(ListOfCards[random.randint(0, len(ListOfCards)-1)])

for card in Deck:
    print(card.name)
    print("  Cost: ", card.cost)
    print("  Health: ", card.health)
    print("  Attack: ", card.attack)
    print("  Effect: ", card.effect)

Hand = []
Graveyard = []
while(True):
    inp = input("Enter command: ")
    if(inp == "hand"):
        for card in Hand:
            print(card.name)
            print("  Cost: ", card.cost)
            print("  Health: ", card.health)
            print("  Attack: ", card.attack)
            print("  Effect: ", card.effect)
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
            print(card.name)
            print("  Cost: ", card.cost)
            print("  Health: ", card.health)
            print("  Attack: ", card.attack)
            print("  Effect: ", card.effect)
    if(inp == "help"):
        print("Commands:")
        print("  hand: View hand")
        print("  draw: Draw a card")
        print("  damage: Will ask for a number, then you take that much damage")
        print("  deck: The number of cards left in your deck")
        print("  play: Will ask you for a card name to play from your hand")
        print("  graveyard: View graveyard")
        print("  help: Shows this message")