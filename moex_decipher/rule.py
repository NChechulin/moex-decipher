from pydantic import BaseModel
from typing import List, Set


class Rule(BaseModel):
    """Describes a rule which the words are matched agains"""
    length: int
    same_characters_positions: List[int]
    matched_characters: Set[str] = set()

    def __get_chars_at_desired_positions(self, word: str) -> List[str]:
        """Returns chars at positions described in `same_characters_positions`"""
        return [word[pos] for pos in self.same_characters_positions]

    def matches(self, word: str) -> bool:
        """Checks whether a given word matches current rule"""
        if len(word) != self.length:
            return False

        # If chars at positions from `same_characters_positions` are same,
        # Then length of set is 1 and the word matches
        return len(set(self.__get_chars_at_desired_positions(word))) == 1

    def save_chars_at_desired_positions(self, word: str) -> None:
        """Saves the chars at desired positions to the list of possible answers"""
        self.matched_characters |= set(self.__get_chars_at_desired_positions(word))

