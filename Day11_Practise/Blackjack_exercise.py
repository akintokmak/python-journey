import random
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)

    return card

dealer_cards = []
dealer_scores = -1

def scores(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


for _ in range(2):
    dealer_cards.append(deal_card())

while sum(dealer_cards) < 17:
    dealer_cards.append(deal_card())

dealer_scores = scores(dealer_cards)
print(f"Dealer hand: {dealer_cards}, dealer score: {dealer_scores}")
