class BowlingGame:
    def __init__(self):
        self.rolls = []  # List to store the number of pins knocked down in each roll

    def roll(self, pins):
        self.rolls.append(pins)  # Add the number of pins for each roll to the list

    def score(self):
        total_score = 0  # Variable to store the total score
        roll_index = 0  # Index to iterate through the rolls

        for frame in range(10):  # Iterate through 10 frames in a game
            if self.is_strike(roll_index):
                # Strike: add 10 plus the bonus for the next two rolls
                total_score += 10 + self.strike_bonus(roll_index)
                roll_index += 1  # Move to the next frame
            elif self.is_spare(roll_index):
                # Spare: add 10 plus the bonus for the next roll
                total_score += 10 + self.spare_bonus(roll_index)
                roll_index += 2  # Move to the next frame
            else:
                # Open frame: add the score of the current frame
                total_score += self.frame_score(roll_index)
                roll_index += 2  # Move to the next frame

        return total_score

    def is_strike(self, roll_index):
        return roll_index < len(self.rolls) and self.rolls[roll_index] == 10

    def is_spare(self, roll_index):
        return (roll_index + 1 < len(self.rolls)) and (self.rolls[roll_index] + self.rolls[roll_index + 1] == 10)

    def strike_bonus(self, roll_index):
        # Sum the next two rolls after a strike
        return sum(self.rolls[roll_index + 1: roll_index + 3])

    def spare_bonus(self, roll_index):
        # Add the number of pins in the next roll after a spare
        return self.rolls[roll_index + 2]

    def frame_score(self, roll_index):
        # Sum the number of pins in the current frame
        return sum(self.rolls[roll_index: roll_index + 2])


def main():
    game = BowlingGame()

    for frame in range(9):
        print(f"Frame {frame + 1}")
        roll1 = int(input("Enter pins knocked down in first roll: "))
        game.roll(roll1)

        if roll1 < 10:
            roll2 = int(input("Enter pins knocked down in second roll: "))
            game.roll(roll2)

        print(f"Current Score: {game.score()}")

    print("Frame 10 (final frame)")
    for roll in range(3):  # Allow up to 3 rolls in the last frame
        roll_pins = int(input(f"Enter pins knocked down in roll {roll + 1}: "))
        game.roll(roll_pins)
        print(f"Current Score: {game.score()}")

    final_score = game.score()
    print(f"Final Score: {final_score}")


if __name__ == "__main__":
    main()
