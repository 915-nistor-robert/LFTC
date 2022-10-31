class Operator:
    def __init__(self, word, stPosition):
        self.word = word
        self.stPosition = stPosition
        self.operators = ['+', '-', '*', '/', ':', '<', '<=', '=', '>=', '>']

    def checkOperator(self, word):
        if word in self.operators:
            return True
        return False

    def getWord(self):
        return self.word

    def getStPosition(self):
        return self.stPosition