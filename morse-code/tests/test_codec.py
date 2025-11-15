# tests/test_codec.py

from morse.codec import encode_text, decode_symbols, LETTER_SEPARATOR, WORD_SEPARATOR


def test_encode_single_word():
    morse = encode_text("SOS")
    # Should be "... --- ..."
    parts = morse.split(LETTER_SEPARATOR)
    assert parts == ["...", "---", "..."]


def test_encode_two_words_spacing():
    morse = encode_text("SOS HELP")
    # We expect exactly one WORD_SEPARATOR (7 spaces) between SOS and HELP
    assert WORD_SEPARATOR in morse
    sos_morse, help_morse = morse.split(WORD_SEPARATOR)
    assert sos_morse.strip() == "... --- ..."
    assert help_morse.strip() == ".... . .-.. .--."


def test_decode_round_trip():
    msg = "HELLO WORLD"
    encoded = encode_text(msg)
    decoded = decode_symbols(encoded)
    assert decoded == msg


def test_decode_known_morse():
    # ... --- ...  (SOS)   with one word: just letter gaps
    morse = "... ... ..."
    decoded = decode_symbols(morse)
    assert decoded == "SSS"

    morse2 = "... --- ...       .... . .-.. .--."
    decoded2 = decode_symbols(morse2)
    assert decoded2 == "SOS HELP"


if __name__ == "__main__":
    test_encode_single_word()
    test_encode_two_words_spacing()
    test_decode_round_trip()
    test_decode_known_morse()
    print("test_codec.py: all tests passed")
