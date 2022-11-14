class PIF:
    def __init__(self, symbolTable):
        self.__pifList = []
        self.symbolTable = symbolTable
        self.reservedWords = ['var', 'if', 'else', 'in', 'every', 'const', 'break', 'null', 'write', 'read', 'while']
        self.operators = ['+', '-', '*', '/', ':', '<', '<=', '=', '>=', '>']
        self.separators = ['[', ']', '{', '}', ';', ':', ' ']

    def genPIF(self, token):
        if self.checkReservedWord(token) or self.checkSeparator(token) or self.checkOperator(token):
            self.__pifList.append((token, '-1'))
        else:
            self.__pifList.append((token, self.symbolTable.get(token)))

    def checkReservedWord(self, token):
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

    def print(self):
        for pif in self.__pifList:
            print(pif[0], "|", pif[1])
