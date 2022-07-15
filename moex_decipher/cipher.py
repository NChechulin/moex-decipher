from copy import copy
from random import shuffle
from string import ascii_lowercase
from typing import Dict
from pprint import pprint


def generate_letter_mapping() -> Dict[str, str]:
    """Generates a mapping from an english letter to another one (possibly, same)"""
    letters = list(ascii_lowercase)
    shuffled = copy(letters)
    shuffle(letters)

    return dict(zip(letters, shuffled))


def encode(text: str, mapping: Dict[str, str]) -> str:
    """Encodes given text with a given mapping skipping all non-ascii chars"""
    return "".join(
        map(
            lambda c: mapping.get(c, c),
            text.lower(),
        )
    )


def main() -> None:
    text = input("Text to encode: ").lower()
    letter_map = generate_letter_mapping()
    encoded = encode(text, letter_map)
    print(encoded)
    print(text)
    pprint(letter_map)

if __name__ == "__main__":
    main()
