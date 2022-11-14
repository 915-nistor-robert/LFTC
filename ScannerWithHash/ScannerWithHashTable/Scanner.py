import re

from PIF import PIF
from SymbolTable import SymbolTable


class Scanner:
    def __init__(self, operators, separators, reservedWords):
        self.operators = operators
        self.separators = separators
        self.reservedWords = reservedWords
        self.allThree = self.operators + self.separators + self.reservedWords
        self.pif = PIF()
        self.symbolTable = SymbolTable()

    def scan(self, fileName):
        index = 0
        # printing operators, separators, reserved words
        for elem in self.allThree:
            print(index, elem)
            index += 1
        lineNr = 0
        with open(fileName, 'r') as file:
            for line in file:
                lineNr += 1
                for element in self.split_Line(line):
                    if element in self.separators or element in self.operators or element in self.reservedWords:
                        continue
                    elif self.is_id(element):
                        if self.symbolTable.find_pos(element) == -1:
                            self.symbolTable.add(element)
                    elif self.is_const(element):
                        if self.symbolTable.find_pos(element) == -1:
                            self.symbolTable.add(element)
                    else:
                        raise Exception('Lexical error, token: ' + element + ' at line ' + str(lineNr))
        file.close()

        with open(fileName, "r") as file:
            for line in file:
                for element in self.split_Line(line):
                    if element in self.separators or element in self.operators or element in self.reservedWords:
                        if element != ' ':
                            self.pif.add(self.find_pos(element), -1)
                    elif self.is_id(element):
                        self.pif.add("id", (self.symbolTable.symbolTable.hash(element), self.symbolTable.find_pos(element)))
                    elif self.is_const(element):
                        self.pif.add("constant", (self.symbolTable.symbolTable.hash(element), self.symbolTable.find_pos(element)))
        file.close()

        f = open("st.out", "w")
        f.write("{:<15} {:<15} \n".format("Bucket", "Values"))
        index = 0
        while index < self.symbolTable.symbolTable.capacity:
            node = self.symbolTable.symbolTable.items[index]
            if node is not None:
                prev = self.symbolTable.symbolTable.items[index]
                values = []
                while node is not None:
                    values.append(node.key)
                    prev = node
                    node = node.next
                f.write("{:<15} {:<15} \n".format(index, str(values)))
            index += 1
        f.close()

        f = open("pif.out", "w")
        f.write("{:<15} {:<15} \n".format("Token", "ST_Position"))
        for element in self.pif.identifiers:
            f.write("{:<15} {:<15} \n".format(element[0], str(element[1])))
        f.close()

    def find_pos(self,elem):
        index = 0
        for element in self.allThree:
            if elem == element:
                return index
            index += 1

    def is_part_of_op(self,char):
        for op in self.operators:
            if char in op:
                return True
        return False

    def is_id(self, token):
        return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9]|_){,7}$', token) is not None

    def is_const(self, token):
        return re.match('^(0|[\+\-]?[1-9][0-9]*)$|^\".*\"$', token) is not None

    def split_Line(self,line):
        element = ''
        index = 0

        while index < len(line):
            if line[index] == '"':
                if element:
                    yield element
                element = '"'
                index += 1
                while index < len(line) and line[index] != '"':
                    element += line[index]
                    index += 1
                element += line[index]
                index += 1
                yield element
                element = ''

            elif self.is_part_of_op(line[index]):
                if element:
                    yield element
                element = ''
                while index < len(line) and self.is_part_of_op(line[index]):
                    element += line[index]
                    index += 1
                yield element
                element = ''

            elif line[index] in self.separators:
                if element:
                    yield element
                element = line[index]
                index += 1
                yield element
                element = ''

            else:
                element += line[index]
                index += 1

        if element:
            yield element
