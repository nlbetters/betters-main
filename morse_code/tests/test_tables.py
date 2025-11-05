# tests/test_tables.py

import pytest
from morse.tables import MORSE_CODE, REVERSE_CODE



def test_codes_are_unique():
    codes = list(MORSE_CODE.values())
    assert len(codes) == len(set(codes)), "Duplicate Morse codes found"


def test_all_symbols_are_valid():
    # Only dots, dashes, and spaces are allowed
    for ch, code in MORSE_CODE.items():
        assert set(code) <= {".", "-", " "}, f"Invalid symbol in {ch} -> {code}"


def test_reverse_mapping_is_bijective():
    # Every char -> code -> char round-trips (including space)
    for ch, code in MORSE_CODE.items():
        assert code in REVERSE_CODE, f"Missing reverse for {ch} -> {code}"
        assert REVERSE_CODE[code] == ch, f"Round-trip failed for {ch} -> {code}"


def test_reverse_has_no_extras():
    # Reverse map shouldn't contain codes we don't define forward
    forward_codes = set(MORSE_CODE.values())
    reverse_codes = set(REVERSE_CODE.keys())
    assert reverse_codes <= forward_codes, "Reverse contains unknown codes"


@pytest.mark.parametrize(
    "ch,expected",
    [
        ("A", ".-"),
        ("B", "-..."),
        ("S", "..."),
        ("O", "---"),
        ("5", "....."),
        ("0", "-----"),
        (".", ".-.-.-"),
        (",", "--..--"),
        (" ", " "),
    ],
)
def test_known_examples(ch, expected):
    assert MORSE_CODE[ch] == expected
    assert REVERSE_CODE[expected] == ch


def test_keys_are_uppercase_or_space():
    for k in MORSE_CODE.keys():
        assert (k == " ") or (k.upper() == k), f"Key should be uppercase: {k}"
