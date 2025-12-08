import random

class Game:
    def __init__(self):
        self.NUM_SIMULATIONS = 10**6
        self.NUM_DICE = 2
        self.DICE_SIDES = 4
        self.NUM_SQUARES = 40
        self.NUM_CARDS = 16

        self.SQUARE_NAMES = [
            "GO", "A1", "CC1", "A2", "T1",
            "R1", "B1", "CH1", "B2", "B3",
            "JAIL", "C1", "U1", "C2", "C3",
            "R2", "D1", "CC2", "D2", "D3",
            "FP", "E1", "CH2", "E2", "E3",
            "R3", "F1", "F2", "U2", "F3",
            "G2J", "G1", "G2", "CC3", "G3",
            "R4", "CH3", "H1", "T2", "H2"
        ]

        self.SQUARE_INDICES = {
            square_name: index
            for index, square_name in enumerate(self.SQUARE_NAMES)
        }

        self.landed = [0] * self.NUM_SQUARES
        self.position = 0

        self.community_chest_position = 0
        self.community_chest_cards = ["GO", "JAIL"]
        self.community_chest_cards += ["NA"] * 14

        self.chance_position = 0
        self.chance_cards = ["GO", "JAIL", "C1", "E3", "H2", "R1", "R", "R", "U", "-3"]
        self.chance_cards += ["NA"] * 6

    def draw_community_chest(self):
        card = self.community_chest_cards[self.community_chest_position]
        self.community_chest_position += 1
        if self.community_chest_position == self.NUM_CARDS:
            random.shuffle(self.community_chest_cards)
            self.community_chest_position = 0
        return card

    def draw_chance(self):
        card = self.chance_cards[self.chance_position]
        self.chance_position += 1
        if self.chance_position == self.NUM_CARDS:
            random.shuffle(self.chance_cards)
            self.chance_position = 0
        return card

    def go_to_position(self, go_to):
        if go_to == "R":
            if self.position < 5 or self.position > 35:
                self.position = 5
            elif self.position < 15:
                self.position = 15
            elif self.position < 25:
                self.position = 25
            else:
                self.position = 35
        elif go_to == "U":
            if self.SQUARE_INDICES["U1"] < self.position < self.SQUARE_INDICES["U2"]:
                self.position = self.SQUARE_INDICES["U2"]
            else:
                self.position = self.SQUARE_INDICES["U1"]
        elif go_to == "-3":
            self.position = (self.position - 3) % self.NUM_SQUARES
        elif go_to != "NA":
            self.position = self.SQUARE_INDICES[go_to]

    def roll(self):
        dice = [
            random.randrange(1, self.DICE_SIDES + 1)
            for _ in range(self.NUM_DICE)
        ]

        self.position = (self.position + sum(dice)) % self.NUM_SQUARES

        if self.SQUARE_NAMES[self.position].startswith("CC"):
            card = self.draw_community_chest()
            self.go_to_position(card)
        elif self.SQUARE_NAMES[self.position].startswith("CH"):
            card = self.draw_chance()
            self.go_to_position(card)
        elif self.SQUARE_NAMES[self.position] == "G2J":
            self.go_to_position("JAIL")

        self.landed[self.position] += 1

    def print_probabilities(self):
        for position, probability in enumerate(self.probabilities):
            print(f"{self.SQUARE_NAMES[position]}: {probability * 100:.2f}%")

    def get_top_three(self):
        top_three = sorted(
            range(self.NUM_SQUARES),
            key=lambda position: self.probabilities[position],
            reverse=True
        )[:3]

        return "".join(
            str(position) if position > 9 else "0" + str(position)
            for position in top_three
        )

    def calculate_probabilities(self):
        self.probabilities = [
            frequency / self.NUM_SIMULATIONS
            for frequency in self.landed
        ]

    def main(self):
        for _ in range(self.NUM_SIMULATIONS):
            self.roll()
        self.calculate_probabilities()
        return self.get_top_three()

game = Game()
print(game.main())