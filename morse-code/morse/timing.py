# timing.py
# Helper functions for Morse timing based on words per minute (WPM).

# - dot = 1 unit
# - dash = 3 units
# - gap between parts of a letter = 1 unit
# - gap between letters = 3 units
# - gap between words = 7 units


UNIT_FACTOR = 1.2  # seconds per "PARIS" timing unit at 1 WPM


def unit_seconds(wpm: float) -> float:
    """
    Return the length of a single Morse time unit (a dot) in seconds
    for a given words-per-minute speed.
    """
    if wpm <= 0:
        raise ValueError("wpm must be positive")
    return UNIT_FACTOR / float(wpm)


def durations(wpm: float) -> dict[str, float]:
    """
    Return a dictionary of standard Morse durations (in seconds) for:
    - dot
    - dash
    - intra  (gap between elements within a character)
    - letter_gap (gap between characters)
    - word_gap   (gap between words)
    """
    u = unit_seconds(wpm)
    return {
        "dot": u,
        "dash": 3 * u,
        "intra": u,
        "letter_gap": 3 * u,
        "word_gap": 7 * u,
    }
