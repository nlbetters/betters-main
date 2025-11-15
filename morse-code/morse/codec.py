# morse/codec.py

from .tables import MORSE_CODE, REVERSE_CODE

# One space between letters, seven between words
LETTER_SEPARATOR = " "
WORD_SEPARATOR = "       "  # 7 units/spaces per ITU


def encode_text(text: str) -> str:
    """
    Convert plain text into a Morse code string using:
      - 1 space/unit between letters
      - 7 spaces/units between words

    Example:
      "SOS HELP" ->
      "... --- ...       .... . .-.. .--."
    """
    text = text.upper().strip()

    if not text:
        return ""

    words = text.split()  # splits on normal spaces between words

    encoded_words = []

    for word in words:
        encoded_letters = []

        for ch in word:
            code = MORSE_CODE.get(ch)
            if code is None:
                # skip characters we don't know how to encode for now
                continue
            encoded_letters.append(code)

        if encoded_letters:
            # join Morse codes for each letter with 1 space
            encoded_words.append(LETTER_SEPARATOR.join(encoded_letters))

    # join word-level Morse groups with 7 spaces
    return WORD_SEPARATOR.join(encoded_words)


def decode_symbols(morse: str) -> str:
    """
    Convert a Morse code string back into plain text, assuming:
      - 1 space between letter codes
      - 7 spaces between word codes
    """
    morse = morse.strip()

    if not morse:
        return ""

    # first split into "word chunks" using the 7-space separator
    word_chunks = morse.split(WORD_SEPARATOR)

    decoded_words = []

    for word_chunk in word_chunks:
        # each word_chunk has letter codes separated by single spaces,
        # like ".... . .-.. .--."
        if not word_chunk:
            continue

        # split on single spaces; filter out any accidental empties
        symbol_codes = [c for c in word_chunk.split(LETTER_SEPARATOR) if c]

        letters = []

        for code in symbol_codes:
            ch = REVERSE_CODE.get(code)
            if ch is None:
                # if unknown pattern -> flag with a question mark
                letters.append("?")
            else:
                letters.append(ch)

        decoded_words.append("".join(letters))

    # join the decoded words with normal single spaces for plain text
    return " ".join(decoded_words)
