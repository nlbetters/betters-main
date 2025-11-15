# morse/cli.py

from .codec import encode_text, decode_symbols


BANNER = """
==========================================
            MORSE CODE INTERFACE
    type "help" for the list of commands
===========================================
"""


def print_help():
    print("""
Available commands:

  encode     - Convert plain text to Morse code
  decode     - Convert Morse code (with 1/7 space gaps) back to text
  quit       - Exit the program
  help       - Show the list of commands

Examples:
  encode
  > Enter text: SOS HELP

  decode
  > Enter Morse: ... --- ...       .... . .-.. .--.
""")


def run_cli():
    print(BANNER)

    while True:
        cmd = input("> ").strip().lower()

        if cmd == "quit":
            print("Exiting.")
            break

        elif cmd == "help":
            print_help()

        elif cmd == "encode":
            text = input("Enter text: ").strip()
            morse = encode_text(text)
            print(f"Morse: {morse}")

        elif cmd == "decode":
            morse = input("Enter Morse: ").strip()
            text = decode_symbols(morse)
            print(f"Text: {text}")

        elif cmd == "":
            continue  # ignore blank enter presses

        else:
            print(f"Unknown command: {cmd}")
            print('Type "help" for options.')


if __name__ == "__main__":
    run_cli()
