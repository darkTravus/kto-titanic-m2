import unittest
from typing import List

MIN_NAME_LENGTH: int = 7


def count_names_longer_than_min_length(first_names: List[str]) -> int:
    """
    Count the number of names whose length is strictly greater
    than MIN_NAME_LENGTH.
    """
    number_of_long_names: int = 0

    for first_name in first_names:
        if len(first_name) > MIN_NAME_LENGTH:
            number_of_long_names += 1

    return number_of_long_names


class TestCountNamesLongerThanMinLength(unittest.TestCase):

    def test_should_count_names_longer_than_seven_letters(self) -> None:
        first_names: List[str] = [
            "Guillaume",
            "Gilles",
            "Juliette",
            "Antoine",
            "François",
            "Cassandre",
        ]
        result: int = count_names_longer_than_min_length(first_names=first_names)
        self.assertEqual(result, 4)


if __name__ == "__main__":
    unittest.main()
