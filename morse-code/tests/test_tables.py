# tests/test_tables.py

from morse.tables import MORSE_CODE, REVERSE_CODE


def test_round_trip_letters():
    # Every MORSE_CODE entry should be invertible by REVERSE_CODE
    for ch, code in MORSE_CODE.items():
        assert REVERSE_CODE.get(code) == ch


def test_known_values():
    # Spot-check a few that are standard
    assert MORSE_CODE["S"] == "..."
    assert MORSE_CODE["O"] == "---"
    assert REVERSE_CODE[".-"] == "A"
    assert REVERSE_CODE["-..."] == "B"


if __name__ == "__main__":
    # simple runner if you call this file directly
    test_round_trip_letters()
    test_known_values()
    print("test_tables.py: all tests passed")
