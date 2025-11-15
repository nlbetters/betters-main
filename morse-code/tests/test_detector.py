# tests/test_detector.py

from morse.detector import segments_to_morse, segments_to_text
from morse.codec import WORD_SEPARATOR


def test_segments_to_morse_sos_help():
    unit = 0.1  # 100 ms per unit

    # Super rough segments for "SOS HELP"
    # S: ...              O: ---              S: ...
    # Then 7-unit word gap, then HELP: ".... . .-.. .--."
    segments = [
        # S: ...
        (True, 0.1), (False, 0.1),
        (True, 0.1), (False, 0.1),
        (True, 0.1), (False, 0.3),  # 3u letter gap

        # O: ---
        (True, 0.3), (False, 0.1),
        (True, 0.3), (False, 0.1),
        (True, 0.3), (False, 0.3),  # 3u letter gap

        # S: ...
        (True, 0.1), (False, 0.1),
        (True, 0.1), (False, 0.1),
        (True, 0.1), (False, 0.7),  # 7u word gap

        # H: ....
        (True, 0.1), (False, 0.1),
        (True, 0.1), (False, 0.1),
        (True, 0.1), (False, 0.1),
        (True, 0.1), (False, 0.3),  # letter gap

        # E: .
        (True, 0.1), (False, 0.3),  # letter gap

        # L: .-..
        (True, 0.1), (False, 0.1),
        (True, 0.3), (False, 0.1),
        (True, 0.1), (False, 0.1),
        (True, 0.1), (False, 0.3),  # letter gap

        # P: .--.
        (True, 0.1), (False, 0.1),
        (True, 0.3), (False, 0.1),
        (True, 0.3), (False, 0.1),
        (True, 0.1), (False, 0.3),
    ]

    morse = segments_to_morse(segments, unit_duration=unit)

    # Should contain a word separator (7 spaces)
    assert WORD_SEPARATOR in morse

    text = segments_to_text(segments, unit_duration=unit)
    assert text == "SOS HELP"


if __name__ == "__main__":
    test_segments_to_morse_sos_help()
    print("test_detector.py: all tests passed")
