import unittest
from task2 import *


class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz(self):
        # Test cases
        self.assertEqual(fizz_buzz(3), 'Fizz')  # divisible by 3
        self.assertEqual(fizz_buzz(5), 'Buzz')  # divisible by 5
        self.assertEqual(fizz_buzz(15), 'FizzBuzz')  # divisible by both
        self.assertEqual(fizz_buzz(4), '4')  # not divisible by 3 or 5
        self.assertEqual(fizz_buzz(20), 'Buzz')  # divisible by 5, not 3
        # Edge cases
        self.assertEqual(fizz_buzz(1), '1')  # single digit
        self.assertEqual(fizz_buzz(100), 'Buzz')  # large number divisible by 5

    #sort
    def test_sort_list(self):
        # Test case 1: Sorting a list of integers
        unsorted_list = [5, 2, 8, 3, 1]
        expected_sorted_list = [1, 2, 3, 5, 8]
        self.assertEqual(sort_list(unsorted_list), expected_sorted_list)

    def test_sort_list_strings(self):
        # Test case 2: Sorting a list of strings
        unsorted_list = ['banana', 'apple', 'cherry']
        expected_sorted_list = ['apple', 'banana', 'cherry']
        self.assertEqual(sort_list(unsorted_list), expected_sorted_list)

    def test_sort_duplicates(self):
        # Test case 3: Sorting a list with duplicates
        unsorted_list = [2, 1, 2, 3, 1]
        expected_sorted_list = [1, 1, 2, 2, 3]
        self.assertEqual(sort_list(unsorted_list), expected_sorted_list)

    # search
    def test_found_in_middle(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 5
        self.assertEqual(binary_search(arr, target), 4)  # index 4 is the correct position

    def test_found_at_beginning(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 1
        self.assertEqual(binary_search(arr, target), 0)  # index 0 is the correct position

    def test_found_at_end(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 9
        self.assertEqual(binary_search(arr, target), 8)  # index 8 is the correct position

    def test_not_found(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 10
        self.assertEqual(binary_search(arr, target), -1)  # not found, return -1

    def test_empty_array(self):
        arr = []
        target = 5
        with self.assertRaises(ValueError):
            binary_search(arr, target)  # raise ValueError for empty array

    # Rock paper scissors
    def test_win_player1(self):
        # Test case: Player 1 chooses "rock" and Player 2 chooses "scissors"
        player1_choice = "rock"
        player2_choice = "scissors"
        winner = play_rock_paper_scissors(player1_choice, player2_choice)
        self.assertEqual(winner, "Player 1")

    def test_win_player2(self):
        # Test case: Player 1 chooses "paper" and Player 2 chooses "rock"
        player1_choice = "paper"
        player2_choice = "rock"
        winner = play_rock_paper_scissors(player1_choice, player2_choice)
        self.assertEqual(winner, "Player 1")

    def test_tie(self):
        # Test case: Both players choose "paper"
        player1_choice = "paper"
        player2_choice = "paper"
        winner = play_rock_paper_scissors(player1_choice, player2_choice)
        self.assertEqual(winner, "Tie")

    def test_invalid_input(self):
        # Test case: Invalid input (e.g. "foo" instead of "rock", "paper", or "scissors")
        player1_choice = "foo"
        player2_choice = "rock"
        with self.assertRaises(ValueError):
            play_rock_paper_scissors(player1_choice, player2_choice)

    def test_type_mismatch(self):
        # Test case: Input is not a string (e.g. integer or float)
        player1_choice = 42  # integer
        player2_choice = "rock"
        with self.assertRaises(TypeError):
            play_rock_paper_scissors(player1_choice, player2_choice)

if __name__ == '__main__':
    unittest.main()