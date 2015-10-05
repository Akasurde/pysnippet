# Function taken from cards.py
# Modified for blackjack game in following way:
# Ace card return card value as 11
# All face cards return card value as 10
def convert(x):
    card = x % 13
    # Suit is not required in blackjack but still kept
    suit = 'SHDC'[(x/13)/5]
    if card == 0:
        # if card is ace then convert its value to 11 as per blackjack rule
        card = 11
    elif card == 11 or card == 12 or card == 13:
        # if card is one of the face cards then convert  its value to 10 as per
        # blackjack rule
        card = 10
    return (card, suit)

# function taken from cards.py
# Modified for blackjack game requirement in assignment
# We need to take 5 decks of 52 cards i.e. 260 cards and shuffle them
def draw_n(n):
    from random import sample

    # initialize the list
    cards = []
    # make sure that we have a valid number
    if n > 0 and n <= 52:
        # sample without replacement
        # as per requirement, we need to take 5 deck of 52 cards i.e. 5 * 52 = 260 cards
        for x in sample(xrange(0, 260), n):
            # append the converted card to the list
            cards.append(convert(x))
    return cards

# variable to hold occurance found
found = 0
# sample iterations
chances = 1000
# Shuffle and draw cards
for i in xrange(chances):
    # Draw first two cards from shoe
    cards = draw_n(2)
    #print "Addition %d" %(cards[0][0] + cards[1][0])
    # if addition of both card value is 21 then its blackjack
    if cards[0][0] + cards[1][0] == 21:
        found += 1

print("Probability of finding blackjack in first two cards : %d in sample of %d" %(found, chances))
