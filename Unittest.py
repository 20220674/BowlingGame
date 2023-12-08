import unittest

class TestBowlingGame(unittest.TestCase):
    def test_all_strikes(self):
        # Test a game with all strikes
        game = BowlingGame()
        for _ in range(12):  # 12 rolls for 10 frames and two bonus rolls
            game.roll(10)
        self.assertEqual(game.score(), 300)  # The maximum score for all strikes is 300

    def test_all_spares(self):
        # Test a game with all spares
        game = BowlingGame()
        for _ in range(21):  # 21 rolls for 10 frames and one bonus roll
            game.roll(5)
            game.roll(5)
        self.assertEqual(game.score(), 150)  # The maximum score for all spares is 150

    def test_open_frames(self):
        # Test a game with no strikes or spares, only open frames
        game = BowlingGame()
        for _ in range(20):  # 20 rolls for 10 frames
            game.roll(3)
        self.assertEqual(game.score(), 60)  # Each frame scores 3, so the total is 60

    def test_mixed_frames(self):
        # Test a game with a combination of strikes, spares, and open frames
        game = BowlingGame()
        rolls = [10, 3, 7, 6, 2, 9, 1, 10, 10, 10, 8, 0, 2, 3, 6, 4, 10]
        for roll in rolls:
            game.roll(roll)
        self.assertEqual(game.score(), 166)  # Calculated based on the given rolls

    def test_invalid_rolls(self):
        # Test the behavior with invalid input (rolls exceeding 10 pins)
        game = BowlingGame()
        with self.assertRaises(ValueError):
            game.roll(11)  # Attempting to knock down more than 10 pins in a single roll

if __name__ == '__main__':
    unittest.main()
