from ScannerWithHashTable.HashTable import HashTable
from ScannerWithHashTable.LanguageSpecification import reservedWords, separators, operators
from ScannerWithHashTable.Scanner import Scanner
from ScannerWithHashTable.Transition import Transition


class FiniteAutomata:
    def __init__(self):
        self.states = HashTable()
        self.alphabet = HashTable()
        self.initialStates = HashTable()
        self.finalStates = HashTable()
        self.transitions = []
        self.scanner = Scanner(operators, separators, reservedWords)

    def readAutomata(self, fileName):
        with open(fileName, 'r') as file:
            lines = file.readlines()
            for element in lines[0].split(':'):
                self.states.insert(element)
            for element in lines[1].split(':'):
                self.alphabet.insert(element)
            for element in lines[2].split(':'):
                transition = Transition(element.split('`')[0],element.split('`')[1],element.split('`')[2])
                self.transitions.append(transition)
        file.close()


    def split_line(self, line):
        element = ''
        index = 0


