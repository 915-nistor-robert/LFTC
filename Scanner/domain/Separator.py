class Separator:
    def __init__(self, word, stPosition):
        self.word = word
        self.stPosition = stPosition
        self.separators = ['[',']','{','}',';',':',' ']

    def checkSeparator(self, word):
        if word in self.separators:
            return True
        return False

    def getWord(self):
        return self.word

    def getStPosition(self):
        return self.stPosition