class Scanner:
    def __init__(self, filePath, reservedWords, operators, separators):
        self.filePath = filePath
        self.reservedWords = reservedWords
        self.operators = operators
        self.separators = separators
        self.file = open(self.filePath, 'r')

    def scan(self):
        lines = self.file.readlines()
        count = 0
        for line in lines:
            count += 1
            words = line.strip().strip(' ')
            print(words.strip(' '))

    def checkReservedWord(self,token):
        if token in self.reservedWords:
            return True
        return False

    def checkOperator(self, token):
        if token in self.operators:
            return True
        return False

    def checkSeparator(self, word):
        if word in self.separators:
            return True
        return False
