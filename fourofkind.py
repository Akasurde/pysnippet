# use your teacher's cards.py here
import cards

# variable to hold count event
found = 0
# sample space
chances = 1000
# for given sample space
for i in range(chances):
    # As per requirement draw 5 cards
    hands = cards.draw_n(5)
    # get only digit of card i.e., if 5 spade will return only 5
    card = [c[0] for c in hands]
    allftypes = set(card) # get only unique cards

    # find four of kind in given set of hand
    for f in allftypes:
        if card.count(f) == 4:
            allftypes.remove(f)
            found += 1
            break
        
print("Probability of find in four of a kind in %d : %d " % (chances, found))
