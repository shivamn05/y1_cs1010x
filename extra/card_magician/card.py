def card_magician(output, cards, trick):
    for card in cards:
        output = trick(output, card)
    return output

def compare_cards(card1, card2):
    c1 = 'Z' if card1[0] == 'A' else card1[0]
    c1 = 'Y' if card1[0] == 'K' else c1
    c1 = 'B' if card1[0] == 'T' else c1
    c2 = 'Z' if card2[0] == 'A' else card2[0]
    c2 = 'Y' if card2[0] == 'K' else c2
    c2 = 'B' if card2[0] == 'T' else c2
    return card1[1] > card2[1] if c1 == c2 else c1 > c2 # card1 bigger means True

# Get highest card from deck 
def high_card(deck):
    a = '2C'
    b = deck
    c = lambda x,y: x if compare_cards(x,y) else y
    return card_magician(a,b,c)
##


# Sort deck from lowest to highest card
def insert_card(deck, card):
    if deck == ():
        return (card,)
    for i in range(len(deck)):
        if compare_cards(deck[i], card):    # if the i-card is bigger than card
            return deck[:i] + (card,) + deck[i:] # put the card at the ith pos
    return deck + (card,)    # else the card is biggest so put at the end 
            
def sort_deck(deck):
    a =  ()
    b = deck
    c = insert_card
    return card_magician(a, b, c)
##


# Separate cards into 4 suits: Clubs, Diamonds, Hearts, Spades
def suit_card(deck, card):
    if card[1] == 'C':
        return (deck[0] + (card,), deck[1], deck[2], deck[3])
    elif card[1] == 'D':
        return (deck[0], deck[1] + (card,), deck[2], deck[3])
    elif card[1] == 'H':
        return (deck[0], deck[1], deck[2] + (card,), deck[3])
    elif card[1] == 'S':
        return (deck[0], deck[1], deck[2], deck[3] + (card,))

def split_deck(deck):
    a = ((),(),(),())
    b = deck
    c = suit_card
    return card_magician(a,b,c)
##


# Finding unique cards from from a piece of 2 shuffled decks 
def get_unique_card(deck, card):
    if card in deck:
        temp = ()
        for i in deck:
            if i == card:
                continue
            else:
                temp += (i,)
        return temp 
    else:
        return deck + (card,)

def unique_deck(deck):
    a = ()
    b = deck 
    c = get_unique_card
    return card_magician(a,b,c)
##


# Getting a tuple of duplicate cards only - requires improved card_magus
"""
def card_magician(output, cards, trick):
    for card in cards:
        output = trick(output, card)
    return output
"""
def card_magus(init, new, cards, trick, output):
    for card in cards:
        init, new = trick(init, new, card)
    return output(new, init)


duplicate_cards = card_magus((),
                             (),
                             ('8H', '3D', 'AC', '4S', '3D', '9S', 'TD', 'TD'),
                             lambda x, y, z: (x + (z,), y) if z in y and not z in x else (x, y + (z,)),
                             lambda w, v: v)

card_to_count = '3D'
number_of_cards = card_magus(card_to_count,
                             (),
                             ('8H', '3D', 'AC', '4S', '3D', '9S', 'TD', 'TD'),
                             lambda x, y, z: (x, y + ((z,) if z == x else ())),
                             lambda ting, tang: len(ting))

also_number_of_cards = card_magus(0,
                                  0,
                                  ('8H', '3D', 'AC', '4S', '3D', '9S', 'TD', 'TD', '3D', '3D'),
                                  lambda x, y, z: (0, y + 1 if z == card_to_count else y),
                                  lambda rictusempra, everte_statum: rictusempra)
##


# Improved sorting of deck using card_magus
def trick(init, new, card):
    if init == ():
        return ((card,), new)
    for i in range(len(init)):
        if compare_cards(card,init[i]):
            return (init[:i] + (card,) + init[i:], new)
    return (init + (card,), new)

def finalize(a, b):
    if not a:   # if a is empty, return b 
        return b
    if not b:   # if b is empty, return a 
        return a
    a = card_magus((), (), a, trick, finalize) # init, new, cards, trick, output
    b = card_magus((), (), b, trick, finalize)
    return a + b
##

#--- TEST CASE ---#
cards1 = ('QS', 'AC', 'TD', 'JC', 'KH')
cards2 = ('AS', '5S', 'TS', '7S')
cards3 = ('7H', '3S', '6C', 'JH', '2H', '2S', 'TD')
cards4 = ('AS', 'AC', 'TD', 'JC', 'AS', 'TD', 'QH')
cards5 = ('TD', '4C', '6S', '9H', '3D', '5C', 'AH', 'KS', '2C', '7D', '8S', 'QC', 'JH')

sorted_deck = sort_deck(cards2)
# print(sorted_deck)

spdeck = split_deck(cards3)
# print(spdeck)

uncards = unique_deck(cards4)
# print(uncards)

# print(duplicate_cards)
# print(number_of_cards)
# print(also_number_of_cards)

sorted_cards = card_magus((), (), cards5, trick, finalize)
# print(sorted_cards)

# twisted twister with my twisted sister while my toungue twisting this 
# twisted tongue twister 
