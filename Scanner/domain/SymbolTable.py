class SymbolTable:
    def __init__(self):
        self.__identifiers = []

    def put(self, id):
        if id in self.__identifiers:
            return self.__identifiers.index(id)
        else:
            self.__identifiers.append(id)
            return self.__identifiers.index(id)

    def get(self, id):
        return self.__identifiers.index(id)
