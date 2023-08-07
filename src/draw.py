import random

deck = ["The Fool", "The Magician", "The High Priestess"]
positions = ["Upright", "Reversed"]


def draw_card(index, total):
    table = []
    clone_deck = deck.copy()
    for _ in range(total):
        draw = random.choice(clone_deck)
        clone_deck.remove(draw)
        table.append(draw)

    print(table)
    card_result = table[index]
    position_result = random.choice(positions)
    return {"card": card_result, "position": position_result}
