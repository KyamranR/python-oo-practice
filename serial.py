"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """Making new generator"""
        self.num = start
        self.start = start

    def __repr__(self):
        """Showing nicer appearance in debugging message"""
        return f"<SerialGenerator start={self.start} num={self.num}"

    def generate(self):
        """Return next serial"""
        current_num = self.num
        self.num += 1
        return current_num
    
    def reset(self):
        """Reset number"""
        self.num = self.start

