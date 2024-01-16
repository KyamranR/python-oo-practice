"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """Machine for finding random words
    
    >>> wf = WordFinder("test.txt")
    3 words read

    >>> wf.random() in ["porsche", "lambo", "ferrari"]
    True
    
    >>> wf.random() in ["porsche", "lambo", "ferrari"]
    True

    >>> wf.random() in ["porsche", "lambo", "ferrari"]
    True
    """
    
    def __init__(self, file_path):
        """Reading the file and reporting how many words read"""

        with open(file_path, 'r') as dict_file:
            self.words = self.read_words(dict_file)

        print(f"{len(self.words)} words read")

    def read_words(self, dict_file):
        """Read words into list of words"""
        return [w.strip() for w in dict_file]
    
    def random(self):
        """Return random word"""
        return random.choice(self.words)

        
class SpecialWordFinder(WordFinder):
    """Special word finder that excludes blanks and comments
    
    >>> swf = SpecialWordFinder("test2.txt")
    3 words read

    >>> swf.random() in ["toyota", "mercedes", "bmw"]
    True

    >>> swf.random() in ["toyota", "mercedes", "bmw"]
    True

    >>> swf.random() in ["toyota", "mercedes", "bmw"]
    True
    
    """

    
    def read_words(self, dict_file):
        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]

