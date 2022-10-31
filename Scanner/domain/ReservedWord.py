class ReservedWord:
    def __init__(self, word, stPosition):
        self.word = word
        self.stPosition = stPosition
        self.reservedWords = ['var','if','else', 'in', 'every', 'const','break','null','write','read','while']

    def checkReservedWord(self):
        if self.word in self.reservedWords:
            return True
        return False

    def getWord(self):
        return self.word

    def getStPosition(self):
        return self.stPosition
